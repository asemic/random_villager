import random
import numpy


def main():

    species = 35 # There are 35 species of animals in the game.
    animals = 23 # There are 23 different cats. Change this depending on what villager species you have

    p = 1 / (species*animals - 9)
    trials = 10000
    probs = [] # initialize array
    steps = 100
    table = False # Set this to true if you want to print a table
    summary = True # Set this to true if you just want a summary
    cutoffs = [0.01, 0.05, 0.1, 0.25, 0.5, 0.75, 0.90, 0.95, 0.99]

    for x in range(trials):
        probs.append((x, 1-pow(1 - p, x))) # Ordered pairs; each signifies (nth trial, probability after n trials)

    for item in probs:
        if table:
            if item[0] % steps == 0:
                if item[0] < 10:
                    print(" ", end="")
                if item[0] < 100:
                    print(" ", end="")
                print(str(item[0])+" | "+str(numpy.round(item[1], decimals=2)))

    if summary:

        print("There is a " + str(p*100) + "% chance of finding RAYMOND.\n") # Switch the name if u want

        for cutoff in cutoffs:
            found = False
            while not found:
                for item in probs:
                    if item[1] > cutoff:
                        print(str(cutoff*100)+"% chance of finding Raymond after searching "+str(item[0])+" islands.")
                        found = True
                        break
                if not found:
                    print(str(cutoff*100)+"% chance not found after "+str(trials)+" islands.")
                    found = True

if __name__ == "__main__":
    main()
