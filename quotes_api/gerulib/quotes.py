import requests
from http import HTTPStatus

url = 'https://1c22eh3aj8.execute-api.us-east-1.amazonaws.com/challenge/quotes'


def validade_response(resp):
    if resp.status_code == HTTPStatus.OK:
        return resp.json()
    raise ValueError('Oops!  That was no valid number.  Try again...')


def get_quotes():
    try:
        response = requests.get(url, timeout=5)
        quotes = validade_response(response)
        response.raise_for_status()
    except requests.exceptions.HTTPError as e:
        return f'Http Error: {str(e)}'
    except requests.Timeout as et:
        return f'Timeout Error: {str(et)}'

    return quotes


def get_quote(quote_number):
    try:
        response = requests.get(f'{url}/{quote_number}', timeout=5)
        quote = validade_response(response)
        response.raise_for_status()
    except requests.exceptions.HTTPError as e:
        return f'Http Error: {str(e)}'
    except requests.Timeout as et:
        return f'Timeout Error: {str(et)}'

    return quote
