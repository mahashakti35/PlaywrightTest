from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)

    page = browser.new_page()
    page.goto("https://facebook.com")
    page.wait_for_timeout(5000)
    page.screenshot(path="homepage.png")
    print(page.title())
    print(page.url)
    browser.close()