import sys
import os
import pandas
import numpy as np
import matplotlib.pyplot as plt
from scipy.spatial import distance

# prompt user for file name to read, assuming this is a csv
pwd = os.getcwd()
pwd = str(pwd) + "/"
file_name = input("Enter the name of the file including the extension: ")
file_path = str(pwd) + str(file_name)
print(file_path)
with open(str(file_path), 'r') as csvfile:
    my_file = pandas.read_csv(csvfile)

player_selection = input("Enter the player name you want to explore: ")
nfl = my_file
# Manipulate file for the nfl example
nfl_numeric = nfl.select_dtypes(include=[np.number])
nfl_normalized = (nfl_numeric - nfl_numeric.mean()) / nfl_numeric.std()
nfl_normalized.fillna(0, inplace=True)
player_normalized = nfl_normalized[nfl["Player"] == str(player_selection)]
euclidean_distances = nfl_normalized.apply(
    lambda row: distance.euclidean(row, player_normalized), axis=1)


def euclidean_distance(row, selected_player):
    diff = row - selected_player
    squares = diff ** 2
    sum_squares = squares.sum(axis=1)
    sqrt_squares = sum_squares ** 0.5
    return sqrt_squares


nfl_dist = euclidean_distance(nfl_normalized, player_normalized)

# Create a new dataframe with distances.
distance_frame = pandas.DataFrame(
    data={"dist": euclidean_distances, "idx": euclidean_distances.index})
distance_frame.sort_values("dist", inplace=True)
second_smallest = distance_frame.iloc[1]["idx"]
five_smallest = [distance_frame.iloc[1]["idx"], distance_frame.iloc[2]["idx"],
                 distance_frame.iloc[3]["idx"],
                 distance_frame.iloc[4]["idx"], distance_frame.iloc[5]["idx"]]
lst = np.zeros(5)
i = 0
for i in range(5):
    lst = (nfl.iloc[int(five_smallest[i])]["Player"])
    print(i, lst)

"""

def euclidean_distance(row, selected_player):
    diff = row - selected_player
    squares = diff ** 2
    sum_squares = squares.sum(axis=1)
    sqrt_squares = sum_squares ** 0.5
    return sqrt_squares




# look at it to make sure we have a real data set
# We need to extract only the numeric volumns for obvious reasons

nfl_numeric = nfl.select_dtypes(include=[np.number])
distance_columns = list(nfl_numeric.head(0))
selected_player = nfl_numeric[nfl["Player"] == "Julio Jones"].iloc[0]

# Test box plot




# Normalize all of the numeric columns
nfl_normalized = (nfl_numeric - nfl_numeric.mean()) / nfl_numeric.std()
# Fill in NA values in nfl_normalized
nfl_normalized.fillna(0, inplace=True)
# Find the normalized vector for lebron james.
brady_normalized = nfl_normalized[nfl["Player"] == "Julio Jones"]
# Find the distance between lebron james and everyone else.
euclidean_distances = nfl_normalized.apply(lambda row: distance.euclidean(row, brady_normalized), axis=1)

# Create a new dataframe with distances.
distance_frame = pandas.DataFrame(data={"dist": euclidean_distances, "idx": euclidean_distances.index})
distance_frame.sort_values("dist", inplace=True)
# Find the most similar player to lebron (the lowest distance to lebron is lebron,
# the second smallest is the most similar non-lebron player)

second_smallest = distance_frame.iloc[1]["idx"]
five_smallest = [distance_frame.iloc[1]["idx"], distance_frame.iloc[2]["idx"], distance_frame.iloc[3]["idx"],
distance_frame.iloc[4]["idx"], distance_frame.iloc[5]["idx"]]
lst = np.zeros(5)
i=0
for i in range(5):
    lst = (nfl.iloc[int(five_smallest[i])]["Player"])
    print(i, lst)





most_similar_to_brady = nfl.iloc[int(second_smallest)]["Player"]

print("The player most similar to  %s  is: %s" % ("Tom Brady", most_similar_to_brady))

"""
