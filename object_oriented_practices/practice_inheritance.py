
class Pet:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show(self):
        print(f"I am {self.name} and I am {self.age} years old")

    def speak(self):
        print("I don't know what I say")


class Cat(Pet):     # inherit from Pet
    def __init__(self, name, age, color):
        super().__init__(name, age)
        self.color = color

    def speak(self):        # 상위 speak method를 override
        print(f"Meow, This is me: {self.name}, {self.age}, and {self.color}")

class Dog(Pet):     # inherit from Pet
    def speak(self):        # 상위 speak method를 override
        print("Bark")

class Fish(Pet):
    pass

p = Pet("Tim", 19)
p.speak()
c = Cat("Bill", 34, 'Blue')  # Pet이 Cat으로 상속됨, Pet class 포함
c.show()
c.speak()
d = Dog("Jill", 25)
d.speak()
f = Fish("Bubbles", 12)
f.speak()
