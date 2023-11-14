*** Settings ***
Resource  resource.robot
Resource  login_resource.robot
Suite Setup  Open And Configure Browser
Suite Teardown  Close Browser
Test Setup  Create User And Go To Register Page

*** Test cases ***
Register With Valid Username And Password
    Set Username  kallekalle
    Set Password  kallekallekalle123
    Set Password Confirmation  kallekallekalle123
    Submit Register Credentials
    Register Should Succeed

Register With Too Short Username And Valid Password
    Set Username  ka**
    Set Password  kalle123123
    Set Password Confirmation  kalle123123
    Submit Register Credentials
    Register Should Fail With Message  Incorrect username

Register With Valid Username And Invalid Password
    Set Username  kallekalle
    Set Password  kallekallekalle
    Set Password Confirmation  kallekallekalle
    Submit Register Credentials
    Register Should Fail With Message  Incorrect password

Register With Nonmatching Password And Password Confirmation
    Set Username  kallekalle
    Set Password  kallekallekalle123123
    Set Password Confirmation  kallekallekalle123
    Submit Register Credentials
    Register Should Fail With Message  Passwords mismatch

Login After Successful Registration
    Set Username  laralaralara
    Set Password  kallekallekalle123
    Set Password Confirmation  kallekallekalle123
    Submit Register Credentials
    Register Should Succeed
    Go To Login Page
    Set Username  laralaralara
    Set Password  kallekallekalle123
    Submit Credentials
    Login Should Succeed



Login After Failed Registration
    Set Username  skäfä****
    Set Password  kallekallekalle123
    Set Password Confirmation  kallekallekalle123
    Submit Register Credentials
    Register Should Fail With Message  Incorrect username
    Go To Login Page
    Set Username  skäfä****
    Set Password  kallekallekalle123
    Submit Credentials
    Login Should Fail With Message  Invalid username or password

***Keywords***
Register Should Succeed
    Welcome Page Should Be Open

Register Should Fail With Message
    [Arguments]  ${message}
    Register Page Should Be Open
    Page Should Contain  ${message}

Submit Register Credentials
    Click Button  Register

Set Username
    [Arguments]  ${username}
    Input Text  username  ${username}

Set Password
    [Arguments]  ${password}
    Input Password  password  ${password}

Set Password Confirmation
    [Arguments]  ${password_again}
    Input Password  password_confirmation  ${password_again}

Create User And Go To Register Page
    Go To Register Page
    Register Page Should Be Open



