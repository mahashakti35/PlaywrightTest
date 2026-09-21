from playwright.sync_api import sync_playwright # type: ignore

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)

    page = browser.new_page()

    page.goto("https://demo.playwright.dev/todomvc")
    page.wait_for_timeout(2000)
    page.locator(".new-todo").fill("Learn Playwright")
    page.locator(".new-todo").press("Enter")
    page.wait_for_timeout(1000)
    page.locator(".new-todo").fill("Learn Python")
    page.locator(".new-todo").press("Enter")
    page.wait_for_timeout(1000)
    page.locator(".new-todo").fill("Build Automation Framework")
    page.locator(".new-todo").press("Enter")
    page.wait_for_timeout(1000)
    page.get_by_placeholder("What needs to be done?").fill("get a job")
    page.get_by_placeholder("What needs to be done?").press("Enter")
    page.wait_for_timeout(1000)
    page.screenshot(path="homepage.png")
    page.locator(".toggle").first.click()
    # page.wait_for_timeout(2000)
    browser.close()

