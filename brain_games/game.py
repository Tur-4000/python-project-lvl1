"""Game."""
import prompt

MAX_TOUR_COUNTER = 3


def run_game(game_data, instruction):
    """Play game.

    Args:
        game_data: callable
        instruction: string
    """
    print('Welcome to the Brain Games!')
    user_name = prompt.string('May I have your name? ')
    print('Hello, {0!s}!'.format(user_name))
    print('{0!s}'.format(instruction))

    tour = 0

    while tour < MAX_TOUR_COUNTER:
        (answer, right_answer) = game_data()
        if answer == right_answer:
            print('Correct!')
            tour += 1
        else:
            print(
                "'{0!s}' is wrong answer ;(. ".format(answer),
                "Correct answer was '{0!s}'".format(right_answer),
            )
            print("Let's try again, {0!s}!".format(user_name))
            return None

    print('Congratulations, {0!s}!'.format(user_name))
