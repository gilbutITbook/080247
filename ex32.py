d = {'a':1, 'b':2, 'c':3, 'd':4}

def flipped_dict(a_dict):
    return {
        value : key
        for key, value in a_dict.items()
    }

print(flipped_dict(d))