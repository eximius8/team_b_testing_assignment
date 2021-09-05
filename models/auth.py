"""Auxilary auth model to store auth data."""
from faker import Faker

fake = Faker("Ru-ru")


class AuthData:
    """Auth data lives here."""

    def __init__(self, username=None, password=None):
        self.username = username
        self.password = password

    @staticmethod
    def random():
        """Create random auth data."""

        username = fake.email()
        password = fake.password()
        return AuthData(username, password)
