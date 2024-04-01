def word_reverse(word):
    rword = ""
    for char in word:
        rword = char + rword
    return rword

def check_polindrom(word):
    return word == word_reverse(word)

def print_word_polindrom(word):
    result = check_polindrom(word)
    if result:
        print("polindrom")
    else:
        print("not a polindrom")


print_word_polindrom("madam")
print_word_polindrom("day")
