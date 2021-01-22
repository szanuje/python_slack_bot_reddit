# Slack bot for Reddit notifications

1. Configure your slack bot and get token.
https://api.slack.com/bot-users#creating-bot-user
2. Configure reddit app: https://www.reddit.com/prefs/apps ("create another app")
3. Paste token and user data in apis.keys package of this project

# Usage

1. (un)Subscribe subreddit:  
`@bot_name reddit watch [new|hot] [subredddit-name]`  
`@bot_name reddit unwatch [new|hot] [subredddit-name]`  
Example: @my_bot reddit watch hot wtf

2. BONUS: Currency Exchange  
`@bot_name currency [CURRENCY-FROM] [CURRENCY-TO] [QUANTITY]`  
Example: @my_bot currency USD PLN 420.69