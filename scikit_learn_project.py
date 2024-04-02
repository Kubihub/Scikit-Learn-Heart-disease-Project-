# -*- coding: utf-8 -*-
"""scikit_learn_project

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/17SJbAjvrDEoXS0r6mYnTxyhqYGjeigMI

What I am covering this tutorial
  
  0. An end-to-end Scikit-learn workflow
  1. Getting to data ready
  2. Choose the right estimato/algorithm for our problems
  3. Fit the model/algorithm and use it to make predictions on our data
  4. Evaluating a model
  5. Improve a model
  6. Save and load a trained model
  7. Putting it all together

## 0. An end-to-end Scikit-learn workflow
"""

import numpy as np

#1. Get the data ready
import pandas as pd
heart_disease = pd.read_csv('/content/heart-disease.csv')
heart_disease

# Create x (features matix)

X = heart_disease.drop("target", axis=1)

# Create y (lables)
y = heart_disease["target"]

# 2. Choose the right model and hyperparameters
# The RandomForestClassifier is for classification machine learning model

from sklearn.ensemble import RandomForestClassifier
clf = RandomForestClassifier(n_estimators=100)

#We'll keep the default hyperparameters
clf.get_params()

# 3. Fit the model to the data
from sklearn.model_selection import train_test_split

x_train, x_test,y_train, y_test = train_test_split(X,y,test_size=0.2)

clf.fit(x_train, y_train)

# Make a prediction
y_preds = clf.predict(x_test)
y_preds



# Make a prediction
# y_label = clf.predict(np.array([0,2,3,4]))

# Make a prediction
y_preds = clf.predict(x_test)
y_preds

y_test

# 4. Evaluate the model on the training data and test data
clf.score(x_train, y_train)

clf.score(x_test, y_test)

from sklearn.metrics import classification_report, confusion_matrix,accuracy_score

print(classification_report(y_test, y_preds))

confusion_matrix(y_test, y_preds)

accuracy_score(y_test, y_preds)

# 5. Improve a model
# Try different amount of n_estimators

np.random.seed(42)
for i in range(10,100,10):
  print(f"Trying model with {i} estimators..")
  clf = RandomForestClassifier(n_estimators=i).fit(x_train, y_train)
  print(f"Model accuracy on test set: {clf.score(x_test, y_test) *100:.2f}")
  print("")

  #from the accuracy we can say that we can use 60,70,80 estimators

# 6. Save a model and load it
import pickle

pickle.dump(clf, open("Heart_disease_randomForest_model", "wb"))

loaded_model = pickle.load(open("Heart_disease_randomForest_model", "rb"))
loaded_model.score(x_test,y_test)