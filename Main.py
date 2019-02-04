import datetime as dt
import matplotlib.pyplot as plt
from matplotlib import style
import pandas as pd
import pandas_datareader.data as web
import quandl




start = dt.datetime(2019,1, 28)
end = dt.datetime.now()


df = web.DataReader('TSLA', 'iex', start, end)
print(df.head())
