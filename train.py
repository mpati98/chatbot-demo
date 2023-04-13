# Importing Libraries
import numpy as np
from flask import Flask,jsonify,request
from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score,classification_report
from sklearn.linear_model import LogisticRegression
import pickle
import os
from flasgger import Swagger
import flasgger

def train_and_save_model():
    '''This function creates and saves a Binary Logistic Regression
    Classifier in the current working directory
    named as LogisticRegression.pkl
    '''
    ## Creating Dummy Data for Classificaton from sklearn.make_classification
    ## n_samples = number of rows/number of samples
    ## n_features = number of total features
    ## n_classes = number of classes - two in case of binary classifier
    X,y = make_classification(n_samples = 1000,n_features = 4,n_classes = 2)
    ## Train Test Split for evaluation of data - 20% stratified test split
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.20, random_state=42,stratify=y)
    ## Building Model
    logistic_regression = LogisticRegression(random_state=42)
    ## Training the Model
    logistic_regression.fit(X_train,y_train)
    ## Getting Predictions
    predictions = logistic_regression.predict(X_test)
    ## Analyzing valuation Metrics
    print("Accuracy Score of Model : "+str(accuracy_score(y_test,predictions)))
    print("Classification Report : ")
    print(str(classification_report(y_test,predictions)))
    ## Saving Model in pickle format
    ## Exports a pickle file named Logisitc Regrssion in current working directory
    output_path = os.getcwd()
    file_name = '/LogisticRegression.pkl'
    output  = open(output_path+file_name,'wb')
    pickle.dump(logistic_regression,output)
    output.close()

train_and_save_model()