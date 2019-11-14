# import tushare as ts
# import datetime
#
# df_sh = ts.get_hist_data('sh', start='2017-01-01', end=datetime.datetime.now().strftime('%Y-%m-%d'))
#
# print(df_sh.info())

# import pandas_datareader.data as web
# import datetime
#
# # 获取上证指数的2017.1.1日至今的交易数据
# df_stockload = web.DataReader("000001.SS", "yahoo", datetime.datetime(2017, 1, 1), datetime.date.today())
#
# # 查看前几行
# print(df_stockload.head())
