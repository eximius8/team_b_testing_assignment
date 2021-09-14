"""Page for user profile lives here."""
from locators.profile_locators import EditProfileLocators
from pages.base_page import BasePage


class UserPage(BasePage):
    """Check and update user profile page."""

    def input_firstname(self):
        """Ввод имени."""
        return self.find_element(EditProfileLocators.FIRSTNAME_INPUT)
