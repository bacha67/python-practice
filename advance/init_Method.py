class Dog:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def bark(self):
        print(self.name,"says Woof!")

1
d1=Dog("Buddy",3)
d1.bark()

# Create the Student class
class Student:
    def __init__(self, name, grade):
         self.name=name
         self.grade=grade

# Create an object
s1=Student("Anna","A")
# Print the grade
print(s1.grade)
# Change the grade
s1.grade="B"
# Print the updated grade
print(s1.grade)

    