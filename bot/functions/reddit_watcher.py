import threading
import time

import apis.reddit_info
from apis.keys import REDDIT_POST_CHECK_INTERVAL_SECONDS
from bot.functions.reddit_notification_data import notification_data
from bot.post_a_message import post
from log.mylogger import get_logger


def handle_reddit(message, channel_id):
    split = message.split()
    function = split[2]
    post_type = split[3]
    subreddit = split[4]
    if function == 'watch':
        watch_subreddit(subreddit, post_type, channel_id)
    if function == 'unwatch':
        unwatch_subreddit(subreddit, post_type, channel_id)


def watch_subreddit(subreddit, post_type, channel_id):
    sub_exists = False
    for sub in notification_data[post_type]['subreddits']:
        if sub['name'] == subreddit:
            sub_exists = True
            if channel_id not in sub['channels']:
                sub['channels'].append(channel_id)
    if not sub_exists:
        notification_data[post_type]['subreddits'].append(
            {
                'name': subreddit,
                'last_post': {
                    'content': '',
                    'url': ''
                },
                'channels': [
                    channel_id
                ]
            }
        )
    post(channel_id, f'Successfully subscribed to "{subreddit}" subreddit')


def unwatch_subreddit(subreddit, post_type, channel_id):
    for sub in notification_data[post_type]['subreddits']:
        if sub['name'] == subreddit and channel_id in sub['channels']:
            sub['channels'].remove(channel_id)
    post(channel_id, f'Successfully unsubscribed "{subreddit}" subreddit')


def run_notification_service(webclient):
    while True:
        for post_type in notification_data:
            for subreddit in notification_data[post_type]['subreddits']:
                sub_name = subreddit['name']
                for channel in subreddit['channels']:
                    latest_post = apis.reddit_info.get_post_from_subreddit(sub_name, post_type)
                    if not latest_post[0] == subreddit['last_post']['content']:
                        sub_name_response = f'*{sub_name}*'
                        post_type_response = f'*{post_type}*'
                        emote = ':warning:'
                        if post_type == 'hot':
                            emote = ':fire:'
                        response = f'{emote}[{post_type_response}][{sub_name_response}]{emote}' \
                                   f'New post --> {latest_post[0]} \n' \
                                   f'Link: {latest_post[1]}'
                        post(channel, response)
                        subreddit['last_post']['content'] = latest_post[0]
                        subreddit['last_post']['url'] = latest_post[1]
                        get_logger().info(f'Notification data changed. {notification_data}')
                    else:
                        get_logger().info(f'Post already logged on channel {channel}. Content: {latest_post[0]}')
        time.sleep(REDDIT_POST_CHECK_INTERVAL_SECONDS)


def start_notifier(webclient):
    my_thread = threading.Thread(target=run_notification_service, args={webclient})
    my_thread.start()
