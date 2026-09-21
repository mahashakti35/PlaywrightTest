
import pytest


def pytest_addoption(parser):
    parser.addoption("--browser_name",action="store",default="chrome",help="browser selection")

@pytest.fixture(scope="session")
def user_credentials(request):
    return request.param

@pytest.fixture
def browserInstance(playwright,request):
    browsername = request.config.getoption("browser_name")
    if browsername == "chrome":
        page = playwright.chromium.launch(headless=False).new_context().new_page()
    elif browsername == "firefox":
        page = playwright.firefox.launch(headless=False).new_context().new_page()

    yield page