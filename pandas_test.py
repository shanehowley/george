import datetime
import pandas
from pandas_datareader import data
import matplotlib.pyplot as plt
from matplotlib import style

style.use('fivethirtyeight')

start = datetime.datetime(2010, 1, 1)
end = datetime.datetime(2015, 8, 22)


df = data.DataReader("XOM", "yahoo", start, end)

df['High'].plot()
plt.legend()
plt.show()




print df.head()

