import pytest
from unittest.mock import MagicMock
from atividade14_email_service import EmailService, EventHandler

def test_handle_event_sends_email():
    
    mock_email_service = MagicMock(spec=EmailService)
    event_handler = EventHandler(mock_email_service)
    test_event = {"type": "TEST_EVENT", "details": "This is a test event"}
    event_handler.handle_event(test_event)
    mock_email_service.send_email.assert_called_once_with(
        'test@example.com', 
        'Event Occurred', 
        str(test_event)
    )

def test_handle_event_with_different_event():

    mock_email_service = MagicMock(spec=EmailService)
    event_handler = EventHandler(mock_email_service)
    different_event = {"type": "ANOTHER_EVENT", "details": "This is another event"}
    event_handler.handle_event(different_event)
    mock_email_service.send_email.assert_called_once_with(
        'test@example.com', 
        'Event Occurred', 
        str(different_event)
    )

if __name__ == "__main__":
    pytest.main(["-s","-x","test_atividade14_email_service.py","-vv"])
