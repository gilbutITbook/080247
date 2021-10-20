import operator

def calc(to_solve):
    op, first_s, second_s = to_solve.split()
    first = int(first_s)
    second = int(second_s)
    
    operations = {'+': operator.add,
                 '-': operator.sub,
                 '*': operator.mul,
                 '/': operator.truediv,
                 '**': operator.pow,
                 '%':operator.mod}
    
    return operations[op](first, second)

print(calc('+ 10 3'))