'''Locators for login page live here.'''
from selenium.webdriver.common.by import By


class AuthLocators:
    '''Локаторы для страницы входа.'''
    LOGIN_ERROR_MESSAGE = (By.ID, "loginerrormessage")
    RECENT_COURSES = (By.ID, "instance-189-header")
    USERNAME = (By.ID, "username")
    PASSWORD = (By.ID, "password")
    LOGIN_BTN = (By.ID, "loginbtn")
