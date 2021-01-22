import re

reddit_watch_new = '(<@)\\w+(>) reddit watch new \\w+'
reddit_watch_hot = '(<@)\\w+(>) reddit watch hot \\w+'
reddit_unwatch_new = '(<@)\\w+(>) reddit unwatch new \\w+'
reddit_unwatch_hot = '(<@)\\w+(>) reddit unwatch hot \\w+'

reddit_patterns = [reddit_watch_new, reddit_watch_hot, reddit_unwatch_new, reddit_unwatch_hot]

currency = '(<@)\\w+(>) currency \\w+ \\w+ [0-9][0-9]*(.([1-9]{0,2}))?'

supported_currencies = ['CAD', 'HKD', 'ISK', 'PHP', 'DKK', 'HUF', 'CZK', 'AUD', 'RON', 'SEK', 'IDR', 'INR', 'BRL',
                        'RUB', 'HRK', 'JPY', 'THB', 'CHF', 'SGD', 'PLN', 'BGN', 'TRY', 'CNY', 'NOK', 'NZD', 'ZAR',
                        'USD', 'MXN', 'ILS', 'GBP', 'KRW', 'MYR']


def is_reddit_request(message):
    for pattern in reddit_patterns:
        if re.match(pattern, message):
            return True
    return False


def is_currency_request(message):
    if re.match(currency, message):
        return True
    return False
