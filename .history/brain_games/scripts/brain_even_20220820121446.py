#!/usr/bin/env python3
"""Программа для запуска."""

from brain_games.cli import welcome_user
from random import randint
 

def main():
    """Поприветствовать игрока."""
    print('Welcome to the Brain Games!')
    welcome_user()
    print('''Answer "yes" if the number is even, otherwise answer "no".
Question: ''') 

if __name__ == '__main__':
    main()