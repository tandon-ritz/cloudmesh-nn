import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.spatial import distance
import requests
from flask import Flask, request, jsonify, send_file, make_response
import random
from numpy.random import permutation
from sklearn.neighbors import KNeighborsRegressor
import math
import io
from cloudmesh.nn.service import code_dir


def data_selection(filename, player_selection):
    data_dir = code_dir + '/data/'
    file = data_dir + filename
    with open(filename, 'r') as csvfile:
        my_file = pd.read_csv(csvfile)
    nfl = my_file
    nfl_numeric = nfl.select_dtypes(include=[np.number])
    nfl_normalized = (nfl_numeric - nfl_numeric.mean()) / nfl_numeric.std()
    nfl_normalized.fillna(0, inplace=True)
    player_normalized = nfl_normalized[nfl["Player"] == str(player_selection)]
    euclidean_distances = nfl_normalized.apply(
        lambda row: distance.euclidean(row, player_normalized), axis=1)
    distance_frame = pd.DataFrame(
        data={"dist": euclidean_distances, "idx": euclidean_distances.index})
    distance_frame.sort_values("dist", inplace=True)
    second_smallest = distance_frame.iloc[1]["idx"]
    five_smallest = [distance_frame.iloc[1]["idx"],
                     distance_frame.iloc[2]["idx"],
                     distance_frame.iloc[3]["idx"],
                     distance_frame.iloc[4]["idx"],
                     distance_frame.iloc[5]["idx"]]

    lst = []
    i = 0
    for i in range(5):
        players = (nfl.iloc[int(five_smallest[i])]["Player"])
        lst.append(players)
    return lst


def selection(filename, player_selection):
    player_selection = str(player_selection)
    data_dir = code_dir + '/data/'
    path = data_dir + filename
    return data_selection(path, player_selection)


def nfl_knn(filename):
    my_file = pd.read_csv('data/' + filename)
    nfl = my_file
    nfl_numeric = nfl.select_dtypes(include=[np.number])
    nfl_normalized = (nfl_numeric - nfl_numeric.mean()) / nfl_numeric.std()
    nfl_normalized.fillna(0, inplace=True)

    # Randomly shuffle the index of nba.
    random_indices = permutation(nfl_normalized.index)
    # Set a cutoff for how many items we want in the test set (in this case
    # 1/3 of the items)
    test_cutoff = math.floor(len(nfl_normalized) / 3)
    # Generate the test set by taking the first 1/3 of the randomly shuffled
    # indices.
    test = nfl_normalized.loc[random_indices[1:test_cutoff]]
    # Generate the train set with the rest of the data.
    train = nfl_normalized.loc[random_indices[test_cutoff:]]

    # Use sklearn
    nfl_normalized.fillna(0, inplace=True)
    distance_columns = nfl_normalized.head(0)
    predict = "Forty"
    y_columns = predict
    distance_columns.drop([predict], axis=1, inplace=True)
    x_columns = distance_columns
    random_indices = permutation(nfl_normalized.index)
    test_cutoff = math.floor(len(nfl_normalized) / 3)
    test = nfl_normalized.loc[random_indices[1:test_cutoff]]
    train = nfl_normalized.loc[random_indices[test_cutoff:]]

    knn = KNeighborsRegressor(n_neighbors=7)

    x_train = np.nan_to_num(train[x_columns])
    y_train = np.nan_to_num(train[y_columns])
    x_test = np.nan_to_num(test[x_columns])
    y_test = np.nan_to_num(test[y_columns])

    knn.fit(x_train, y_train)
    predictions = knn.predict(x_test)
    # predictions
    actual = y_test
    mse = (((predictions - actual) ** 2).sum()) / len(predictions)
    img = plt.scatter(predictions, actual)
    return


def nfl_knn_results(filename):
    my_file = pd.read_csv('data/' + filename)
    nfl = my_file
    nfl_numeric = nfl.select_dtypes(include=[np.number])
    nfl_normalized = (nfl_numeric - nfl_numeric.mean()) / nfl_numeric.std()
    nfl_normalized.fillna(0, inplace=True)

    # Randomly shuffle the index of nba.
    random_indices = permutation(nfl_normalized.index)
    # Set a cutoff for how many items we want in the test set (in this case
    # 1/3 of the items)
    test_cutoff = math.floor(len(nfl_normalized) / 3)
    # Generate the test set by taking the first 1/3 of the randomly shuffled
    # indices.
    test = nfl_normalized.loc[random_indices[1:test_cutoff]]
    # Generate the train set with the rest of the data.
    train = nfl_normalized.loc[random_indices[test_cutoff:]]

    # Use sklearn
    nfl_normalized.fillna(0, inplace=True)
    distance_columns = nfl_normalized.head(0)
    predict = "Forty"
    y_columns = predict
    distance_columns.drop([predict], axis=1, inplace=True)
    x_columns = distance_columns
    random_indices = permutation(nfl_normalized.index)
    test_cutoff = math.floor(len(nfl_normalized) / 3)
    test = nfl_normalized.loc[random_indices[1:test_cutoff]]
    train = nfl_normalized.loc[random_indices[test_cutoff:]]

    knn = KNeighborsRegressor(n_neighbors=12)

    x_train = np.nan_to_num(train[x_columns])
    y_train = np.nan_to_num(train[y_columns])
    x_test = np.nan_to_num(test[x_columns])
    y_test = np.nan_to_num(test[y_columns])

    knn.fit(x_train, y_train)
    predictions = knn.predict(x_test)
    # predictions
    actual = y_test
    mse = (((predictions - actual) ** 2).sum()) / len(predictions)
    new = [predictions, actual]
    plt.boxplot(new)
    bytes_image = io.BytesIO()
    # bytes_image
    plt.savefig(bytes_image, format='png')
    bytes_image.seek(0)
    return bytes_image


def nfl_knn_results_boxplot(filename):
    bytes_obj = nfl_knn_results(filename)
    return send_file(bytes_obj,
                     attachment_filename='plot.png',
                     mimetype='image/png')
