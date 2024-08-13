def is_palindrome_iterative(word):
    if not word:
        return False
    word_size = len(word)
    return word[:word_size] == word[::-1]
