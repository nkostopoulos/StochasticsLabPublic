import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression

datas = pd.read_csv('data2.csv')

X = datas.iloc[:, 1:2].values
y = datas.iloc[:, 2].values

lin = LinearRegression()
lin.fit(X, y)

poly = PolynomialFeatures(degree=2)
X_poly = poly.fit_transform(X)
poly.fit(X_poly, y)
lin2 = LinearRegression()
lin2.fit(X_poly, y)

plt.scatter(X, y, color = 'blue')

plt.plot(X, lin.predict(X), color = 'red')
plt.plot(X, lin2.predict(poly.fit_transform(X)), color = 'green')
plt.show()


