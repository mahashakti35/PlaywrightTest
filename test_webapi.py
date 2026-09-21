import json
import time
from playwright.sync_api import Playwright,expect
import pytest
from pageObjects.login import LoginPage
from pageObjects.dashboard import DashboardPage
from utils.api_framework import ApiUtils

# pytest --browser_name chrome -m smoke -n 4 --tracing on --html=report.html

with open('data/credentials.json') as f:
    test_data = json.load(f)
    user_credentials_list = test_data["user_credentials"]

# @pytest.mark.smoke
@pytest.mark.parametrize('user_credentials',user_credentials_list)
def test_e2e_web_api(playwright:Playwright,browserInstance,user_credentials):
    username = user_credentials["userEmail"]
    password = user_credentials["password"]
    api_uitls = ApiUtils()
    orderID = api_uitls.createOrder(playwright,user_credentials)
 
    loginPage = LoginPage(browserInstance)
    loginPage.navigate()
    dashboardPage = loginPage.login(username,password)
    orderHistoryPage = dashboardPage.selectOrdersLink()
    orderDetailsPage = orderHistoryPage.selectOrder(orderID)
    orderDetailsPage.verifyOrderMessage()
    # page.get_by_role("button", name = "View").first.click()
    # expect(page.get_by_text(api_uitls.orderID)).to_be_visible()
    
    