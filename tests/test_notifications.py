import unittest
from unittest.mock import patch, MagicMock

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
    def test_init_thread(self, mock_post):
        self.notification.init_thread("content", {})
        mock_post.assert_called_with(
            "",
            data='{"text": "content"}',
            headers={"Content-Type": "application/json; charset=UTF-8"},
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
