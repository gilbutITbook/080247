def plword(word):
    if word[0] in 'aeiou':
        return word + 'way'

    return word[1:] + word[0] + 'ay'

def plfile(filename):
    return ' '.join(plword(one_word)
     for one_line in open(filename)
     for one_word in one_line.split())

print('# 단어 하나 변환')
print(plword('hello'))
print()

print('# 파일 변환')
print('너무 많이 출력하므로, 200번째 글자까지만 출력하게 했습니다.')
print(plfile('etc/words.txt')[:200])