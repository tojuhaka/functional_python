""" Combining imperative and functional approach """
from random import random

start_position = (1, 1, 1)


def increase_positions(position: 'tuple') -> tuple:
    return tuple(map(lambda a: a + 1 if random() > 0.3 else a, position))


def position_output(car_position: 'int') -> str:
    return "-" * car_position


def draw(car_positions: 'tuple') -> None:
    print("")
    print("\n".join(list(map(position_output, car_positions))))


def race(start_position: 'tuple', time: 'int') -> tuple:
    for i in range(0, time):
        yield start_position
        start_position = increase_positions(start_position)


[draw(i) for i in race(start_position, 100)]


