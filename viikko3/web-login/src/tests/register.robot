*** Settings ***
Resource  resource.robot
Suite Setup     Open And Configure Browser
Suite Teardown  Close Browser
Test Setup      Reset Application Create User And Go To Register Page

*** Test Cases ***


Login After Successful Registration
    Input Text  username  newuser
    Input Password  password  Valid1234
    Input Password  password_confirmation  Valid1234
    Click Button  Register
    Welcome Page Should Be Open
    Click Link  xpath=//a[@href='ohtu']
    Click Button  Logout
    Login Page Should Be Open
    Input Text  username  newuser
    Input Password  password  Valid1234
    Click Button  Login

Register With Valid Username And Password
    Input Text  username  validuser
    Input Password  password  Valid1234
    Input Password  password_confirmation  Valid1234
    Click Button  Register
    Welcome Page Should Be Open

Register With Too Short Username And Valid Password
    Input Text  username  ab
    Input Password  password  Valid1234
    Input Password  password_confirmation  Valid1234
    Click Button  Register
    Page Should Contain  Username must be at least 3 characters long

Register With Valid Username And Too Short Password
    Input Text  username  validuser
    Input Password  password  short
    Input Password  password_confirmation  short
    Click Button  Register
    Page Should Contain  Password must be at least 8 characters long

Register With Valid Username And Invalid Password
    Input Text  username  validuser
    Input Password  password  onlyletters
    Input Password  password_confirmation  onlyletters
    Click Button  Register
    Page Should Contain  Password must contain at least one non-letter character

Register With Nonmatching Password And Password Confirmation
    Input Text  username  validuser
    Input Password  password  Valid1234
    Input Password  password_confirmation  Mismatch123
    Click Button  Register
    Page Should Contain  Passwords do not match

Register With Username That Is Already In Use
    Input Text  username  takenusername
    Input Password  password  Valid1234
    Input Password  password_confirmation  Valid1234
    Click Button  Register
    Welcome Page Should Be Open
    
    Input Text  username  takenusername
    Input Password  password  AnotherValid123
    Input Password  password_confirmation  AnotherValid123
    Click Button  Register


Login After Failed Registration
    Input Text  username  invalid
    Input Password  password  short
    Input Password  password_confirmation  short
    Click Button  Register
    Page Should Contain  Password must be at least 8 characters long
    Go To Login Page
    Input Text  username  invalid
    Input Password  password  short
    Click Button  Login
    Page Should Contain  Invalid username or password

*** Keywords ***
Welcome Page Should Be Open
    Title Should Be  Welcome to Ohtu Application!

Login Page Should Be Open
    Title Should Be  Login