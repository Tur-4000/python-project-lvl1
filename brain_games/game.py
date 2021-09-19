"""Game."""
from random import randint

import prompt

welcome_text = 'Welcome to the Brain Games!'
name_query_text = 'May I have your name?'
greeting_text = 'Hello'
rules_of_play = 'Answer "yes" if the number is even, otherwise answer "no".'
TOUR_COUNTER = 3


def welcome_user():
    """
    Welcome user and prompt type player name.

    Returns:
        str
    """
    print('{0!s}'.format(welcome_text))
    name = prompt.string('{0!s} '.format(name_query_text))
    print('{0!s}, {1!s}!'.format(greeting_text, name))

    return name


def game():
    """Play game."""
    user_name = welcome_user()
    print('{0!s}'.format(rules_of_play))
    tour = TOUR_COUNTER

    while tour > 0:
        question = randint(1, 100)
        right_answer = 'yes' if is_even(question) else 'no'
        print('Question: {0}'.format(question))
        answer = prompt.string('Your answer: ')

        if answer == right_answer:
            print('Correct!')
            tour -= 1
        else:
            print(
                "'{0!s}' is wrong answer ;(. ".format(answer),
                "Correct answer was '{0!s}'".format(right_answer),
            )
            print("Let's try again, {0!s}!".format(user_name))
            tour = TOUR_COUNTER

    print('Congratulations, {0!s}!'.format(user_name))


def is_even(number):
    """
    Check is even number.

    Args:
        number: checked number

    Returns:
        bool
    """
    return number % 2 == 0
