import os

def all_lines(path):
    for one_filename in os.listdir(path):
        try:
            for one_line in open(os.path.join(path, one_filename)):
                yield one_line
        except: 
            pass
            


for one_line in all_lines('etc/48'):
    print(one_line, end='')