class Dog:
    def __init__(self, name):
        self.name = name
    def bark(self):
        print(f"{self.name}：汪汪！")
my_dog = Dog("阿財")
my_dog.bark()