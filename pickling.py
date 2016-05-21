# Jeremy Aguillon
# CMSC 471
# Description: short file to pickle the data to make it easier to acces.
#              Only need to run once.

import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np
from sklearn.neighbors import KNeighborsClassifier

from sklearn import datasets, svm, metrics

import pickle

PATH = "./training"
HEART_PATH = "/00"
HAT_PATH = "/01"
HASH_PATH = "/02"
DOLLAR_PATH = "/03"
SMILE_PATH = "/04"

HEART = 0
HAT = 1
HASH = 2
DOLLAR = 3
SMILE = 4

IMG_TYPE = ["heart","hat","hash","dollar","smile"]

HEART_AMT = 81
HAT_AMT = 72
HASH_AMT = 88
DOLLAR_AMT = 87
SMILE_AMT = 85

def main():
    
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
    
    #path = "./Data/training/"
    for index in range(1, HEART_AMT + 1):
        curExt = "{}/{:02}.jpg".format(HEART_PATH,index)
        curPath = PATH + curExt
        test = mpimg.imread(curPath)
        test1 = np.array(test)
        test1 = np.sum(test, 2).flatten()
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
    
    data = hearts + hats + hashs + dollars + smiles
    labels = heartcount + hatcount + hashcount + dollarcount + smilecount

    myPickle = [data, labels]

    with open('data.pickle', 'wb') as f:
        # Pickle the 'data' dictionary using the highest protocol available.
        pickle.dump(myPickle, f, pickle.HIGHEST_PROTOCOL)

main()
