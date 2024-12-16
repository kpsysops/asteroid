from circleshape import *
from constants import *

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x,y,radius)  # FIX
        pass

    def draw(self, screen): #ADDED
        pygame.draw.circle(screen, "white", self.position, self.radius,2) #ADDED

    def update(self,dt):
        self.position += self.velocity * dt # ADDED

