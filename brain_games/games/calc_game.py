"""Calc Game."""
from random import choice, randint

import prompt
from brain_games.game import run_game

OPERATIONS = ('+', '-', '*')
MAX_PERIOD = 20


def calc_game():
    """Play Calc Game."""
    instruction = 'What is the result of the expression?'

    run_game(get_game_data, instruction)


def get_game_data():
    """
    Game.

    Returns:
        tuple

    """
    (question, right_answer) = calc()
    print('Question: {0}'.format(question))
    answer = prompt.string('Your answer: ')

    return (int(answer), right_answer)


def calc():
    """
    Calculate.

    Returns:
        tuple
    """
    number_one = randint(1, MAX_PERIOD)
    number_two = randint(1, MAX_PERIOD)
    operation = choice(OPERATIONS)
    right_answer = 0

    if operation == '+':
        right_answer = number_one + number_two
    elif operation == '-':
        right_answer = number_one - number_two
    elif operation == '*':
        right_answer = number_one * number_two

    question = '{0!s} {1!s} {2!s}'.format(number_one, operation, number_two)

    return (question, right_answer)
