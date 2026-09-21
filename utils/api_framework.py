from playwright.sync_api import Playwright
import time

coat = "6960eac0c941646b7a8b3e68"
shoes = "6960eae1c941646b7a8b3ed3"
Iphone = "6960ea76c941646b7a8b3dd5"

orderPayLoad = {
    "orders": [
        {
            "country": "India",
            "productOrderedId": Iphone
        }
    ]
}


class ApiUtils:

    base_url = "https://rahulshettyacademy.com"

    def get_token_from_login(self, playwright: Playwright, user_credentials):

        email = user_credentials["userEmail"]
        password = user_credentials["password"]

        context = playwright.request.new_context(
            base_url=self.base_url
        )

        for attempt in range(3):
            try:
                print(f"Login API attempt: {attempt + 1}")

                response = context.post(
                    "/api/ecom/auth/login",
                    data={
                        "userEmail": email,
                        "userPassword": password
                    },
                    timeout=30000
                )

                print(f"Login API status: {response.status}")

                assert response.ok

                responseBody = response.json()
                return responseBody["token"]

            except Exception as e:
                print(f"Login API failed: {e}")

                if attempt == 2:
                    raise

                time.sleep(3)

        context.dispose()

    def createOrder(self, playwright: Playwright, user_credentials):

        token = self.get_token_from_login(
            playwright,
            user_credentials
        )

        context = playwright.request.new_context(
            base_url=self.base_url
        )

        response = context.post(
            "/api/ecom/order/create-order",
            data=orderPayLoad,
            headers={
                "Authorization": token,
                "Content-Type": "application/json"
            },
            timeout=30000
        )

        print(f"Create order status: {response.status}")

        assert response.ok

        response_body = response.json()

        return response_body["orders"][0]