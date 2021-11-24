import unittest
from unittest.mock import patch, MagicMock, call

from lifeguard_notification_google_chat.notifications import GoogleNotificationBase

MOCK_LOGGER = MagicMock(name="logger")


class GoogleNotificationBaseTest(unittest.TestCase):
    def setUp(self):
        self.notification = GoogleNotificationBase()

    @patch("lifeguard_notification_google_chat.notifications.post")
    @patch("lifeguard_notification_google_chat.notifications.logger", MOCK_LOGGER)
    def test_send_single_message(self, mock_post):
        self.notification.send_single_message("content", {})
        mock_post.assert_called_with(
            "",
            data='{"text": "content"}',
            headers={"Content-Type": "application/json; charset=UTF-8"},
        )

    @patch("lifeguard_notification_google_chat.notifications.post")
    @patch("lifeguard_notification_google_chat.notifications.logger", MOCK_LOGGER)
    def test_send_multiple_single_message(self, mock_post):
        json_response = MagicMock(name="json")
        json_response.json.return_value = {"thread": "thread"}
        mock_post.return_value = json_response

        self.notification.send_single_message(["line1", "line2"], {})

        mock_post.assert_has_calls(
            [
                call(
                    "",
                    data='{"text": "line1"}',
                    headers={"Content-Type": "application/json; charset=UTF-8"},
                ),
                call(
                    "",
                    data='{"text": "line2", "thread": "thread"}',
                    headers={"Content-Type": "application/json; charset=UTF-8"},
                ),
            ]
        )

    @patch("lifeguard_notification_google_chat.notifications.post")
    @patch("lifeguard_notification_google_chat.notifications.logger", MOCK_LOGGER)
    def test_init_thread(self, mock_post):
        self.notification.init_thread("content", {})
        mock_post.assert_called_with(
            "",
            data='{"text": "content"}',
            headers={"Content-Type": "application/json; charset=UTF-8"},
        )

    @patch("lifeguard_notification_google_chat.notifications.post")
    @patch("lifeguard_notification_google_chat.notifications.logger", MOCK_LOGGER)
    def test_init_thread_with_multiples_messages(self, mock_post):
        json_response = MagicMock(name="json")
        json_response.json.return_value = {"thread": "thread"}
        mock_post.return_value = json_response

        self.notification.init_thread(["line1", "line2"], {})

        mock_post.assert_has_calls(
            [
                call(
                    "",
                    data='{"text": "line1"}',
                    headers={"Content-Type": "application/json; charset=UTF-8"},
                ),
                call(
                    "",
                    data='{"text": "line2", "thread": "thread"}',
                    headers={"Content-Type": "application/json; charset=UTF-8"},
                ),
            ]
        )

    @patch("lifeguard_notification_google_chat.notifications.post")
    @patch("lifeguard_notification_google_chat.notifications.logger", MOCK_LOGGER)
    def test_update_thread(self, mock_post):
        self.notification.update_thread("content", "thread", {})
        mock_post.assert_called_with(
            "",
            data='{"text": "thread", "thread": "content"}',
            headers={"Content-Type": "application/json; charset=UTF-8"},
        )

    @patch("lifeguard_notification_google_chat.notifications.post")
    @patch("lifeguard_notification_google_chat.notifications.logger", MOCK_LOGGER)
    def test_close_thread(self, mock_post):
        self.notification.close_thread("content", "thread", {})
        mock_post.assert_called_with(
            "",
            data='{"text": "thread", "thread": "content"}',
            headers={"Content-Type": "application/json; charset=UTF-8"},
        )
