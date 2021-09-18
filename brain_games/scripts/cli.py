"""Вывод приветствия и запрос имени игрока."""
import prompt


def welcome_user():
    """Display welcome and prompt palayer name."""
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print('Hello, {0!s}!'.format(name))
