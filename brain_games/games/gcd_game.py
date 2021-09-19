"""GCD Game."""
from math import gcd
from random import randint

import prompt
from brain_games.game import run_game

MAX_PERIOD = 100


def gcd_game():
    """Play GCD Game."""
    instruction = 'Find the greatest common divisor of given numbers.'

    run_game(get_game_data, instruction)


def get_game_data():
    """
    Game data.

    Returns:
        tuple

    """
    (question, right_answer) = get_question_data()
    print('Question: {0}'.format(question))
    answer = prompt.string('Your answer: ')

    return (int(answer), right_answer)


def get_question_data():
    """
    Make question data.

    Returns:
        tuple
    """
    number_one = randint(1, MAX_PERIOD)
    number_two = randint(1, MAX_PERIOD)
    right_answer = gcd(number_one, number_two)
    question = '{0} {1}'.format(number_one, number_two)

    return (question, right_answer)
