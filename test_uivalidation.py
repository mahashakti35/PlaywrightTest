import time

from playwright.sync_api import Page, expect

# id - #id, tag - tag, class - .class
def test_dynamicUIValidation(browserInstance):
    page = browserInstance
    page.goto("https://rahulshettyacademy.com/loginpagePractise/")
    page.get_by_label("Username:").fill("rahulshettyacademy")
    page.get_by_label("Password:").fill("Learning@830$3mK2")
    page.get_by_role("combobox").select_option("consult")
    page.get_by_role("link",name = "terms and conditions").click()
    page.locator("#terms").check()
    # page.get_by_role("button",name = "signin").click()
    page.get_by_text("Sign In").click()
    iphone = page.locator("app-card").filter(has_text= "iphone X")
    iphone.get_by_role("button").click()
    time.sleep(1)
    nokia = page.locator("app-card").filter(has_text= "Nokia Edge")
    nokia.get_by_text("Add").click()
    time.sleep(1)
    page.get_by_text("Checkout").click()
    expect(page.locator(".media-body")).to_have_count(2)
    # time.sleep(5)

def test_childPagetest(browserInstance):
    page = browserInstance
    page.goto("https://rahulshettyacademy.com/loginpagePractise/")

    with page.expect_popup() as new_page:
        page.locator('.blinkingText').first.click()
        childPage = new_page.value
        text = childPage.locator(".red").text_content()
        # print(text)
        # words = text.split("at")
        # email = words[1].strip().split(" ")[0]
        email = text.split(" ")[4]
        print(email)
        assert email == "mentor@rahulshettyacademy.com"