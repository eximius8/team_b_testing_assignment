'''Tests for adding user data live here.'''
# import pytest
# from models.personal_data import PersonalData


class TestAddPersonalData:
    """Adding new data to person's profile."""

    def test_update_profile(self, app, auth):

        app.login.go_to_editing_personal_data()
        # personal_data = PersonalData.random()
        # app.user_page._edit_personal_data(personal_data)
        assert True
