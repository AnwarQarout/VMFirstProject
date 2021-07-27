*** Settings ***
Suite Setup       Custom Setup
Suite Teardown    Custom Teardown
Resource          variables.robot
Library           MyCustomLibrary.py
Library           SSHLibrary

*** Test Cases ***
printInfoTC
    Get hostname and network configurations

uploadFilesTC
    Copy Directory Into VM And Assure The Files Are Copied

removeFilesTC
    Delete files from directory in VM and assure that they dont exist
