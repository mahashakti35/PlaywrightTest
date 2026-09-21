
from playwright.sync_api import Page, Playwright, expect

from utils.api import ApiUtils;

def test_session_storage(browserInstance,playwright:Playwright):
    page = browserInstance
    api_utils = ApiUtils()
    getToken = api_utils.get_token_from_login(playwright)
    page.add_init_script(f"""localStorage.setItem('token','{getToken}')""")
    page.goto("https://rahulshettyacademy.com/client")
    page.get_by_role("button",name="ORDERS").click()
    expect(page.get_by_text("Your Orders")).to_be_visible()