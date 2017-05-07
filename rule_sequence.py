""" Example of rule sequence function that matches string of binaries based on the rules
    given. Once all rules are checked, return the result of final rule. """

from typing import Optional


def zero(s: 'str') -> str:
    if s[0] == "0":
        return s[1:]


def one(s: 'str') -> str:
    if s[0] == "1":
        return s[1:]


def rule_sequence(s: 'str', rules: 'tuple') -> Optional[str]:
    if not rules or not s:
        return s if s else None
    return rule_sequence(rules[0](s), rules[1:])


print(rule_sequence('0101', (zero, one, zero)))
print(rule_sequence('01010', (zero, one, zero, one)))
print(rule_sequence('0101', (zero, zero)))
print(rule_sequence('', (zero, zero)))
print(rule_sequence(None, (zero, zero)))
