#!/usr/bin/env python3
"""Программа для запуска."""

from brain_games.cli import welcome_user


def main():
    """Поприветствовать игрока"""
    print("Welcome to the Brain Games!")
    welcome_user() 
    
if __name__ == '__main__':
    main()

