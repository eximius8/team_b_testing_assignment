"""Page for user profile lives here."""
from locators.profile_locators import EditProfileLocators
from pages.base_page import BasePage


class UserPage(BasePage):
    """Check and update user profile page."""

    def input_firstname(self):
        """Ввод имени."""
        return self.find_element(EditProfileLocators.FIRSTNAME_INPUT)

    def input_lastname(self):
        """Ввод фамилии."""
        return self.find_element(EditProfileLocators.LASTNAME_INPUT)

    def input_email(self):
        """Ввод фамилии."""
        return self.find_element(EditProfileLocators.EMAIL_INPUT)

    def select_timezone(self):
        """Выбор часового пояса."""
        return self.find_element(EditProfileLocators.TIMEZONE_INPUT)

    def input_city(self):
        """Ввод города."""
        return self.find_element(EditProfileLocators.CITY_INPUT)

    def select_country(self):
        """Выбор страны."""
        return self.find_element(EditProfileLocators.COUNTRY_INPUT)

    def btn_save_profile(self):
        """Кнопка сохрнить профиль."""
        return self.find_element(EditProfileLocators.SAVE_PROFILE_BTN)

    def input_info(self):
        """Ввод общей информации."""
        return self.find_element(EditProfileLocators.EDIT_INFO)

    def input_basic_data(self):
        """Ввод общей информации."""
        return self.find_element(EditProfileLocators.BASIC_DATA)

    def input_moodle_net_profile(self):
        """Ввод информации."""
        return self.find_element(EditProfileLocators.MOODLE_NET_PROFILE)

    def submit_button(self):
        """Сохранить профиль."""
        return self.find_element(EditProfileLocators.SAVE_PROFILE_BTN)

    def has_data_changed_alert(self):
        """Сообщение что данные изменены"""
        return len(self.find_elements(EditProfileLocators.DATA_CHANGED_ALERT)) != 0

    def _input_name(self, firstname):
        self.fill_element(self.input_firstname(), firstname)

    def _input_lastname(self, lastname):
        self.fill_element(self.input_lastname(), lastname)

    def _input_email(self, email):
        self.fill_element(self.input_email(), email)

    def _input_city(self, city):
        self.fill_element(self.input_city(), city)

    def _select_country(self, value):
        self.select_value(self.select_country(), value)

    def _select_timezone(self, value):
        self.select_value(self.select_timezone(), value)

    def _input_about(self, text):
        self.fill_element(self.input_info(), text)

    def _save_profile_data(self):
        self.click_element(self.submit_button())

    def _edit_personal_data(self, data):

        self._input_name(data.name)
        self._input_lastname(data.last_name)
        self._input_city(data.city)
        self._save_profile_data()
