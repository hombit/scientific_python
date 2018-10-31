def is_snake(word):
    if not word.isalpha():
        raise ValueError("String '{}' is not a word")
    if word.lower() == 'python':
        return True
    if word.lower() == 'питон':
        return True
    return False
