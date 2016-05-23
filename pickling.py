# Jeremy Aguillon
# CMSC 471
# Description: short file to pickle the data to make it easier to acces.
#              Only need to run once.

# some extra imports because this was not all separate files to begin with
import matplotlib.pyplot as plt
# uses mpimg for featurizing
import matplotlib.image as mpimg
import numpy as np
from sklearn.neighbors import KNeighborsClassifier
from sklearn import datasets, svm, metrics
# pickles data
import pickle

# different paths images can be in
PATH = "./training"
HEART_PATH = "/00"
HAT_PATH = "/01"
HASH_PATH = "/02"
DOLLAR_PATH = "/03"
SMILE_PATH = "/04"

# label for each image
HEART = 0
HAT = 1
HASH = 2
DOLLAR = 3
SMILE = 4

# string of each image
IMG_TYPE = ["heart","hat","hash","dollar","smile"]

# amount of each image given
HEART_AMT = 81
HAT_AMT = 72
HASH_AMT = 88
DOLLAR_AMT = 87
SMILE_AMT = 85

# main function
def main():
    # used to capture the featurized images and their labels
    hearts = []
    heartcount = []
    hats = []
    hatcount = []
    hashs = []
    hashcount = []
    dollars = []
    dollarcount = []
    smiles = []
    smilecount = []
    
    # old ------ path = "./Data/training/"

    # loops through the amount of images for each group
    for index in range(1, HEART_AMT + 1):
        # builds the correct path
        curExt = "{}/{:02}.jpg".format(HEART_PATH,index)
        curPath = PATH + curExt
        # transforms image to a list
        test = mpimg.imread(curPath)
        test1 = np.array(test)
        test1 = np.sum(test, 2).flatten()
        # counts each final image and its label
        hearts.append(test1)
        heartcount.append(HEART)

    for index in range(1, HAT_AMT + 1):
        curExt = "{}/{:02}.jpg".format(HAT_PATH,index)
        curPath = PATH + curExt
        test = mpimg.imread(curPath)
        test1 = np.array(test)
        test1 = np.sum(test, 2).flatten()
        hats.append(test1)
        hatcount.append(HAT)

    for index in range(1, HASH_AMT + 1):        
        curExt = "{}/{:02}.jpg".format(HASH_PATH,index)
        curPath = PATH + curExt
        test = mpimg.imread(curPath)
        test1 = np.array(test)
        test1 = np.sum(test, 2).flatten()
        hashs.append(test1)
        hashcount.append(HASH)

    for index in range(1, DOLLAR_AMT + 1):
        curExt = "{}/{:02}.jpg".format(DOLLAR_PATH,index)
        curPath = PATH + curExt
        test = mpimg.imread(curPath)
        test1 = np.array(test)
        test1 = np.sum(test, 2).flatten()
        dollars.append(test1)
        dollarcount.append(DOLLAR)

    for index in range(1, SMILE_AMT + 1):        
        curExt = "{}/{:02}.jpg".format(SMILE_PATH,index)
        curPath = PATH + curExt
        test = mpimg.imread(curPath)
        test1 = np.array(test)
        test1 = np.sum(test, 2).flatten()
        smiles.append(test1)
        smilecount.append(SMILE)
    
    # gets all of the data in one list
    data = hearts + hats + hashs + dollars + smiles
    # gets all the labels in one list
    labels = heartcount + hatcount + hashcount + dollarcount + smilecount
    # stores the object to be pickled
    myPickle = [data, labels]

    # pickles the data
    with open('data.pickle', 'wb') as f:
        pickle.dump(myPickle, f, pickle.HIGHEST_PROTOCOL)

main()
