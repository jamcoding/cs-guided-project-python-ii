class Animal:
    def __init__(self, kind, color, name):
        # Construct a new instance of animal
        # define properties of "Animal"
        # "self" variable: mandatory at the beginning of any class function
        # "self" works similar to "this"

        self.kind = kind
        self.color = color
        self.name = name
        self.num_legs = 4

    def description(self):
        # use terminal to run 
        print(f'{self.name} is a {self.kind} with color {self.color}')

cat = Animal('cat', 'orange', 'Tabby') # calls __init__
dog = Animal('dog', 'golden', 'Woffie') # calls __init__

# print(cat.kind)
# print(dog.kind)

cat.description()
dog.description()

print(cat.num_legs)