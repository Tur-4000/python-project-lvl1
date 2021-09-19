"""Even Game."""
from random import randint

import prompt
from brain_games.game import run_game


def prime_game():
    """Play Prime Game."""
    instr = 'Answer "yes" if given number is prime. Otherwise answer "no".'

    run_game(get_game_data, instr)


def get_game_data():
    """
    Prepare game data.

    Returns:
        tuple
    """
    question = randint(1, 100)
    right_answer = 'yes' if is_prime(question) else 'no'
    print('Question: {0}'.format(question))
    answer = prompt.string('Your answer: ')

    return (answer, right_answer)


def is_prime(number):
    """
    Check is prime number.

    Args:
        number: checked number

    Returns:
        bool
    """
    if number < 2:
        return False
    div = 2

    while number % div != 0:
        div += 1

    return div == number
