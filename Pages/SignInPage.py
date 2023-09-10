import re
import time
from Pages.BasePage import BasePage
from Utilities.data_provider import get_data


class SignInScreen(BasePage):
    """
    This is theSign In page which is opened when user provided the email of his and click on confinue button.
    All the method written here are strictly present in Sign In page only.
    """
    def __init__(self, driver):
        super().__init__(driver)

    def fill_email(self, data):
        self.type("email_text_box_class", data=data)

    def click_to_continue(self):
        self.click("continue_button_id")
        time.sleep(3)

    def clik_on_title(self):
        self.click("title_id")

    def fill_password(self, data):
        self.type("android.widget.EditText", data=data)

    def verify_error_message(self):
        error_message = self.get_text("invalid_password_text_id")
        assert error_message == re.compile("Incorrect password", re.IGNORECASE), \
            "Error message did not match with expected error message."

    def click_on_permission_deny(self):
        self.click("deny_notification_id")

    def click_on_travellers_type(self):
        self.click("type_of_travellers_uiautomator")

    def click_on_family(self):
        self.click("family_uiautomator")

    def click_on_desired_hotel(self):
        self.click("selected_hotel_uiautomator")

    def verify_per_night_price(self):
        per_night_charge = self.get_text("per_night_charge_id")
        assert str(154) in per_night_charge