'''Locators for edit profile page live here.'''
from selenium.webdriver.common.by import By


class EditProfileLocators:
    """Locators Profile page."""

    FIRSTNAME_INPUT = (By.ID, "id_firstname")
    LASTNAME_INPUT = (By.ID, "id_lastname")
    TIMEZONE_INPUT = (By.ID, "id_timezone")
    CITY_INPUT = (By.ID, "id_city")
    COUNTRY_INPUT = (By.ID, "id_country")
    SAVE_PROFILE_BTN = (By.ID, "id_submitbutton")
    EDIT_INFO = (By.CSS_SELECTOR, "a[href*='user/edit.php']")
    BASIC_DATA = (By.ID, "id_moodle")
    EMAIL_INPUT = (By.ID, "id_email")
    MOODLE_NET_PROFILE = (By.ID, "id_moodlenetprofile")
