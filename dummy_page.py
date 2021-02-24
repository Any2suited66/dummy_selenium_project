
import inspect
from datetime import datetime
from decimal import *
from time import sleep

from selenium.common.exceptions import ElementClickInterceptedException, WebDriverException, \
    NoSuchElementException, InvalidElementStateException
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from dummy_locators import DummyLocators


class Page:

    def __init__(self, driver):
        self.driver = driver

    def find_element(self, *locator):
        return self.driver.find_element(*locator)

    def find_elements(self, *locator):
        return self.driver.find_elements(*locator)

    def get_title(self):
        return self.driver.title

    def get_url(self):
        return self.driver.current_url

    def time_stamp_generator(self):
        time_now = datetime.now().strftime('%y.%m.%d%H.%M.%S.%f')
        return time_now

    def wait_for_element(self, *locator):
        return WebDriverWait(self.driver, 45).until(
            EC.element_to_be_clickable((locator)))

    def wait_find_click_element(self, *locator):
        self.wait_for_element(*locator)
        self.find_element(*locator).click()

    def wait_for_one_popup_window(self, time):
        return WebDriverWait(self.driver, time).until(
            EC.number_of_windows_to_be(2))

    def enter_text(self, *locator, text):
        self.wait_for_element(*locator)
        el = self.find_element(*locator)
        try:
            el.clear()
        except InvalidElementStateException:
            pass
        el.send_keys(text)

    def switch_to_frame(self, *locator):
        self.wait_for_element(*locator)
        el = self.find_element(*locator)
        self.driver.switch_to.frame(el)


class DummyPage(Page):

    def __init__(self, driver):
        self.locator = DummyLocators
        super().__init__(driver)

    def enter_username(self):
        self.enter_text(*self.locator.DUMMY_USERNAME_TXT_BOX, text="Username")

    def enter_pw(self):
        self.enter_text(*self.locator.DUMMY_PW_BOX, text="password")

    def click_signin_btn(self):
        self.wait_find_click_element(*self.locator.DUMMY_BTN)

    def text_element(self):
        return self.find_element(*self.locator.DUMMY_TEXT_ELEMENMT)

