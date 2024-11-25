import string
from util import *

def word_ladder_neighbors(current_word, valid_words):
    '''
    Given a word (current_word) as a string and a set of valid words,
    returns a list of words that are all one letter different 
    than current_word.
    '''
    alphabet = string.ascii_lowercase

    return []

def word_ladder_search(valid_words, start_word, end_word):
    '''
    Given a list of valid words, a starting word (string), and an ending 
    word (string), returns the path of of strings representing the word ladder from
    start_word to end_word.
    '''
    return None

def better_word_ladder_search(valid_words, start_word, end_word):
    '''
    Given a list of valid words, a starting word (string), and an ending 
    word (string), returns the path of of strings representing the word ladder from
    start_word to end_word. This search should use heuristic_function to speed up
    the search.
    '''
    return None

def heuristic_function(state, end_word):
    pass


if __name__=="__main__":
    # valid_words is a set containing all strings that should be considered valid
    # words (all in lower-case)
    with open('words_alpha.txt') as f:
        valid_words = {i.strip() for i in f}

    print("You have", len(valid_words), "words to work with.")

    # start = "tide"
    # end = "pool"

    # path = word_ladder_search(valid_words, start, end)