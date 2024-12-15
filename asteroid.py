from circleshape import *
from constants import *

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        pass

    def draw(self): #ADDED
        pygame.draw.circle(screen, "white", self.position, self.radius,2) #ADDED

    def update():
        self.position += self.velocity * dt # ADDED

