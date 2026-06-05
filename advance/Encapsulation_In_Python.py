class Vehicle:
    def __init__(self, brand, model):
        self.brand = brand
        self.__model = model
    def get_model(self):
         return self.__model

    def move(self):
        print("Move!")

class Car(Vehicle):
    pass

class Boat(Vehicle):
    def move(self):
        print("Sail!")

class Plane(Vehicle):
    def move(self):
        print("Fly!")

car1 = Car("Ford", "Mustang")
boat1 = Boat("Ibiza", "Touring 20")
plane1 = Plane("Boeing", "747")

for x in (car1, boat1, plane1):
    print(x.brand)
    print(x.get_model())
    x.move()

    #exmple 2
    class ScoreBoard:
        def __init__(self,score):
            self.__score=score
        def get_score(self):
            return self.__score
        
    s1=ScoreBoard(7)
    print(s1.get_score())