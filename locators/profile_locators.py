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
