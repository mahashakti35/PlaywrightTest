from playwright.sync_api import Page

mockData = {"data":[],"message":"No Orders"}
def mockDataHandler(route):
      route.fulfill(
             json = mockData
      )  

def test_mockResponse(browserInstance):
        page = browserInstance
        page.goto("https://rahulshettyacademy.com/client")
        page.route("https://rahulshettyacademy.com/api/ecom/order/get-orders-for-customer/*",mockDataHandler)
        page.get_by_placeholder("email@example.com").fill("mahashakti@gmail.com")
        page.get_by_placeholder("enter your passsword").fill("Sonusanu@1")
        page.get_by_role("button", name = "Login").click()
        page.get_by_role("button", name = "Orders").click()
        noOrderText = page.locator(".mt-4").text_content()
        print(noOrderText)