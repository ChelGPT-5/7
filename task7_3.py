words = ['abc', 'aabb', 'zxcvbbvcxz', 'aboba', 'Project', 'runnur']

def check_words(word):
    return word == word[::-1] #использование среза [:: -1] для проверки строки на палиндром


palindrome_words = list(filter(check_words, words))


print(palindrome_words)