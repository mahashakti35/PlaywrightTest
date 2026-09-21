
import pytest
from pytest_bdd import given, scenarios, then, when,parsers
from pageObjects.login import LoginPage
from utils.api_framework import ApiUtils

scenarios('features/orderDetails.feature')
@pytest.fixture
def shared_data():
    return {}

@given(parsers.parse('place the item order with {username} and {password}'))
def place_item_order(playwright,username,password,shared_data):
    user_credentials = {}
    user_credentials["userEmail"] = username
    user_credentials["password"] = password
    api_uitls = ApiUtils()
    orderID = api_uitls.createOrder(playwright,user_credentials)
    shared_data["orderID"] = orderID

@given('the user is on landing page')
def user_on_landing_page(browserInstance,shared_data):
    loginPage = LoginPage(browserInstance)
    loginPage.navigate()
    shared_data["login"] = loginPage

@when(parsers.parse('login to portal with {username} and {password}'))
def login(username,password,shared_data):
    loginPage = shared_data["login"]
    dashboardPage = loginPage.login(username,password)
    shared_data["dashboard"] = dashboardPage

@when('Navigate to orders page')
def navigateOrdersPage(shared_data):
    dashboardPage = shared_data["dashboard"]
    orderHistoryPage = dashboardPage.selectOrdersLink()
    shared_data['orderHistoryPage'] = orderHistoryPage

@when('Select the order ID')
def selectOrderID(shared_data):
    orderHistoryPage = shared_data['orderHistoryPage']
    orderID = shared_data["orderID"]
    orderDetailsPage = orderHistoryPage.selectOrder(orderID)
    shared_data["orderDetailsPage"] = orderDetailsPage

@then('the order message is successfully displayed')
def showOrderMessage(shared_data):
    orderDetailsPage = shared_data["orderDetailsPage"]
    orderDetailsPage.verifyOrderMessage()