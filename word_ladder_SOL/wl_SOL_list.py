import string

def word_ladder_neighbors(current_word, valid_words):
    '''
    Given a word (current_word) as a string and a set of valid words,
    returns a list of words that are all one letter different 
    than current_word.
    '''
    neighboring_words = []
    alphabet = string.ascii_lowercase
    for i in range(len(current_word)):
        for letter in alphabet:
            new_word = current_word[:i] + letter + current_word[i+1:]
            if new_word in valid_words:
                neighboring_words.append(new_word)
    return neighboring_words

def word_ladder_search(valid_words, start_word, end_word, heuristic=None):
    '''
    Given a list of valid words, a starting word (string), and an ending 
    word (string), returns the path of strings representing the word ladder from
    start_word to end_word.
    '''
    parent = {start_word:None}
    queue = [start_word]
    visited = {start_word}
    current = None

    num_explored = 0
    while queue:
        current = queue.pop(0)
        num_explored+=1
        for n in word_ladder_neighbors(current, valid_words):
            if n == end_word:
                parent[n]=current
                path = [n]
                current_word = n
                while current_word!=start_word:
                    path.append(parent[current_word])
                    current_word=parent[current_word]
                return path[::-1], num_explored
            if n not in visited:
                visited.add(n)
                parent[n]=current
                queue.append(n)
        
        if heuristic!=None:
            queue.sort(key=lambda x : heuristic(x, end_word), reverse=True)

def heuristic_function(current_word, end_word):
    correct_letters=0
    for i in range(len(current_word)):
        if current_word[i]==end_word[i]:
            correct_letters+=1
    return correct_letters


if __name__=="__main__":
    # valid_words is a set containing all strings that should be considered valid
    # words (all in lower-case)
    with open('words_alpha.txt') as f:
        valid_words = {i.strip() for i in f}

    print("You have", len(valid_words), "words to work with.")
    start = "start"
    end = "final"

    # path, num_explored = word_ladder_search(valid_words, start, end)
    path, num_explored = word_ladder_search(valid_words, start, end, heuristic=heuristic_function)
    for word in path:
        print(word)
    print("You explored", num_explored, "words to get here!")


    

