# 'hello' -> 'hubellubo'

def ubbi_dubbi(word):
    output = ''
    for one_letter in word:
        if one_letter in 'aeiou':
            output += f'ub{one_letter}'
        else:
            output += one_letter
    return output

print(ubbi_dubbi('hello'))