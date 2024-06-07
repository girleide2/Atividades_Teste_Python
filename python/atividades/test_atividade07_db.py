import pytest
from unittest.mock import MagicMock
from atividade07_db import User, UserService

def test_save_user_with_valid_user():
    db_mock = MagicMock()
    user_service = UserService(db_mock)
    user = User("Fulano", "fulanodetal@email.com")

    user_service.save_user(user)

    db_mock.save_user.assert_called_once_with(user)

def test_save_user_with_empty_name():
    db_mock = MagicMock()
    user_service = UserService(db_mock)
    user = User("", "fulanodetal@email.com")

    with pytest.raises(ValueError, match="User must have a name and email"):
        user_service.save_user(user)

def test_save_user_with_empty_email():
    db_mock = MagicMock()
    user_service = UserService(db_mock)
    user = User("Fulano", "")

    with pytest.raises(ValueError, match="User must have a name and email"):
        user_service.save_user(user)

def test_save_user_with_invalid_user():
    db_mock = MagicMock()
    user_service = UserService(db_mock)
    user = User(None, None)

    with pytest.raises(ValueError, match="User must have a name and email"):
        user_service.save_user(user)

if __name__ == "__main__":
    pytest.main(["-s","-x","test_atividade07_db.py","-vv"])
