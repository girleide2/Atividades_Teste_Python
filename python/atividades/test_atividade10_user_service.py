import pytest
from unittest.mock import MagicMock
from atividade10_user_service import User, UserService, UserManager

def test_fetch_user_info_success():
    mock_user_service = MagicMock(spec=UserService)
    mock_user = User(user_id=1, name="John Doe")
    mock_user_service.get_user_info.return_value = mock_user
    user_manager = UserManager(mock_user_service)
    result = user_manager.fetch_user_info(1)
    mock_user_service.get_user_info.assert_called_once_with(1)
    assert result == mock_user

def test_fetch_user_info_user_not_found():

    mock_user_service = MagicMock(spec=UserService)
    mock_user_service.get_user_info.return_value = None
    user_manager = UserManager(mock_user_service)
    with pytest.raises(ValueError, match="User not found"):
        user_manager.fetch_user_info(1)
    mock_user_service.get_user_info.assert_called_once_with(1)

if __name__ == "__main__":
    pytest.main(["-s","-x","test_atividade10_user_service.py","-vv"])
