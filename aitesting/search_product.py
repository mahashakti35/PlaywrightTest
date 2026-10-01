# prompt
# Generate and execute a Playwright test using pytest and Playwright MCP.
# Test Scenario:
# Open https://rahulshettyacademy.com/client
# login using email = mahashakti@gmail.com password = Sonusanu@1
# place an order of ADIDAS ORIGINAL
# after placing order
# go to orders page
# check the first order and check that the first order is adidas original
# Implementation Requirements:
# Use pytest-style structure (functions starting with test_).
# Execute each step interactively through Playwright MCP tools.
# Once all steps succeed, generate and save the final test script as aitesting/search_product.py.
# Run the saved test automatically in headed mode (browser visible).
# If any step or assertion fails, identify and fix the issue, then rerun until the test passes.
# Expected Output:
# A fully working Playwright + pytest test script.
# The script should automate the complete flow described above and successfully validate the product name in the results.
# below code is after simplified and optimized for better readability and maintainability.
import re

from playwright.sync_api import expect, sync_playwright


def test_place_adidas_order_and_verify_first_order():
    email = "mahashakti@gmail.com"
    password = "Sonusanu@1"

    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=False)
        page = browser.new_page()
        try:
            # Login
            page.goto("https://rahulshettyacademy.com/client", wait_until="domcontentloaded")
            page.get_by_placeholder("email@example.com").fill(email)
            page.get_by_placeholder("enter your passsword").fill(password)
            page.get_by_role("button", name="Login").click()
            page.wait_for_url("**/dashboard/dash")

            # Add Adidas to cart
            adidas = page.locator(".card").filter(has_text="ADIDAS ORIGINAL")
            expect(adidas).to_have_count(1)
            adidas.get_by_role("button", name="Add To Cart").click()

            # Go to cart
            page.locator('button[routerlink="/dashboard/cart"]').click()
            page.wait_for_url("**/dashboard/cart")
            expect(page.get_by_text("ADIDAS ORIGINAL", exact=True)).to_be_visible()

            # Checkout and place order
            page.get_by_role("button", name="Checkout").click()
            page.wait_for_url("**/dashboard/order**")

            # Select country
            country = page.get_by_placeholder("Select Country")
            if country.count() and country.is_visible():
                country.click()
                country.press_sequentially("India", delay=120)
                page.get_by_role("button", name=re.compile(r"India$")).click()

            # Complete order
            page.locator("a.action__submit").click()
            page.wait_for_url("**/dashboard/thanks**")

            # Verify order in history
            page.get_by_role("button", name="Orders").click()
            page.wait_for_url("**/dashboard/myorders")
            first_order = page.locator("tbody tr").first
            expect(first_order).to_be_visible()
            expect(first_order).to_contain_text(re.compile("ADIDAS ORIGINAL", re.IGNORECASE))
        finally:
            browser.close()