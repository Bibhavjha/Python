from abc import ABC,abstractmethod
class Animal(ABC):
    @abstractmethod
    def makesound(self):
        pass
class Dog(Animal):
    def makesound(self):
        print("barks")
class Cat(Animal):
    def makesound(self):
        print("meow")
dog=Dog()
cat=Cat()
dog.makesound()
cat.makesound()