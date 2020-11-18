Feature: OrangeHRM Logo

  #@LoginForm

  Scenario: Logo presence on OrangeHRM home page
  Given I launch chrome browser
  When open orange hrm homepage
  And verify that the logo is present on the page
  Then close the browser  
