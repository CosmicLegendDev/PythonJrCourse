class Bird:

    def fly(self):
        pass

class Ostrich(Bird):

    def fly(self):
        return "I cant"
    
class Peacock(Bird):

    def fly(self):
        return "I can fly."
    
bird = Ostrich()

bird.fly()

bird = Peacock()

bird.fly()


