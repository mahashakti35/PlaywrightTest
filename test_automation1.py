import time

from playwright.sync_api import Page, expect
import pytest

# def test_automation(playwright):
#     browser = playwright.chromium.launch(headless = False)
#     context = browser.new_context()
#     page = context.new_page()
#     # browser.close()
#     page.goto("")

#it will lunch only in chromium and in headless mode.
# def test_pageshortcut(browserInstance):
#     page.goto("https://facebook.com")
# to make this headed mode->  pytest test_automation1.py::test_pageshortcut --headed

def test_locators(browserInstance):
    page = browserInstance
    page.goto("https://rahulshettyacademy.com/loginpagePractise/")
    page.get_by_label("Username:").fill("rahulshettyacademy")
    page.get_by_label("Password:").fill("Learning@830$3mK2")
    page.get_by_role("combobox").select_option("consult")
    page.get_by_role("link",name = "terms and conditions").click()
    page.locator("#terms").check()
    # page.get_by_role("button",name = "signin").click()
    page.get_by_text("Sign In").click()
    time.sleep(5)
    page.get_by_text("Category 2").click()


def test_practise(browserInstance):
     page = browserInstance
     page.goto("https://rahulshettyacademy.com/loginpagePractise/")
     page.get_by_label("Username:").fill("rahulshettyacademy")
     page.get_by_label("Password:").fill("Learning@830$3mK1")
     page.get_by_text("Sign In").click()
     expect(page.get_by_text("Incorrect username/password.")).to_be_visible()

    #  time.sleep(5)
@pytest.mark.skip
def test_firefox(playwright):
    browser = playwright.firefox.launch()
    page = browser.new_page()
    page.goto("https://rahulshettyacademy.com/loginpagePractise/")
    page.get_by_label("Username:").fill("rahulshettyacademy")
    page.get_by_label("Password:").fill("Learning@830$3mK2")
    page.get_by_role("combobox").select_option("consult")
    page.get_by_role("link",name = "terms and conditions").click()
    page.locator("#terms").check()
    # page.get_by_role("button",name = "signin").click()
    page.get_by_text("Sign In").click()
    page.get_by_text("Category 2").click()
