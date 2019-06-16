import random

from pyramid.view import view_config

import gerulib


@view_config(route_name='home', renderer='../templates/home.jinja2')
def home(request):
    return dict(project='Desafio Web 1.0')


@view_config(route_name='quotes', renderer='../templates/quotes.jinja2')
def get_quotes(request):
    response = gerulib.get_quotes()
    return dict(quotes=response.get('quotes'))


@view_config(route_name='quote', renderer='../templates/quote.jinja2')
def get_quote(request):
    response = gerulib.get_quote(request.matchdict.get('quote_number'))
    return dict(quote_number=request.matchdict.get('quote_number'), quote=response.get('quote'))


@view_config(route_name='random_quote', renderer='../templates/random_quote.jinja2')
def get_random_quote(request):
    quotes = gerulib.get_quotes().get('quotes')
    quotes_len = len(quotes)
    random_quote = random.randint(0, quotes_len - 1)
    response = gerulib.get_quote(random_quote)
    return dict(quote_number=random_quote, quote=response.get('quote'))
