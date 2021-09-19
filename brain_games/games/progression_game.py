"""Progression Game."""
from random import randint

import prompt
from brain_games.game import run_game

LEN_PROGRESSION = 10
MAX_START_RANGE = 50


def progression_game():
    """Play Progression Game."""
    instruction = 'What number is missing in the progression?'

    run_game(get_game_data, instruction)


def get_game_data():
    """
    Get game data.

    Returns:
        tuple

    """
    step = randint(1, 10)
    start = randint(1, MAX_START_RANGE)
    (question, right_answer) = make_progression(start, step)
    print('Question: {0}'.format(question))
    answer = prompt.string('Your answer: ')

    return (int(answer), right_answer)


def make_progression(start, step):
    """
    Generate question data.

    Args:
        start: int
        step: int

    Returns:
        tuple
    """
    missing = randint(1, LEN_PROGRESSION)
    question = ''
    count = 1
    element = start
    right_answer = None
    while count <= LEN_PROGRESSION:
        if count == missing:
            question += '{0!s} '.format('..')
            right_answer = element
        else:
            question += '{0!s} '.format(element)

        element += step
        count += 1

    return (question[:-1], right_answer)
