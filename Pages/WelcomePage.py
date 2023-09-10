from Pages.BasePage import BasePage
from Pages.SignInPage import SignInScreen


class WelcomePage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    def click_on_continue_with_email(self):
        self.click("continue_with_email_id")
        return SignInScreen(self.driver)