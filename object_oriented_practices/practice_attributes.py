
class Person:
    number_of_people = 0 # class attributes
    GRAVITY = -9.8

    def __init__(self, name):
        self.name = name
        Person.add_person()

    @classmethod        # class method, only access to class itself
    def number_of_people_(cls):
        return cls.number_of_people

    @classmethod
    def add_person(cls):
        cls.number_of_people += 1

p1 = Person("Tim")
print(Person.number_of_people)
p2 = Person("Jill")
print(p1.number_of_people)

Person.number_of_people = 9
print(p2.number_of_people)
print(p1.number_of_people)

print(Person.number_of_people_()) # only access these class attributes or anything specific to the class

# static methods
class Math:

    @staticmethod
    def add5(x):
        return x + 5

    @staticmethod
    def add10(x):
        return x + 10

    @staticmethod
    def pr():
        print("\nThis is about static method\nrun")

Math.pr()