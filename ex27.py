import random

def create_password_generator(characters):
    def create_password(length):
        output = []

        for i in range(length):
            output.append(random.choice(characters))

        return ''.join(output)

    return create_password
    
f = create_password_generator('abcdefghij!@#$%')
print(f)
print(f(10))
print(f(10))