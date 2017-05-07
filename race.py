""" Example of functional race program with recursion """

from random import random

start_positions = (1, 1, 1)


def increase_positions(positions: 'tuple'):
    return tuple(map(lambda a: a + 1 if random() > 0.3 else a, positions))


def draw(car_position: 'tuple'):
    print("-" * car_position)


def race(start_position: 'tuple', time: 'int'):
    time -= 1
    if time < 0:
        return start_position

    print("")
    for position in start_position:
        draw(position)

    return race(increase_positions(start_position), time)


race(start_positions, 5)
