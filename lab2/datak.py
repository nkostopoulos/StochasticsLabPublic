from pylab import plot,show
from numpy import vstack,array
from numpy.random import rand
import numpy as np
from scipy.cluster.vq import kmeans,vq
import pandas as pd
import pandas_datareader as dr
from math import sqrt
from sklearn.cluster import KMeans
from matplotlib import pyplot as plt
 
 
sp500_url = 'https://en.wikipedia.org/wiki/List_of_S%26P_500_companies'
 
#read in the url and scrape ticker data
data_table = pd.read_html(sp500_url)
 
tickers = data_table[0][1:][0].tolist()
prices_list = []
for ticker in tickers:
    try:
        prices = dr.DataReader(ticker,'yahoo','01/01/2017')['Adj Close']
        prices = pd.DataFrame(prices)
        prices.columns = [ticker]
        prices_list.append(prices)
    except:
        pass
    prices_df = pd.concat(prices_list,axis=1)
 
prices_df.sort_index(inplace=True)
 
prices_df.head()
