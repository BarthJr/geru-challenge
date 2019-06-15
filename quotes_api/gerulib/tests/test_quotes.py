from gerulib import get_quotes, get_quote


def test_get_quotes_should_be_instance_of_dict():
    assert isinstance(get_quotes(), dict)


def test_if_quotes_values_is_a_instance_of_list():
    assert isinstance(get_quotes().get('quotes'), list)


def test_get_quote_should_be_instance_of_dict():
    assert isinstance(get_quote(2), dict)


def test_if_quote_value_is_a_instance_of_str():
    assert isinstance(get_quote(2).get('quote'), str)


def test_get_quotes_should_return_dict_of_list():
    expected = {'quotes': ['Beautiful is better than ugly.', 'Explicit is better than implicit.',
                           'Simple is better than complex.', 'Complex is better than complicated.',
                           'Flat is better than nested.', 'Sparse is better than dense.', 'Readability counts.',
                           "Special cases aren't special enough to break the rules.",
                           'Although practicality beats purity.',
                           'Errors should never pass silently.', 'Unless explicitly silenced.',
                           'In the face of ambiguity, refuse the temptation to guess.',
                           'There should be one-- and preferably only one --obvious way to do it.',
                           "Although that way may not be obvious at first unless you're Dutch.",
                           'Now is better than never.',
                           'Although never is often better than *right* now.',
                           "If the implementation is hard to explain, it's a bad idea.",
                           'If the implementation is easy to explain, it may be a good idea.',
                           "Namespaces are one honking great idea -- let's do more of those!"
                           ]
                }
    assert expected == get_quotes()


def test_get_quote_should_return_quote():
    expected = {'quote': 'Simple is better than complex.'}
    assert expected == get_quote(2)
