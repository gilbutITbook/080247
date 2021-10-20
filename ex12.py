WORDS = ['this', 'is', 'an', 'elementary', 'test', 'example']
    
# this - 0
# is - 0
# an - 0
# elementary - e 3
# test - 2
# example - 2

from collections import Counter

def most_repeating_letter_count(word):
    return Counter(word).most_common(1)[0][1]

# most_repeating_letter_count('elementary')

def most_repeating_word(words):
    return max(words, key=most_repeating_letter_count)
    
print(most_repeating_word(WORDS))