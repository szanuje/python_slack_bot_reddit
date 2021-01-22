import slack

import apis.keys

my_token = apis.keys.SLACK_TOKEN

rtmclient = slack.RTMClient(token=my_token)
webclient = slack.WebClient(my_token)


def get_rtm_client():
    return rtmclient


def get_web_client():
    return webclient
