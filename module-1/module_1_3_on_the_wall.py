# Kristopher Duda. September 14, 2025. Assignment 1.3: On the Wall Song
# This short program represents the "Beer on the Wall" song. The user is prompted to enter
# a starting number of beers on the wall and the program counts down the number of bottles
# left in accordance with the song until there are no beers left and it is time to buy some more.


def on_the_wall(bottles: int):
    # This function counts down the bottles of beer starting from an int value assigned to 'bottles'
    while bottles > 1:
        print(f"{bottles} bottles of beer on the wall, {bottles} bottles of beer.")
        bottles -= 1
        if bottles > 1:
            print(f"Take one down and pass it around, {bottles} bottles of beer on the wall.\n")
        else:
            print(f"Take one down and pass it around, {bottles} bottle of beer on the wall.\n")
    
    # When 1 bottle remains, user is told to buy more beer
    print(f"1 bottle of beer on the wall, 1 bottle of beer.")
    print("Take it down and pass it around, 0 bottles of beer on the wall.\n")
    print("Time to buy more bottles of beer!\n")


# Main program
if __name__ == "__main__":
    bottlestart = int(input("Enter the number of bottles:"))
    print()
    on_the_wall(bottlestart)


            

