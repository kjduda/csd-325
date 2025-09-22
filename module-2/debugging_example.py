# Kristopher Duda. September 21, 2025. Assignment 2.2: Debugging
# This short program is used as an example to demonstrate the debugging process. It is 
# borrowed from the debugging guide at https://cse232-msu.github.io/CSE232/debugging_guide.html.
# The program itself starts a for loop that iterates five times, each time generating a random
# number. The program then computes and displays the average of those five numbers.

from random import randint

def average(li: list) -> float:
    avg = 0
    for num in li:
        avg += num
    avg /= len(li)
    return avg

def main():
    li = []
    for _ in range(5):
        li.append(randint(1, 10))
    
    avg = average(li)
    print(avg)

if __name__ == "__main__":
    main()