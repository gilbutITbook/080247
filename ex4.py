def hex_output(hexnum):
    total = 0
    for index, one_digit in enumerate(reversed(hexnum)):
#         print(f'{one_digit} * 16 ** {index}')
        total += int(one_digit, 16) * 16 ** index
    return total
        
        
print(hex_output('ff'))