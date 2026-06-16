import random


class Spelling:
    def __init__(self):
        '''Constants used to refer to elements of words list'''
        self.MISSPELLED = 1
        self.CORRECT = 0

        '''Accesses the words.txt file and enters the contents into the words list'''
        with open("words.txt", "r", encoding="utf-8") as file:
            self.words = [line.split() for line in file if line.strip()]

        '''Initialising lists'''
        self.spelling_list = [0] * 10
        self.misspelled_words = [0] * 10
        self.correct_words = [0] * 10
        self.results = [0] * 10
