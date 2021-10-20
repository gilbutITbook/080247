def sum_numbers(numbers):
    return sum(int(x)
                for x in numbers.split()
                if x.isdigit() )
    
print(sum_numbers('10 20 30 abcd efgh 40 50'))