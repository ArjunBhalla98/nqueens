import game
import random
import dna
import sys


def run(n):

    # Make a new game

    instance = game.Game(n)
    mutation_rate = 0.25

    # Initialise random population

    dna_pieces = []

    while len(instance.locations) != n:
        y = random.randint(0, 7)
        x = random.randint(0, 7)

        if (x, y) not in instance.locations:
            dna_pieces.append(dna.Dna(x, y))
            instance.place(x, y)

    gens = 0

    # Evolution loop

    while not instance.has_won():

        # Place pieces on the board
        for x, y in instance.locations:
            instance.place(x, y)

        # Calculate fitness of each object, sort dna_pieces by fitness

        for el in dna_pieces:
            el.calc_fitness(instance)

        distr_arr = gen_distr_array(dna_pieces)
        new_places = gen_new_pos(
            distr_arr, n, mutation_rate)  # returns DNA list

        instance.clear_board()

        for gene in new_places:
            instance.place(gene.x, gene.y)

        gens += 1
        sys.stdout.write("Current Generation: %i \r" % (gens))
        sys.stdout.flush()

    print()
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


def gen_new_pos(arr, n, mut_rate):
    """
    Generates n new places for the board. Mutations occur here.

    arr: list of DNA objects
    n: integer 
    """
    new_pos = []
    new_pos_tups = []  # Just to keep track of the positions for comparison

    while len(new_pos_tups) != n:
        parent_A = random.choice(arr)
        parent_B = random.choice(arr)

        child = dna.Dna(parent_A.x, parent_B.y)
        mut_x_pr = random.uniform(0, 1)
        mut_y_pr = random.uniform(0, 1)

        if mut_x_pr <= mut_rate:
            child.x = random.randint(0, 7)

        if mut_y_pr <= mut_rate:
            child.y = random.randint(0, 7)

        if (child.x, child.y) not in new_pos_tups:
            new_pos.append(child)
            new_pos_tups.append((child.x, child.y))

    return new_pos


if __name__ == '__main__':
    run(8)
