class Rectangle:
    def __init__(self, length: int, width: int):
        self.length = length  ### Initialize the length attribute
        self.width = width    ### Initialize the width attribute

###Enable iteration over the instance
    def __iter__(self):
        yield {'length': self.length}  # Yield the length in the required format
        yield {'width': self.width}     # Yield the width in the required format

### usage
rect = Rectangle(5, 10)

### Iterating over the instance
for dimension in rect:
    print(dimension)
