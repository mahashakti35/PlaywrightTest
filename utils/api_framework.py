from playwright.sync_api import Playwright
coat = "6960eac0c941646b7a8b3e68"
shoes = "6960eae1c941646b7a8b3ed3"
Iphone = "6960ea76c941646b7a8b3dd5"
orderPayLoad = {"orders": [{"country": "India","productOrderedId": Iphone}]}
class ApiUtils:
    base_url = "https://rahulshettyacademy.com"
    # orderID = ""
    def get_token_from_login(self,playwright:Playwright,user_credentials):
        email = user_credentials["userEmail"]
        password = user_credentials["password"]
        context = playwright.request.new_context(base_url= self.base_url)
        response = context.post("/api/ecom/auth/login",data = {"userEmail": email, "userPassword": password})
        assert response.ok
        responseBody = response.json()
        return responseBody["token"]

    def createOrder(self,playwright:Playwright,user_credentials):
        token = self.get_token_from_login(playwright,user_credentials)
        context = playwright.request.new_context(base_url= self.base_url)
        response=context.post("/api/ecom/order/create-order",data = orderPayLoad,headers={
            "Authorization":token,
            "Content-type":"application/json"
        })
        response_body = response.json()
        # self.orderID = response_body['orders'][0]
        return(response_body['orders'][0])
