from exchangeratesapi import Api

api = Api()


def exchange(currency_from, currency_to, quantity):
    actual_from = currency_from.upper()
    actual_to = currency_to.upper()
    if api.is_currency_supported(actual_from) and api.is_currency_supported(actual_to):
        quantity = float(quantity)
        return str(api.get_rate(actual_from, actual_to) * float(quantity))
    else:
        raise ValueError
