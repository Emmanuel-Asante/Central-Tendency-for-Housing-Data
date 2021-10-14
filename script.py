# Import packages
import numpy as np
import pandas as pd
from scipy import stats

# Read in housing data
brooklyn_one_bed = pd.read_csv('brooklyn-one-bed.csv')
brooklyn_price = brooklyn_one_bed['rent']

manhattan_one_bed = pd.read_csv('manhattan-one-bed.csv')
manhattan_price = manhattan_one_bed['rent']

queens_one_bed = pd.read_csv('queens-one-bed.csv')
queens_price = queens_one_bed['rent']

# Add mean calculations below

# Calculate the average of brooklyn_price and assign the value to a variable called brooklyn_mean
brooklyn_mean = np.average(brooklyn_price)

# Calculate the average of manhattan_price and assign the value to a variable called manhattan_mean
manhattan_mean = np.average(manhattan_price)

# Calculate the average of queens_price and assign the value to a variable called queens_mean
queens_mean = np.average(queens_price)

# Add median calculations below

# Calculate the median price of Brooklyn and assign the value to brooklyn_median
brooklyn_median = np.median(brooklyn_price)

# Calculate the median price of Manhattan and assign the value to manhattan_median
manhattan_median = np.median(manhattan_price)

# Calculate the median price of Queens and assign the value to queens_median
queens_median = np.median(queens_price)

# Add mode calculations below

# Calculate the modal price of Brooklyn and assign the value to brooklyn_mode
brooklyn_mode = stats.mode(brooklyn_price)

# Calculate the modal price of Manhattan and assign the value to manhattan_mode
manhattan_mode = stats.mode(manhattan_price)

# Calculate the modal price of Queens and assign the value to queens_mode
queens_mode = stats.mode(queens_price)



##############################################
##############################################
##############################################







# Don't look below here
# Mean
try:
    print("The mean price in Brooklyn is " + str(round(brooklyn_mean, 2)))
except NameError:
    print("The mean price in Brooklyn is not yet defined.")
try:
    print("The mean price in Manhattan is " + str(round(manhattan_mean, 2)))
except NameError:
    print("The mean in Manhattan is not yet defined.")
try:
    print("The mean price in Queens is " + str(round(queens_mean, 2)))
except NameError:
    print("The mean price in Queens is not yet defined.")
    
    
# Median
try:
    print("The median price in Brooklyn is " + str(brooklyn_median))
except NameError:
    print("The median price in Brooklyn is not yet defined.")
try:
    print("The median price in Manhattan is " + str(manhattan_median))
except NameError:
    print("The median price in Manhattan is not yet defined.")
try:
    print("The median price in Queens is " + str(queens_median))
except NameError:
    print("The median price in Queens is not yet defined.")
    
    
#Mode
try:
    print("The mode price in Brooklyn is " + str(brooklyn_mode[0][0]) + " and it appears " + str(brooklyn_mode[1][0]) + " times out of " + str(len(brooklyn_price)))
except NameError:
    print("The mode price in Brooklyn is not yet defined.")
try:
    print("The mode price in Manhattan is " + str(manhattan_mode[0][0]) + " and it appears " + str(manhattan_mode[1][0]) + " times out of " + str(len(manhattan_price)))
except NameError:
    print("The mode price in Manhattan is not yet defined.")
try:
    print("The mode price in Queens is " + str(queens_mode[0][0]) + " and it appears " + str(queens_mode[1][0]) + " times out of " + str(len(queens_price)))
except NameError:
    print("The mode price in Queens is not yet defined.")