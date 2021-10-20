class MyEnumerate:
    def __init__(self, data):
        self.data = data
        self.index = 0
        
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.index >= len(self.data):
            raise StopIteration
            
        value = (self.index, self.data[self.index])
        self.index += 1
        return value
    
    
    
for index, one_item in MyEnumerate('abcd'):
    print(f'{index} : {one_item}')