import requests
from requests.models import Response

_HOST_ = "https://api.frankfurter.app"
_CURRENCIES_ = "/currencies"
_LATEST_ = "/latest"


def call_api(url: str) -> requests.models.Response:
    """
    Function that will call the specified API endpoint and return the response

    Parameters
    ----------
    url : str
        URL of the API endpoint to be called

    Pseudo-code
    ----------
    in try create variable which stores response of get requests and return it
    if exception occure return "None"

    Returns
    -------
    requests.models.Response
        Response from API request
    """
    # => code
    try:
        response = requests.get(url)

        return response

    except:
        return None


def format_currencies_url() -> str:
    """
    Function that will format the URL to the currency endpoint

    Parameters
    ----------
    None

    Pseudo-code
    ----------
    return formated string using currency endpoint

    Returns
    -------
    str
        Formatted URL to the currency endpoint
    """
    # => To be filled by student

    return _HOST_ + _CURRENCIES_


def get_currencies():
    """
    Function that will extract the currency codes available from the Frankfurter app as a list

    Parameters
    ----------
    None

    Pseudo-code
    ----------
    create foramt currency url using format_currencies_url()
    store it in to variable and use call_api() for that variable
    convert return of call_api() into list which gives list of all available currencies

    Returns
    -------
    list
        Currency codes available from the Frankfurter app
    """
    # => code
    formated_currency_url = format_currencies_url()
    response = call_api(formated_currency_url)
    # response = requests.get(currency_url)

    return list(response.json().keys())


def format_latest_url(from_currency: str, to_currency: str) -> str:
    """
    Function that will format the URL to the latest endpoint

    Parameters
    ----------
    from_currency : str
        Currency code to be converted fromimport re
    to_currency : str
        Currency code to be converted to

    Pseudo-code
    ----------
    return formated string with "latest endpoint + "?from=" + currency to convert from + "&to=" +  currency to convert in"

    Returns
    -------
    str
        Formatted URL to the latest endpoint
    """
    # => code

    return _HOST_ + _LATEST_ + "?from=" + from_currency + "&to=" + to_currency
