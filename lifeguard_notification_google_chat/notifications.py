"""
Base of notification system
"""
import json

from lifeguard.http_client import post
from lifeguard.logger import lifeguard_logger as logger
from lifeguard.notifications import NotificationBase

from lifeguard_notification_google_chat.settings import \
    GOOGLE_DEFAULT_CHAT_ROOM


class GoogleNotificationBase(NotificationBase):
    """
    Base of notification
    """

    def send_single_message(self, content, _settings):
        logger.info("seding single message to google chat")
        headers = {"Content-Type": "application/json; charset=UTF-8"}
        data = {
                "text": content
            }
        post(GOOGLE_DEFAULT_CHAT_ROOM, data=json.dumps(data), headers=headers)
