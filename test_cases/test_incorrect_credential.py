from Pages.SignInPage import SignInScreen
from Pages.WelcomePage import WelcomePage
from test_cases.BaseTest import BaseTest
import pytest
from Utilities.data_provider import get_data


class TestIncorrectCred(BaseTest):
    """
    This negative test will verify if a user tries to log in with an invalid username and/or password they must get a correct error message.
    """
    @pytest.mark.regression
    @pytest.mark.invalid_cred
    def test_happy_path(self, appium_driver):
        sign_page = SignInScreen(self.driver)
        welcome_page = WelcomePage(self.driver)
        welcome_page.click_on_continue_with_email().fill_email(data=get_data('invalid_user')[0][0])
        sign_page.click_to_continue()
        sign_page.fill_password(data=get_data('invalid_user')[0][1])
        sign_page.clik_on_title()
        sign_page.click_to_continue()
        sign_page.verify_error_message()
