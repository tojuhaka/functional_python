""" Let's say we have migration data from old system and we need to move that data to the new system.
The data is pretty bad since the old system didn't have much validation and conversions for the incoming data.

We need to convert the incoming data so that these rules will be applied:

- lastname and firstname should start with an upper case letter
- all the numbers should have +358 prefix on them
- dots should be removed from names

Most of the imperative code we'll see looks like this::

def change_persons(persons):
    for person in persons:
        person['firstname'] = person['firstname'].replace('.', '')
        person['firstname'] = person['firstname'].title()
        person['lastname'] = person['lastname'].replace('.', '')
        person['lastname'] = person['lastname'].title()
        person['msisdn'] = "+358" + person['msisdn'][1:]

change_persons(persons)
print(persons)

This is a short example, so it's still quite maintainable but imagine having
lot of these conversions. They can't be reused individually and there is
danger of side effects since we're changing the mutable list on the fly. It's also
not that readable and doesn't tell us what the code should do.

Below is one of the functional approaches.
"""

from functools import reduce


def change_dict_value(_d: 'dict', key: 'str', value: 'str') -> dict:
    dict_copy = _d.copy()
    dict_copy[key] = value
    return dict_copy


def remove_dots_from_names(data: 'dict') -> dict:
    _d = change_dict_value(data, 'firstname', data['firstname'].replace('.', ''))
    return change_dict_value(_d, 'lastname', data['lastname'].replace('.', ''))


def capitalize_names(data: 'dict') -> dict:
    _d = change_dict_value(data, 'firstname', data['firstname'].title())
    return change_dict_value(_d, 'lastname', data['lastname'].title())


def add_prefix_to_msisdn(data: 'dict') -> dict:
    return change_dict_value(data, 'msisdn', "+358" + data['msisdn'][1:])


def pipeline(data: 'list', functions: 'list') -> map:
    return reduce(lambda a, x: map(x, a), functions, data)


persons = [
    {'firstname': 'jack', 'lastname': 'sparrow', 'msisdn': '0456571234'},
    {'firstname': 'Willy', 'lastname': 'weedock', 'msisdn': '0400123345'},
    {'firstname': 'Janet', 'lastname': 'Bubbles', 'msisdn': '0401235678'}
]
result = pipeline(persons, [remove_dots_from_names, capitalize_names, add_prefix_to_msisdn])
print(list(result))
