import apis.exchange_info as exchange
from bot.handler.message_patterns import supported_currencies
from bot.post_a_message import post


def handle_currency(message, channel_id):
    split = message.split()
    from_cur = split[2]
    to_cur = split[3]
    quantity = split[4]
    try:
        result = exchange.exchange(from_cur, to_cur, quantity)
        message = f'{quantity} {from_cur} = {result} {to_cur}'
        post(channel_id, message)
    except ValueError:
        message = f'Cannot calculate exchange rate. Pattern: ' \
                  '"[@bot_name] currency [CURRENCY-FROM] [CURRENCY-TO] [QUANTITY]" \n' \
                  f'Supported currencies: {supported_currencies} \n' \
                  f'Quantity format examples: 0.10, 1.1, 100.22, 420.69'
        post(channel_id, message)
