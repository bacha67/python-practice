class person():
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def greet(self):
        print('hello my name is',self.name, 'and i am',self.age,'years old')
p1=person('john',36)
p1.greet()