import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model.logistic import LogisticRegression
from sklearn.model_selection import train_test_split, cross_val_score

# load csv file
df  = ___

# split dataset
X_train_raw, X_test_raw, ____, ____ = train_test_split(______)

# vectorize data
vectorizer = ________
Xtrain = vectorizer.fit_transform(_______)

# fit Logistic Regression model
____
____

# calculate accurary based on test set
_________________________
