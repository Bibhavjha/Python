class animal:
    def makesound(self):
        print("generic animal sound")
class dog(animal):
    def makesound(self):
        print("bark")
class cat(animal):
    def makesound(self):
        print('meow')
d=dog()
d.makesound()
c=cat()
c.makesound()