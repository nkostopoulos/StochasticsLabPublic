import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model.logistic import LogisticRegression

# Load the csv file into a dataframe
#df = pd.read_csv("demo3a.csv")
df = pd.read_csv("foo.csv")

# Separate the input features from the target variable
x = df.iloc[:,1:13].values
y = df.iloc[:,0].values

# Split the dataset into train and test set
Xtrain,Xtest,Ytrain,Ytest = train_test_split(x,y, test_size = 0.2)

# Fit the data into a Logistic Regression model
classifier = LogisticRegression(max_iter = 1000)
classifier.fit(Xtrain,Ytrain)

# Get the predictions on the test set
prediction = classifier.predict(Xtest)

# Calculate the total number of errors on the test set
errors = 0
for index in range(0,len(prediction) - 1):
	if prediction[index] != Ytest[index]:
		errors += 1

print()
print("Total errors on the test dataset")
print(errors)
