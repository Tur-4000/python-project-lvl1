"""Even Game."""
from random import randint

import prompt

from brain_games.game import run_game


def even_game():
    """Play Even Game."""
    instruction = 'Answer "yes" if the number is even, otherwise answer "no".'

    run_game(get_game_data, instruction)


def get_game_data():
    """Game"""
    question = randint(1, 100)
    right_answer = 'yes' if is_even(question) else 'no'
    print('Question: {0}'.format(question))
    answer = prompt.string('Your answer: ')

    return (answer, right_answer)


def is_even(number):
    """
    Check is even number.

    Args:
        number: checked number

    Returns:
        bool
    """
    return number % 2 == 0
