""" Example of rule sequence function that matches string of binaries based on the rules
    given. Once all rules are checked, return the result of final rule. """


def zero(s):
    if s[0] == "0":
        return s[1:]


def one(s):
    if s[0] == "1":
        return s[1:]


def rule_sequence(s, rules):
    if not rules:
        return s
    s = rules[0](s)
    return rule_sequence(s, rules[1:])


print(rule_sequence('0101', (zero, one, zero)))
print(rule_sequence('0101', (zero, zero)))
