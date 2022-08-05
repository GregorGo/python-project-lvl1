"""Этот скрипт содержит функцию welcome_user."""

import prompt

"""Описание функции."""
def welcome_user():
	"""
     Это первая наша функция.
	"""
	name = prompt.string('May I have your name? ')
	print('Hello, {}!'.format(name))
