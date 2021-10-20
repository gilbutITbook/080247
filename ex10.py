def mysum(*items):
    if not items:
        return items
    
    output = items[0]
    for one_item in items[1:]:
        output += one_item
    return output

print(mysum(10, 20, 30))
print(mysum(100, 200, 300, 400, 500))