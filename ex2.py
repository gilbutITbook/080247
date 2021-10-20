def mysum(*args):
    total = 0
    for one_number in args:
        total += one_number
    return total

print(mysum(1,2,3))  # 6

print(mysum(10, 20, 30, 40, 50))  # 150