# Monty Hall Simulation
# Robin van der Noord
# 27-12-2021
# https://www.youtube.com/watch?v=4Lb-6rxZxx0

from collections import defaultdict
from pprint import pprint
import numpy.random
import random
import time
import sys


def generate_setup():
    lst = numpy.array([1, 0, 0])
    random.shuffle(lst)
    return lst


def calculate_win(choice, setup):
    return setup[choice] == 1


def switch_door(goat, initial):
    # fixme: optimize?
    return {
        (0, 1): 2,
        (0, 2): 1,
        (1, 0): 2,
        (1, 2): 0,
        (2, 0): 1,
        (2, 1): 2,
    }[(goat, initial)]


def montyhall():
    """
    Procedure:
    1. Contestant chooses one of three doors
    2. Host opens one door with a goat
    3. Contestant chooses either to stay or to switch (-> new choice of the two remaining doors)
    4. Win or Lose

    https://en.wikipedia.org/wiki/Monty_Hall_problem
    """
    d = numpy.array([0, 1, 2])

    # 0. Place goats and car behind doors
    doors = generate_setup()

    # 1. Contestant chooses one of three doors
    initial_door_choice = numpy.random.choice(d)  # initial door choice (3 options)

    # 2. Host opens one door with a goat (that's not the contestant's choice)
    goat_indices = numpy.array([i for i, _ in enumerate(doors) if _ == 0 and i != initial_door_choice])
    remove_index = numpy.random.choice(goat_indices)
    switch = random.randint(0, 1)  # yes or no
    if switch:
        # choose the door that is not initial_door_choice or remove_index

        # first remove the highest index, then the lowest
        # this way, the indices don't shift before removing
        # -> the final choice is kept at index 0
        # doors = numpy.delete(doors, max(remove_index, initial_door_choice))
        # doors = numpy.delete(doors, min(remove_index, initial_door_choice))
        # final_door_choice = 0

        # faster in the case of numpy, slower for numba/vanilla:
        final_door_choice = switch_door(remove_index, initial_door_choice)  # 28.8s vs 36.4s
    else:
        # keep initial choice
        final_door_choice = initial_door_choice

    win = calculate_win(final_door_choice, doors)
    return win, switch


def main(n=1_000_000):
    scores = numpy.zeros(2)

    for _ in range(n):
        win, switch = montyhall()
        scores[switch] += win

    return scores


def print_scores(scores):
    print("Wins if staying", scores[0])
    print("Wins if switching", scores[1])


if __name__ == '__main__':
    print("first:")
    s = time.time()
    print_scores(main())
    print("took", time.time() - s)
    print("additional")
    s = time.time()
    main()
    print("took", time.time() - s)
