import time

from playwright.sync_api import Page,expect
text = "Sonu"
def test_placeholderHideShow(browserInstance):
    page = browserInstance
    page.goto("https://rahulshettyacademy.com/AutomationPractice/")
    expect(page.get_by_placeholder("Hide/Show Example")).to_be_visible()
    page.get_by_role("Button",name = "Hide").click()
    expect(page.get_by_placeholder("Hide/Show Example")).not_to_be_visible()
    page.get_by_role("Button",name = "Show").click()
    expect(page.get_by_placeholder("Hide/Show Example")).to_be_visible()

def test_alertBox(browserInstance):
    page = browserInstance
    page.goto("https://rahulshettyacademy.com/AutomationPractice/")
    textbox = page.get_by_placeholder("Enter Your Name")
    expect(textbox).to_be_visible()
    textbox.fill("Sonu")
    page.get_by_role("button",name = "Confirm").click()
    page.on("dialog",lambda dialog:dialog.accept() )

def test_megamenu(browserInstance):
    page = browserInstance
    page.goto("https://rahulshettyacademy.com/AutomationPractice/")
    page.locator("#mousehover").hover()
    page.get_by_role("link",name = "Top").click()

# def test_iframes(browserInstance):
#     page = browserInstance
#     page.goto("https://rahulshettyacademy.com/AutomationPractice/")
#     pageFrame = page.frame_locator("#courses-iframe")
#     pageFrame.get_by_role("link",name = "All Access Plan").click()
#     expect(pageFrame.get_by_text("one Single Subscription")).to_be_visible()

def test_web_tables(browserInstance):
    page = browserInstance
    page.goto("https://rahulshettyacademy.com/seleniumPractise/#/offers")
    for index in range(page.locator("th").count()):
        if page.locator("th").nth(index).filter(has_text= "Price").count() > 0:
            colvalue = index
            print(f"column is {colvalue}")
            break
    riceRow = page.locator("tr").filter(has_text="Rice")
    expect(riceRow.locator("td").nth(colvalue)).to_have_text("37")