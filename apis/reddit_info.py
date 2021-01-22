import praw
from apis import keys
from log.mylogger import get_logger

reddit = praw.Reddit(
    client_id=keys.REDDIT_CLIENT_ID,
    client_secret=keys.REDDIT_CLIENT_SECRET,
    user_agent=keys.REDDIT_USER_AGENT,
    username=keys.REDDIT_USERNAME,
    password=keys.REDDIT_PASSWORD
)


def get_post_from_subreddit(subreddit, post='new'):
    get_logger().info(f'Getting data from reddit API. Subreddit: {subreddit}. Post type: {post}')
    sub = reddit.subreddit(subreddit)
    if post == 'new':
        new_post = sub.new(limit=1)
    else:
        new_post = sub.hot(limit=1)
    for post in new_post:
        return post.title, post.url
