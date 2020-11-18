from behave import *
from selenium import webdriver

@given('I launch chrome browser')
def launchBrowser(context):
    context.driver=webdriver.Chrome()


@when('open orange hrm homepage')
def openHomePage(context):
    context.driver.get("https://opensource-demo.orangehrmlive.com/")


@when('verify that the logo is present on the page')
def verifyLogo(context):
    status=context.driver.find_element_by_xpath("//*[@id='divLogo']/img").is_displayed()
    assert status is True


@then('close the browser')
def closeBrowser(context):
    context.driver.close()
