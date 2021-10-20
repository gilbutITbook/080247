def firstlast(s):
    return s[:1] + s[-1:]

print(firstlast('abc'))  # 'ac'
print(firstlast([10, 20, 30, 40, 50]))  # [10, 50]
print(firstlast((100, 200, 300, 400)))  # (100, 400)