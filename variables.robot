*** Variables ***
${IP}             127.0.0.1
${username}       anwar
${password}       root1234

*** Keywords ***
Custom Setup
    login to host    ${IP}    2222    ${username}    ${password}
    Open Connection    ${IP}    port=2222
    Login    ${username}    ${password}

Custom Teardown
    logout from host
    Close Connection

Get hostname and network configurations
    ${hostname}    TestSSH.Execute Command    cat /etc/hostname
    Log    ${hostname}
    ${networkConfigs}    TestSSH.execute command    ip ad show
    Log    ${networkConfigs}

Copy Directory Into VM And Assure The Files Are Copied
    TestSSH. Execute Command    rm -r toCopy
    Put Directory    toCopy    toCopy
    List Files In Directory    toCopy
    File Should Exist    toCopy/toCopy1.txt
    File Should Exist    toCopy/toCopy2.txt
    File Should Exist    toCopy/toCopy3.txt
    ${count}    TestSSH. Execute Command    ls toCopy | wc -l
    Should be equal    ${count}    3

Delete files from directory in VM and assure that they dont exist
    delete files in dir    toCopy
    ${count}    TestSSH. Execute Command    ls toCopy | wc -l
    Should be equal    ${count}    0
