import time

from playwright.sync_api import Page,expect


def mockRequest(route):
        route.continue_(url="https://rahulshettyacademy.com/api/ecom/order/get-orders-details?id=6a96dc0821054ba46503d285")

def test_mockResponse(browserInstance):
        page = browserInstance
        page.goto("https://rahulshettyacademy.com/client")
        page.route("https://rahulshettyacademy.com/api/ecom/order/get-orders-details?id=*",mockRequest)
        page.get_by_placeholder("email@example.com").fill("mahashakti@gmail.com")
        page.get_by_placeholder("enter your passsword").fill("Sonusanu@1")
        page.get_by_role("button", name = "Login").click()
        page.get_by_role("button", name = "Orders").click()
        page.get_by_role("button", name = "View").first.click()
        expect(page.locator('.blink_me')).to_be_visible()
        # time.sleep(60)