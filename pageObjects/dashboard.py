from pageObjects.ordersHistory import OrderHistory


class DashboardPage:
    def __init__(self,page):
        self.page = page

    def selectOrdersLink(self):
        self.page.get_by_role("button", name = "Orders").click()
        orderHistoryPage = OrderHistory(self.page)
        return orderHistoryPage