import urllib3
import re
import pandas
import numpy as np

http = urllib3.PoolManager()

pages = 4
conts = []

for page in range(1, pages + 1):
    url = "http://nufm.dfcfw.com/EM_Finance2014NumericApplication/JS.aspx?cb=jQuery1124012582582823807198_1554554782636&type=CT&token=4f1862fc3b5e77c150a2b985b12db0fd&sty=FPGBKI&js=({data:[(x)],recordsFiltered:(tot)})&cmd=C._BKHY&st=(ChangePercent)&sr=-1&p=%d"
    url += "&ps=20&_1554554783027"
    try:
        res = http.request('GET', url)
        pattern = re.compile(r'BK(.*?)"')
        list = re.findall(pattern, res.data.decode())
        for i in list:
            conts.append(i)
        print(dir(list))
    except Exception as e:
        print(e)

df = pandas.DataFrame(np.zeros((len(conts), 7)),
                      columns=[u'板块名称', u'BK涨跌幅', u'总市值', u'换手率', u'涨跌家数', u'领涨股票', u'SK涨跌幅'])

for num, entity in enumerate(conts):
    entity = entity.split(',')
    df.loc[df.index[num], u'板块名称'] = entity[1]
    df.loc[df.index[num], u'BK涨跌幅'] = entity[2]
    df.loc[df.index[num], u'总市值'] = entity[3]
    df.loc[df.index[num], u'换手率'] = entity[4]
    df.loc[df.index[num], u'涨跌家数'] = entity[5]
    df.loc[df.index[num], u'领涨股票'] = entity[8]
    df.loc[df.index[num], u'SK涨跌幅'] = entity[10]

df.to_csv("table-bk.csv", columns=df.columns, index=True, encoding="utf-8")
