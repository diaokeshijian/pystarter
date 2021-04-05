*** Settings ***
Documentation    Suite description
Library          OperatingSystem
Library  Selenium2Library
*** Variables ***
${MESSAGE}  Hello, world!

*** Test Cases ***
My Test
    [Documentation]                        Example test
    Log                                    ${MESSAGE}
    log to console  ${CURDIR}
    My Keyword      ${CURDIR}

Another Test
    [Documentation]                         compare the equality
    Should be equal     ${MESSAGE}          Hello, world!

Open CNOM GUI
    open browser  https://ericsson.cnom.com:8585  firefox
    Reload Page
 #   close browser

*** Keywords ***
My Keyword
    [Arguments]                  ${path}
    directory should exist       ${path}