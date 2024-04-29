# currency_parser.py
from forex_python.converter import CurrencyRates

def get_currency_rates():
    currency_rates = CurrencyRates()
    usd_to_eur = currency_rates.get_rate('USD', 'EUR')
    eur_to_usd = currency_rates.get_rate('EUR', 'USD')
    return {'USD_to_EUR': usd_to_eur, 'EUR_to_USD': eur_to_usd}
