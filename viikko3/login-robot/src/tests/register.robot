*** Settings ***
Resource  resource.robot
Test Setup  Create User And Input Login Command



*** Test Cases ***
Register With Valid Username And Password
    Input Credentials  kille  kille123123
    Output Should Contain  New user registered

Register With Valid Username And Too Short Password
    Input Credentials  kille  k
    Output Should Contain  Incorrect password

Register With Valid Username And Long Enough Password Containing Only Letters
    Input Credentials  kille  sadasdasdasdasda
    Output Should Contain  Incorrect password

Register With Already Taken Username And Valid Password
    Input Credentials  kalle  joo123123123123
    Output Should Contain  User with username kalle already exists

Register With Too Short Username And Valid Password
    Input Credentials  ka  joooo123123
    Output Should Contain  Incorrect username

Register With Enough Long But Invald Username And Valid Password
    Input Credentials  asdasdsa*******  juupeli123
    Output Should Contain  Incorrect username



*** Keywords ***
Create User And Input Login Command
    Create User  kalle  kalle123
    Input Register Command