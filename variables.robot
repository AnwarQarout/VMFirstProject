*** Variables ***
${IP}             127.0.0.1
${username}       anwar
${password}       root1234

*** Keywords ***
Custom Setup
    Open Connection And Login    ${IP}    2222    ${username}    ${password}
    Open Connection    ${IP}    port=2222
    Login    ${username}    ${password}

Custom Teardown
    Close Connection And Logout
    Close Connection

Get hostname and network configurations
    ${hostname}    Execute My Command    cat /etc/hostname
    Log    ${hostname}
    ${networkConfigs}    Execute My Command    ip ad show
    Log    ${networkConfigs}

Copy Directory Into VM And Assure The Files Are Copied
    Execute My Command    rmdir toCopy
    Copy Directory From Source To VM    toCopy    toCopy
    List Files In Directory    toCopy
    File Should Exist    toCopy/toCopy1.txt
    File Should Exist    toCopy/toCopy2.txt
    File Should Exist    toCopy/toCopy3.txt
    ${count}    Execute My Command    ls toCopy | wc -l
    Should be equal    ${count}    3

Delete files from directory in VM and assure that they dont exist
    Delete Files In Directory    toCopy
    File Should Not Exist    toCopy/toCopy1.txt
    File Should Not Exist    toCopy/toCopy2.txt
    File Should Not Exist    toCopy/toCopy3.txt
    ${count}    Execute My Command    ls toCopy | wc -l
    Should be equal    ${count}    0
