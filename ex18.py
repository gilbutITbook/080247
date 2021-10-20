def get_final_line(filename):
    final_line = ''
    for one_line in open(filename):
        final_line = one_line
    return final_line

print(get_final_line('etc/passwd'))