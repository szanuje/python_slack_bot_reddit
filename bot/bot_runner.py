from slack import RTMClient

import bot.client.client as client
import bot.functions.reddit_watcher as reddit_watcher
from bot.functions.currency_converter import handle_currency
from bot.functions.reddit_watcher import handle_reddit
from bot.handler.message_patterns import is_reddit_request, is_currency_request
from bot.post_a_message import post
from log.mylogger import get_logger

my_client = client.get_web_client()
auth_data = my_client.auth_test()
get_logger().info(f'AUTH INFO: {auth_data}')

bot_user_id = auth_data['user_id']
kekw = '<https://media4.giphy.com/media/6uSP9U0UwKc5a/giphy.gif?cid" \
                   "=920975b58xnwbha236ams6salfa1fpqr7i0lkwqbb5enrktv&rid=giphy.gif|XD> '


@RTMClient.run_on(event="message")
def handle_message(data, **kwargs):
    if 'bot_id' not in data:
        channel_id = data['channel']
        get_logger().info(f'Incoming Message. Channel: {channel_id}. Content: {data}')
        if bot_user_id in data['text']:
            # thread_ts = data['ts']
            user = data['user']
            message = data['text']
            if is_reddit_request(message):
                handle_reddit(message, channel_id)
                return
            if is_currency_request(message):
                handle_currency(message, channel_id)
                return

            response = f'Hi <@{user}> {kekw}'
            post(channel_id, response)


reddit_watcher.start_notifier(my_client)
# client.get_rtm_client().on(handler.handle_message, event='message')
client.get_rtm_client().start()
