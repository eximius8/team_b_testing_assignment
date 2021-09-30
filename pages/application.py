"""Abstraction of user working with different pages."""
from pages.create_course_page import CreateCoursePage
from pages.login_page import LoginPage
from pages.user_page import UserPage


class Application:
    """Main application class."""

    def __init__(self, driver, url):
        self.driver = driver
        self.url = url
        self.login = LoginPage(self)
        self.user_page = UserPage(self)
        self.create_course = CreateCoursePage(self)

    def quit(self):
        self.driver.quit()

    def open_auth_page(self):
        self.driver.get(self.url + "/login/index.php")

    def open_create_course_page(self):
        self.driver.get(self.url + "/course/edit.php")
