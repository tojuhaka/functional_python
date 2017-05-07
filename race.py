""" Example of functional race program with recursion. Prints the race usingh
    multiplied lines  """

from random import random

start_positions = (1, 1, 1)


def increase_positions(positions: 'tuple'):
    return tuple(map(lambda a: a + 1 if random() > 0.3 else a, positions))


def position_output(car_position: 'int'):
    return "-" * car_position


def draw(car_positions: 'tuple'):
    print("")
    print("\n".join(list(map(position_output, car_positions))))


def race(start_position: 'tuple', time: 'int'):
    time -= 1
    if time < 0:
        return start_position

    draw(start_position)
    return race(increase_positions(start_position), time)


race(start_positions, 5)
