import datetime as dt
import matplotlib.pyplot as plt
from matplotlib import style
import pandas as pd
import pandas_datareader.data as web
import numpy as np


style.use('fivethirtyeight')

start = dt.datetime(2015,1,1)
end = dt.datetime.now()


df = web.DataReader("NVDA", "iex", start, end)




df.to_csv("NVDA.csv")

df.reset_index(inplace=True)
df.set_index("date", inplace=True)

#df = df.drop('symbol', axis=1)

print(df.tail())

pd.dataFrame


df['low'].plot()

plt.legend()
plt.show()
