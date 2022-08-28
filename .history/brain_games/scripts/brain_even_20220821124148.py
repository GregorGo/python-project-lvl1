#!/usr/bin/env python3
"""Скрипт для запуска."""

from brain_games.even import welcome_user, random_game


def main():
    """Сыграть в игру на делимость."""
    welcome_user()
    random_game()
    

if __name__ == '__main__':
    main()