from dummy_page import DummyPage
from selenium import webdriver
import pytest


@pytest.mark.usefixtures("browser")
@pytest.mark.usefixtures("open_dummy_url")
class TestDummyPage:

    def test_dummy_something(self):
        dp = DummyPage(self.driver)
        dp.enter_username()
        dp.enter_pw()
        dp.click_signin_btn()
        assert dp.text_element() is not None