# Jeremy Aguillon
# CMSC 471 
# Project 3 executable

# imports sys for command line arguments (argv)
import sys
# to featurize the image
import matplotlib.image as mpimg
# numpy import
import numpy as np
# pickle import
import pickle
# scikitlearn imports
from sklearn.neighbors import KNeighborsClassifier
from sklearn import datasets, svm, metrics
from sklearn.cross_validation import train_test_split

## Constants ##
DATA = 0
LABELS = 1
PATH = 1
NAMES = ["Heart","Hat","Hash","Dollar","Smile"]

# main function
def main(argv):

    if len(argv) != 2:
        print("Invalid input\nUsage: python classify.py <path to image>")
    else:
        # gets the pickle data file and imports the data
        with open('data.pickle', 'rb') as myfile:
            pickleData = pickle.load(myfile)

        # retrieves the pickled data
        data = pickleData[DATA]
        labels = pickleData[LABELS]
    
        # stores the data for the matrix
        X = data
        y = labels
    
        # splits the data into a training and test set
        X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=2)

        # creating k nearest neighbor
        kneigh = KNeighborsClassifier(n_neighbors=5)
        # fits the given data
        kneigh.fit(X_train, y_train)

        # featurizes the given path to an image
        curPath = argv[PATH]
        test = mpimg.imread(curPath)
        test1 = np.array(test)
        test1 = np.sum(test, 2).flatten()
        test1 = test1.reshape(1,-1)
        
        # prints out the prediction for the image
        print(NAMES[kneigh.predict(test1)[0]])

# call to main
main(sys.argv)
