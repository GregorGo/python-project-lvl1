#!/usr/bin/env python3
"""Script to run."""

from brain_games.engine import run_game
from brain_games.games import gcd


def main():
    """Play a gcd game."""
    run_game(gcd)


if __name__ == '__main__':
    main()
