import unittest
from api import call_api, format_currencies_url, get_currencies, format_latest_url, _HOST_, _LATEST_, _CURRENCIES_


class TestFormatUrl(unittest.TestCase):
    def test_format_latest_url(self):
        # => code
        actual_url = _HOST_ + _LATEST_ + "?from=USD&to=INR"
        from_currency = "USD"
        to_currency = "INR"
        output_url = format_latest_url(from_currency, to_currency)
        self.assertEqual(actual_url, output_url)

    def test_format_currencies_url(self):
        # => code
        actual_url = _HOST_ + _CURRENCIES_
        output_url = format_currencies_url()
        self.assertEqual(actual_url, output_url)


class TestAPI(unittest.TestCase):
    def test_get_currencies(self):
        # => code
        actual_list = [
            "AUD",
            "BGN",
            "BRL",
            "CAD",
            "CHF",
            "CNY",
            "CZK",
            "DKK",
            "EUR",
            "GBP",
            "HKD",
            "HRK",
            "HUF",
            "IDR",
            "ILS",
            "INR",
            "ISK",
            "JPY",
            "KRW",
            "MXN",
            "MYR",
            "NOK",
            "NZD",
            "PHP",
            "PLN",
            "RON",
            "RUB",
            "SEK",
            "SGD",
            "THB",
            "TRY",
            "USD",
            "ZAR",
        ]
        output_list = get_currencies()
        self.assertEqual(actual_list, output_list)

    def test_call_api(self):
        actual_status = 200
        output_status = call_api(_HOST_ + _CURRENCIES_).status_code
        self.assertEqual(actual_status, output_status)


if __name__ == "__main__":
    unittest.main()
