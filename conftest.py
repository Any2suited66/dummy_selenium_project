import pytest
from dummy_page import DummyPage
import chromedriver_autoinstaller
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

chromedriver_autoinstaller.install()

@pytest.fixture(scope="function")
def browser(request):
    options = Options()
    #options.add_argument("--headless")
    options.add_argument("window-size=1920,1080")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    driver = webdriver.Chrome(options=options)
    request.cls.driver = driver
    yield driver
    driver.quit()


@pytest.fixture()
def open_dummy_url(browser):
    browser.get("https://www.github.com")