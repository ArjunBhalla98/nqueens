import game
import random
import dna


def run(n):

    # Make a new game

    instance = game.Game(n)
    mutation_rate = 0.01

    # Initialise random population

    dna_pieces = []

    while len(instance.locations) != n:
        y = random.randint(0, 7)
        x = random.randint(0, 7)

        if (y, x) not in instance.locations:
            instance.locations.append(y, x)
            dna_pieces.append(dna.Dna(x, y))

    gens = 0

    # Evolution loop

    while not instance.has_won():

        # Place pieces on the board
        for x, y in instance.locations:
            instance.place(x, y)

        # Calculate fitness of each object, sort dna_pieces by fitness

        for el in dna_pieces:
            el.calc_fitness(instance)

        dna_pieces = sorted(dna_pieces, key=lambda x: x.fitness)
        distr_arr = gen_distr_array(dna_pieces)
        new_places = gen_new_pos(distr_arr, n)  # returns DNA list

    print(instance.board)
    print("Generations: " + str(gens))


def gen_distr_array(pieces):
    """
    Generates a probability distribution array which allows the use of random.choice
    for weighted probabilities.

    pieces is an array of DNA objects.
    """

    f_arr = []

    for item in pieces:
        f_arr += [item]*item.fitness

    return f_arr


def gen_new_pos(arr, n):
    """
    Generates n new places for the board. Mutations occur here.

    arr: list of DNA objects
    n: integer 
    """
