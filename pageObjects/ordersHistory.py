from pageObjects.orderDetailsPage import OrderDetailsPage


class OrderHistory:
    def __init__(self,page):
            self.page = page

    def selectOrder(self,orderID):
        orderRow = self.page.locator("tr").filter(has_text= orderID)
        orderRow.get_by_role("button", name = "View").click()
        orderDetailsPage = OrderDetailsPage(self.page)
        return orderDetailsPage