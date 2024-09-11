# method overriding example
class animal:
    def makesound(self):
        print("animal make sound")
class cat(animal):
    def makesound(self):
        print("cat sounds meow")
class dog(animal):
    def makesound(self):
        print("dog barks")
c=cat()
c.makesound()
d=dog()
d.makesound()
a=animal()
a.makesound()
