# Kristopher Duda. October 5, 2025. Assignment 4.2: Sitka Highs and Lows Graphs
# This short program reads data from a CSV file that shows weather data for Sitka, Alaska.
# Matplotlib is then used to plot a graph based on that data. 
# The user is presented with a menu to choose what kind of data to present: Highs, Lows, or Exit.
# If the user selects "Highs", then they will see a graph in red of daily high temperatures 
# If the user selects "Lows", then they will see a graph in blue of daily low temperatures.
# If the user slects "Exit", the program ends with an exit message.
# The program will continue looping back to the menu until the user selects "Exit."

import csv
from datetime import datetime
from matplotlib import pyplot as plt

# Welcome message and menu instructions
print("\nThis program displays daily temperatures of Slitka, Alaska in 2018.")
print("From the following menu, you may select to see high temperatures, low temperatures, or exit.")
print()
print("  To see daily high temperatures, enter 'Highs'.")
print("  To see daily low temperatures, enter 'Lows'.")
print("  To quit the program, enter 'Exit'.")
print()

# Reads data from the CSV file
filename = 'sitka_weather_2018_simple.csv'

dates, highs, lows = [], [], []

with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader) # skips header row that contains column names

    # loops through data, creating lists of high/low temperatures and dates 
    for row in reader:
        current_date = datetime.strptime(row[2], '%Y-%m-%d') # dates in row 2 converted to datetime format
        high = int(row[5]) # high temperatures converted to integers
        low = int(row[6]) # low temperatures converted to integers
        
        dates.append(current_date)
        highs.append(high)
        lows.append(low)

# Menu begins. It will keep looping back to here until user selects "Exit."
while True:
    selection = input("Enter your choice (Highs/Lows/Exit): ").strip().lower()

    # High temperatures are plotted in red when user selects this option
    if selection == 'highs':
        fig, ax = plt.subplots()
        ax.plot(dates, highs, c='red')

        plt.title("Daily High Temperatures - 2018", fontsize=24)
        plt.xlabel('', fontsize=16)
        fig.autofmt_xdate()
        plt.ylabel("Temperature (F)", fontsize=16)
        plt.tick_params(axis='both', which='major', labelsize=16)

        plt.show()

    # Low temperatures are plotted in blue when user selects this option
    elif selection == 'lows':
        fig, ax = plt.subplots()
        ax.plot(dates, lows, c='blue')

        plt.title("Daily Low Temperatures - 2018", fontsize=24)
        plt.xlabel('', fontsize=16)
        fig.autofmt_xdate()
        plt.ylabel("Temperature (F)", fontsize=16)
        plt.tick_params(axis='both', which='major', labelsize=16)

        plt.show()

    # Displays exit message and terminates loop when user selects "Exit"
    elif selection == 'exit':
        print("\nYou have chosen to exit the program. Thank you for trying it out!\n")
        break

    else:
        print("You did not choose a valid option. Please enter 'Highs', 'Lows', or 'Exit'.\n")
