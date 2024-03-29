import os

def find_longest_word(filename):
    longest_word = ''
    try:
        for one_line in open(filename):
            for one_word in one_line.split():
                if len(one_word) > len(longest_word):
                    longest_word = one_word
    except (OSError, UnicodeDecodeError) as e:
        print(f'Ignoring {filename}: {e}')
    return longest_word

def find_all_longest_words(dirname):
    return {
        filename : find_longest_word(os.path.join(dirname, filename))
        for filename in os.listdir(dirname)
        if os.path.isfile(os.path.join(dirname, filename))
    }

print(find_longest_word('etc/wcfile.txt'))
print(find_all_longest_words('.'))
# find_all_longest_words는 현재 폴더의 python 파일을 대상으로 실행하게 했습니다.