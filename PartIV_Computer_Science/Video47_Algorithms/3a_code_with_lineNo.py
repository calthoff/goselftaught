def is_palindrome(word):
    word = word.lower()
    return word[::-1] == word
