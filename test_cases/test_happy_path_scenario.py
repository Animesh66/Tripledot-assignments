from Pages.SignInPage import SignInScreen
from Pages.WelcomePage import WelcomePage
from test_cases.BaseTest import BaseTest
import pytest
from Utilities.data_provider import get_data


class TestVerifyHappyPathScenario(BaseTest):
    """
    This is a positive test that will navigate to the desired hotel screen and verify whether the price per night matches the assertion given in the test.
    """
    @pytest.mark.regression
    @pytest.mark.happy_path
    def test_happy_path(self, appium_driver):
        sign_page = SignInScreen(self.driver)
        welcome_page = WelcomePage(self.driver)
        welcome_page.click_on_continue_with_email().fill_email(data=get_data('happy_path_data')[0][0])
        sign_page.click_to_continue()
        sign_page.click_to_continue()
        sign_page.click_on_permission_deny()
        sign_page.click_on_travellers_type()
        sign_page.click_on_family()
        sign_page.click_on_desired_hotel()
        sign_page.verify_per_night_price()





