""" Based on the pipeline.py we can create a higher order function to create an abstraction and bring the
data conversion to higher level. There is a lot going on with the chained functions. It's well done but not very
readable. Here it is only matter of taste if we should try to get more close to pure functional programming or just
stay in a more readable level by defining named functions as in pipeline.py
"""

from functools import reduce


def change(_d: 'dict', key: 'str', value: 'str') -> dict:
    dict_copy = _d.copy()
    dict_copy[key] = value
    return dict_copy


def without(d, key):
    new_d = d.copy()
    new_d.pop(key)
    return new_d


def pipeline(data: 'list', functions: 'list') -> map:
    return reduce(lambda a, x: map(x, a), functions, data)


def action(fn, key):
    return lambda _dict: change(_dict, key, fn(_dict.get(key)))


def remove(_list: 'list'):
    return lambda _dict: reduce(without, _list, _dict)


persons = [
    {'firstname': 'jack', 'lastname': 'sparrow', 'msisdn': '0456571234'},
    {'firstname': 'Willy', 'lastname': 'weedock', 'msisdn': '0400123345'},
    {'firstname': 'Janet', 'lastname': 'Bubbles', 'msisdn': '0401235678'}
]

result = pipeline(persons, [action(lambda x: x.replace('.', '').title(), 'firstname'),
                            action(lambda x: x.replace('.', '').title(), 'lastname'),
                            action(lambda x: "+358" + x[1:], 'msisdn'),
                            remove(['firstname'])])

print(list(result))
