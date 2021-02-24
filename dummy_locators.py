from selenium.webdriver.common.by import By


class DummyLocators:

    DUMMY_BTN = (By.ID, "SomeButton")
    DUMMY_USERNAME_TXT_BOX = (By.ID, "SomeUsernameTextBox")
    DUMMY_PW_BOX = (By.ID, "SomePWTextBox")
    DUMMY_ASSERT_EL = (By.ID, "AssertDummyElement")
    DUMMY_TEXT_ELEMENMT = (By.ID, "DummyTextElement")
