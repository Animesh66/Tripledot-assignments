from Pages.BasePage import BasePage
from Pages.SignInPage import SignInScreen


class WelcomePage(BasePage):
    """
    This is the inital Sign In page which is opened when user opens the app for the first time.
    All the method written here are strictly present in Welcome page only.
    """

    def __init__(self, driver):
        super().__init__(driver)

    def click_on_continue_with_email(self):
        self.click("continue_with_email_id")
        return SignInScreen(self.driver)