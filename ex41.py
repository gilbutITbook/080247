class Scoop:
    def __init__(self, flavor):
        self.flavor = flavor

class Bowl:
    max_scoops = 3
    
    def __init__(self):
        self.scoops = []
    def add_scoops(self, *new_scoops):
        for one_scoop in new_scoops:
            if len(self.scoops) >= self.max_scoops:
                break
            self.scoops.append(one_scoop)
    def __repr__(self):
        return '\n'.join(one_scoop.flavor
                          for one_scoop in self.scoops)
            

s1 = Scoop('chocolate')
s2 = Scoop('vanilla')
s3 = Scoop('persimmon')

s4 = Scoop('flavor 4')
s5 = Scoop('flavor 5')
s6 = Scoop('flavor 6')

print("**** Bowl")
b = Bowl()
b.add_scoops(s1, s2)
b.add_scoops(s3, s4)
b.add_scoops(s5)
print(b)


class BigBowl(Bowl):
    max_scoops = 5


print("**** BigBowl")
bb = BigBowl()
bb.add_scoops(s1, s2)
bb.add_scoops(s3, s4)
bb.add_scoops(s5)
bb.add_scoops(s6)
print(bb)