import pandas_datareader.data as web
import datetime

# 获取上证指数的2017.1.1日至今的交易数据
df = web.DataReader("000001.SS", "yahoo", datetime.datetime(2017, 1, 1), datetime.date.today())

# 查看前几行
print(df.head())
