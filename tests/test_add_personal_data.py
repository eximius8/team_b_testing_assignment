"""Tests for adding user data live here."""
import pytest

from models.personal_data import PersonalData


class TestAddPersonalData:
    """Adding new data to person's profile."""

    def test_update_profile(self, app, auth):
        """Тест на изменения данных пользователя - данные валидные.
        Steps
        1. Перейти в страницу ввода данных.
        2. Сгенерировать случайные данные.
        3. Заполнить поля с данными.
        4. Проверить наличие окна, что данные успешно изменены."""

        app.login.go_to_editing_personal_data()
        personal_data = PersonalData.random()
        app.user_page._edit_personal_data(personal_data)
        assert app.user_page.has_data_changed_alert(), "Данные не изменены"

    @pytest.mark.parametrize("param", ["last_name", "name"])
    def test_edit_basic_personal_data_with_incorrect_email(self, app, auth, param):
        """Тест на изменения данных пользователя - данные невалидные.
        Steps
        1. Перейти в страницу ввода данных.
        2. Сгенерировать случайные данные.
        3. Добавить невалидные данные.
        4. Проверить отсутсвие окна, что данные успешно изменены.
        """

        app.login.go_to_editing_personal_data()
        personal_data = PersonalData.random()
        setattr(personal_data, param, "")
        app.user_page._edit_personal_data(personal_data)
        assert not app.user_page.has_data_changed_alert(), "Данные были изменены!"
