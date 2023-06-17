import unittest
from currency import check_valid_currency, extract_api_result, Currency


class TestValidCurrency(unittest.TestCase):
    def test_check_valid_currency(self):
        # => code
        actual_currency = True
        output_currency = check_valid_currency("INR")
        self.assertEqual(actual_currency, output_currency)


class TestExtractApi(unittest.TestCase):
    def test_extract_api_result(self):
        # => code
        actual_json = {"amount": 1.0, "base": "EUR", "date": "2021-08-26", "rates": {"INR": 87.23}}
        currency = Currency()
        currency.from_currency = "EUR"
        currency.to_currency = "INR"
        currency.amount = 1.0
        currency.rate = 87.23
        currency.reverse_rate()
        currency.date = "2021-08-26"
        output_value = extract_api_result(actual_json)
        self.assertEqual(currency, output_value)
