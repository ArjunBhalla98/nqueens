import numpy as np


class Dna():

    """
    The Dna class represents a Dna object, with genetic information being the
    x and y co-ordinates
    """

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.fitness = 0

    def calc_fitness(self, game):
        """
        Given some game instance, this will calculate the fitness of the current
        DNA object. game is a Game object.
        """

        self.fitness = 8 - game.num_cross(self.x, self.y)
        return self.fitness
