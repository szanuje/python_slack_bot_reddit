from log.mylogger import get_logger
from bot.client.client import get_web_client


def post(channel, message):
    get_logger().info(f'Posting message: Channel: {channel}. Message: {message}.')
    get_web_client().chat_postMessage(
        as_user="true",
        channel=channel,
        text=message
    )
