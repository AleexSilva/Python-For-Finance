import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import pandas_datareader as pdr
import datetime as dt

def new_func(ticker):
    start = dt.datetime(2020,1,1)
    aapl = pdr.get_data_yahoo(ticker, start)
    return aapl

aapl=new_func('AAPL')

aapl.head()
