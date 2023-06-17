from dataclasses import dataclass
from api import get_currencies

CURRENCIES = get_currencies()


def check_valid_currency(currency: str) -> bool:
    """
    Function that will check currency code is amongst the list of available currencies

    Parameters
    ----------
    currency : str
        Currency code to be checked

    Pseudo-code
    ----------
    function will take currency as parameter
    and check if that is avaialbe in CURRENCIES or not
    if it is true then return True else return False

    Returns
    -------
    bool
        True if the currency code is valid otherwise False
    """

    # => code
    if currency in CURRENCIES:
        return True
    else:
        return False


@dataclass
class Currency:
    """
    Class that represents a Currency conversion object.

    Attributes
    ----------
    from_currency : str
        Code for the origin currency
    to_currency : str
        Code for the destination currency
    amount : float
        The amount (in origin currency) to be converted
    rate : float
        The conversion rate to be applied on the origin amount (origin -> destination)
    inverse_rate : float
        The inverse of the previous rate  (destination -> origin)
    date : str
        Date when the conversion rate was recorded
    """

    from_currency: str = None
    to_currency: str = None
    amount: float = 0
    rate: float = 0
    inverse_rate: float = 0
    date: str = None

    def reverse_rate(self):
        """
        Method that will calculate the inverse rate, round it to 5 decimal places and save it in the attribute inverse_rate

        Parameters
        ----------
        None

        Pseudo-code
        ----------
        create self variable call inverse rate wich is equal to 1/rate

        Returns
        -------
        None
        """
        # => code
        self.inverse_rate = 1 / self.rate

    def format_result(self):
        """
        Methods returning the formatted successful message

        Parameters
        ----------
        None

        Pseudo-code
        ----------
        create variaable which store string with date and conversion rates

        Returns
        -------
        str
            Formatted successful message
        """
        # => code
        result = f"Today's ({self.date}) conversion rate from {self.from_currency} to {self.to_currency} is {self.rate}. The inverse rate is {self.inverse_rate}"

        return result


def extract_api_result(result: dict) -> Currency:
    """
    Function that will extract the relevant fields from API result, instantiate a Currency class accordingly and
    calculate the inverse rate

    Parameters
    ----------
    result : dict
        Results of the API converted as dictionary

    Pseudo-code
    ----------
    create object of Currency class
    assign value from result
        from_currency as result["base"]
        to_currency as list of results["rates"]
        amount as result["amount"]
        rate as list of result["rates"]
        date as resulr["date] and call function reverse_rate()

    Returns
    -------
    Currency
        Instantiated Currency
    """
    # => code
    currency = Currency()
    currency.from_currency = result["base"]
    currency.to_currency = list(result["rates"].keys())[0]
    currency.amount = result["amount"]
    currency.rate = list(result["rates"].values())[0]
    currency.reverse_rate()
    currency.date = result["date"]
    return currency
