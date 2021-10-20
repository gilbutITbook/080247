class Animal:
    def __init__(self, color, number_of_legs):
        self.color = color
        self.number_of_legs = number_of_legs
        self.species = self.__class__.__name__.lower()

    def __repr__(self):
        return f'{self.color} {self.species}, {self.number_of_legs} legs'

class Wolf(Animal):
    def __init__(self, color):
        super().__init__(color, 4)
        
class Sheep(Animal):
    def __init__(self, color):
        super().__init__(color, 4)
        
class Snake(Animal):
    def __init__(self, color):
        super().__init__(color, 0)
        
class Parrot(Animal):
    def __init__(self, color):
        super().__init__(color, 2)

class Cage:
    def __init__(self, id_number):
        self.id_number = id_number
        self.animals = []
        
    def add_animals(self, *args):
        for one_animal in args:
            self.animals.append(one_animal)
            
    def __repr__(self):
        output = f'Cage {self.id_number}\n'
        output += '\n'.join(f'\t{one_animal}'
                            for one_animal in self.animals)
        return output

class Zoo:
    def __init__(self):
        self.cages = []
        
    def add_cages(self, *args):
        for one_cage in args:
            self.cages.append(one_cage)
            
    def __repr__(self):
        return '\n'.join(str(one_cage)
                         for one_cage in self.cages)
    
    def animals_by_color(self, color):
        return [one_animal
               for one_cage in self.cages
               for one_animal in one_cage.animals
               if one_animal.color == color]
    
    def number_of_legs(self):
        return sum([one_animal.number_of_legs
               for one_cage in self.cages
               for one_animal in one_cage.animals])

wolf = Wolf('black')
sheep1 = Sheep('black')
sheep2 = Sheep('white')
snake = Snake('brown')
parrot = Parrot('green')

c1 = Cage(1)
c1.add_animals(wolf, sheep1, sheep2)

c2 = Cage(2)
c2.add_animals(snake, parrot)

z = Zoo()
z.add_cages(c1, c2)
print(z)

print(z.animals_by_color('green'))
print(z.number_of_legs())