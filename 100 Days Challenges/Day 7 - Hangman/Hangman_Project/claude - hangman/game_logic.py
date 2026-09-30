import os
import sys
import random as rng
from pathlib import Path


def _import_word_gen():
    hangman_project_dir = Path(__file__).resolve().parents[1]
    repo_root = Path(__file__).resolve().parents[4]
    sys.path.insert(0, str(hangman_project_dir))
    original_cwd = os.getcwd()
    try:
        os.chdir(repo_root)
        import word_gen as wg
    finally:
        os.chdir(original_cwd)
    return wg


wg = _import_word_gen()

MAX_LIVES = 6

DIFFICULTY_TIERS = {
    'Very Easy': wg.very_easy_words,
    'Easy': wg.easy_words,
    'Medium': wg.medium_words,
    'Hard': wg.hard_words,
}


class HangmanGame:
    def __init__(self, difficulty_label):
        words = DIFFICULTY_TIERS[difficulty_label]['headword'].to_list()
        self.difficulty_label = difficulty_label
        self.word = rng.choice(words).lower()
        self.guessed_letters = set()
        self.wrong_guesses = 0
        self.lives = MAX_LIVES

    @property
    def display(self):
        return ''.join(letter if letter in self.guessed_letters else '_' for letter in self.word)

    @property
    def is_won(self):
        return all(letter in self.guessed_letters for letter in self.word)

    @property
    def is_lost(self):
        return self.lives <= 0

    @property
    def is_over(self):
        return self.is_won or self.is_lost

    def guess(self, raw_letter):
        letter = raw_letter.strip().lower()

        if len(letter) != 1 or not letter.isalpha():
            return 'invalid'

        if letter in self.guessed_letters:
            return 'already_guessed'

        self.guessed_letters.add(letter)

        if letter in self.word:
            return 'correct'

        self.wrong_guesses += 1
        self.lives -= 1
        return 'wrong'
