import sys
from api import call_api, format_latest_url
from currency import Currency, check_valid_currency, extract_api_result


def main():
    """
    Function that will check if there are enough input arguments provided.
    If so it will return the formatted result from the Frankfurter app.
    If not it will return an error message

    Parameters
    ----------
    None

    Pseudo-code
    ----------
    takes input using sys.argv[]
    if length is < 3 then returns error message
    else using get_rate() gives results for currencies

    Returns
    -------
    str
        Formatted API result or error message
    """
    # => code``
    if len(sys.argv) < 3:
        rate = "You haven't provided 2 currency codes"
    else:
        rate = get_rate(sys.argv[1], sys.argv[2])

    print(rate)
    return rate


def get_rate(from_currency: str, to_currency: str):
    """
    Function that will check if provided currency codes are valid otherwise it will return error message.
    If both are valid, it will format the API url, make a request to it and format the result

    Parameters
    ----------
    from_currency : str
        Currency code to be converted from
    to_currency : str
        Currency code to be converted to

    Pseudo-code
    ----------
    if any currency is not valid then return error message
    if both currencies are valid then create latest url
    and use call api function for the same url and store it in a variable response_call
    if response call is None than return error message for APi
    else store json of response call and use it to extract api result using  extract_api_result()
    and then convert extracted result to formated result using Currency.format_result()

    Returns
    -------
    str
        Formatted API result or error message
    """
    # => code

    if check_valid_currency(
            from_currency) == True & check_valid_currency(to_currency) == True:
        latest_url = format_latest_url(from_currency, to_currency)
        # print(latest_url)
        response_call = call_api(latest_url)
        if response_call == None:
            return "There is an error with API callr"
        # print(response_call.json())
        else:
            response_call = response_call.json()
            api_result = extract_api_result(response_call)
            # print(type(try1))
            format_result = Currency.format_result(api_result)
            return format_result
    if check_valid_currency(from_currency) == False:
        return f"{from_currency} is not vaild"
    if check_valid_currency(to_currency) == False:
        return f"{to_currency} is not vaild"


if __name__ == "__main__":
    main()
