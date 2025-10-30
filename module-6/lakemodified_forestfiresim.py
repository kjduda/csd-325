# Kristopher Duda. October 19, 2025. Assignment 6.2: Forest Fire Sim Modified with Lake.
# This program is a modified version of Sue Sampson's Forest Fire Sim. The original program 
# represents a forest fire by using a grid of cells. Each cell represents a tree, a fire, or
# is empty. A forest is created with an initial tree density (of trees and empty spaces). Each
# empty space has a chance of growing a tree, and each tree has a chance of catching fire from
# lightning. Trees on fire can spread to other trees, and an empty space is created when the
# fire burns outs. An infinite loop is used to simulate this forest fire simulation, and it 
# undergoes changes in real time on the screen until the user exits by pressing Ctrl-C.
#
# This modified version of the forest fire simulation adds the following:
# 1. A lake roughly in the center of the display is added
# 2. The water feature uses a different character ~ and is blue.
# 3. The water feature cannot be modified once it is in place: it acts as a firebreak that flames cannot cross.

"""Forest Fire Sim, modified by Sue Sampson, based on a program by Al Sweigart
A simulation of wildfires spreading in a forest. Press Ctrl-C to stop.
Inspired by Nicky Case's Emoji Sim http://ncase.me/simulating/model/
** use spaces, not indentation to modify **
Tags: short, bext, simulation"""

import random, sys, time

try:
    import bext
except ImportError:
    print('This program requires the bext module, which you')
    print('can install by following the instructions at')
    print('https://pypi.org/project/Bext/')
    sys.exit()

# Set up the constants:
WIDTH = 79
HEIGHT = 22

TREE = 'A'
FIRE = '@'
EMPTY = ' '
WATER = '~'  # MODIFICATION FOR WEEK 6: New symbol to represent lake cells

# (!) Try changing these settings to anything between 0.0 and 1.0:
INITIAL_TREE_DENSITY = 0.20  # Amount of forest that starts with trees.
GROW_CHANCE = 0.01  # Chance a blank space turns into a tree.
FIRE_CHANCE = 0.01  # Chance a tree is hit by lightning & burns.

# (!) Try setting the pause length to 1.0 or 0.0:
PAUSE_LENGTH = 0.5


def main():
    forest = createNewForest()
    bext.clear()

    while True:  # Main program loop.
        displayForest(forest)

        nextForest = {'width': forest['width'], 'height': forest['height']}

        for x in range(forest['width']):
            for y in range(forest['height']):
                if (x, y) in nextForest:
                    continue  # Already set this cell in nextForest.

                currentCell = forest[(x, y)]

                # MODIFICATION FOR WEEK 6: Water cells are not modified
                if currentCell == WATER:
                    nextForest[(x, y)] = WATER
                    continue

                # Trees can grow in empty cells
                if currentCell == EMPTY and random.random() <= GROW_CHANCE:
                    nextForest[(x, y)] = TREE

                # Lightning can strike trees
                elif currentCell == TREE and random.random() <= FIRE_CHANCE:
                    nextForest[(x, y)] = FIRE

                # Fire activity
                elif currentCell == FIRE:
                    # MODIFICATION FOR WEEK 6: Fire only spreads to neighboring trees, not to water
                    for ix in range(-1, 2):
                        for iy in range(-1, 2):
                            neighbor = (x + ix, y + iy)
                            if forest.get(neighbor) == TREE:
                                nextForest[neighbor] = FIRE
                    # The tree has burned down now, so erase it:
                    nextForest[(x, y)] = EMPTY

                # Just copy the existing object:
                else:
                    nextForest[(x, y)] = currentCell

        forest = nextForest
        time.sleep(PAUSE_LENGTH)


def createNewForest():
    """Returns a dictionary for a new forest data structure: MODIFIED TO HAVE A LAKE"""
    forest = {'width': WIDTH, 'height': HEIGHT}
    lake_width = WIDTH // 5
    lake_height = HEIGHT // 4
    lake_x_start = (WIDTH // 2) - (lake_width // 2)
    lake_y_start = (HEIGHT // 2) - (lake_height // 2)

    for x in range(WIDTH):
        for y in range(HEIGHT):
            # Create lake in centralized location:
            if (lake_x_start <= x < lake_x_start + lake_width) and (lake_y_start <= y < lake_y_start + lake_height):
                forest[(x, y)] = WATER
            else:
                # Create the rest of the forest
                if random.random() <= INITIAL_TREE_DENSITY:
                    forest[(x, y)] = TREE
                else:
                    forest[(x, y)] = EMPTY
    return forest


def displayForest(forest):
    """Display the forest data structure on the screen."""
    bext.goto(0, 0)
    for y in range(forest['height']):
        for x in range(forest['width']):
            cell = forest[(x, y)]
            if cell == TREE:
                bext.fg('green')
                print(TREE, end='')
            elif cell == FIRE:
                bext.fg('red')
                print(FIRE, end='')
            elif cell == WATER:
                bext.fg('blue')
                print(WATER, end='')
            elif cell == EMPTY:
                print(EMPTY, end='')
        print()
    bext.fg('reset')
    print('Grow chance: {}%  '.format(GROW_CHANCE * 100), end='')
    print('Lightning chance: {}%  '.format(FIRE_CHANCE * 100), end='')
    print('Press Ctrl-C to quit.')


# Run the simulation:
if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        sys.exit()


