*** Settings ***
Suite Setup       Custom Setup
Suite Teardown    Custom Teardown
Library           SSHLibrary

*** Test Cases ***
printInfoTC
    Get hostname and network configurations

uploadFilesTC
    Copy Directory Into VM And Assure The Files Are Copied

removeFilesTC
    Delete files from directory in VM and assure that they dont exist

*** Keywords ***
Custom Setup
    Open Connection    127.0.0.1    port=2222
    Login    anwar    root1234

Custom Teardown
    Close Connection

Get hostname and network configurations
    ${hostname}    Execute Command    cat /etc/hostname
    Log    ${hostname}
    ${networkConfigs}    Execute Command    ip ad show
    Log    ${networkConfigs}

Copy Directory Into VM And Assure The Files Are Copied
    Execute Command    rmdir toCopy
    Put Directory    toCopy    toCopy
    List Files In Directory    toCopy
    File Should Exist    toCopy/toCopy1.txt
    File Should Exist    toCopy/toCopy2.txt
    File Should Exist    toCopy/toCopy3.txt
    ${count}    Execute Command    ls toCopy | wc -l
    Should be equal    ${count}    3

Delete files from directory in VM and assure that they dont exist
    Execute Command    rm toCopy/toCopy1.txt
    Execute Command    rm toCopy/toCopy2.txt
    Execute Command    rm toCopy/toCopy3.txt
    File Should Not Exist    toCopy/toCopy1.txt
    File Should Not Exist    toCopy/toCopy2.txt
    File Should Not Exist    toCopy/toCopy3.txt
    ${count}    Execute Command    ls toCopy | wc -l
    Should be equal    ${count}    0
