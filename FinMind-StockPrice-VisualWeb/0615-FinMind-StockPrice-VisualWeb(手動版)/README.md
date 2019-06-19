# 使用FinMind和Highcharts進行股價視覺化

https://medium.com/@yanweiliu/%E4%BD%BF%E7%94%A8finmind%E5%92%8Chighcharts%E9%80%B2%E8%A1%8C%E8%82%A1%E5%83%B9%E8%A6%96%E8%A6%BA%E5%8C%96-2a59ad4c1740?postPublishedType=initial

- 20190615-FinMind_get_2330-StockPrice.ipynb為抓取股價的程式

- result資料夾中有stock.html(為產生的靜態網頁)、index.PNG為視覺化成果圖片

- data資料夾中有csv和json檔及date_json.py(可以將csv轉成適合Highcharts的程式)

> 本文建議有 Python,HTML,CSS,JavaScript基礎的人閱讀

> **流程**

```
1.透過FinMind把股票資料抓下來
2.使用CSDN上一位大神寫的程式(把CSV轉成符合Highcharts要求的JSON檔案)
3.建立靜態網頁(HTML+JavaScript)佈署
```

------

### 透過FinMind把股票資料抓下來

```
from FinMind.Mining import Mind
import pandas as pd
pd.set_option("display.max_rows", 1000)    #設定最大能顯示1000rows
pd.set_option("display.max_columns", 1000) #設定最大能顯示1000columns
_2330 = Mind.Stock('2330','2019-01-01')    #台積電代號2330
StockPrice=_2330.StockPrice                #抓取股價
close=StockPrice.drop(labels=['Trading_Volume','Trading_money','open','max','min','spread','Trading_turnover','stock_id','update_time','create_time','country'],axis=1)   #只保留日期和收盤價格
close.plot(x='date',y='close')             #用pandas進行視覺化
close = close.set_index("date", drop=True) #調整index
close.to_csv('2330.csv')                   #存到CSV檔案
```

### 把CSV轉成符合Highcharts要求的JSON檔案

```
import os, sys
import time
import json
 
if len(sys.argv) ==2:
    f1 = sys.argv[1]
else:
    print('usage: date_json.py fcode.csv ')
    sys.exit(1)
 
if not os.path.exists(f1):
    print("Error: %s not found." % f1)
    sys.exit(1)
 
fn,ext = os.path.splitext(f1)
if len(fn) !=4:            #依照csv檔名的長度進行調整，2330.csv，就填4
    print('Error: len(%s) !=6' % fn)
    sys.exit(1)
if ext !='.csv':
    print('Error: %s is not .csv' % f1)
    sys.exit(1)
 
fp = open(f1,'r')
fp.readline()
 
f2 = fn +'.json'
fp2 = open(f2,'w')
fp2.write('{"code":1,"msg":"OK","data":')
ts=0  # timestamp
jz = float('0.0')
alist =[]
for line in fp:
    date,jz,lljz = line.strip().split(',')
    #%Y/%m/%d必須依照CSV裡的date欄位進行調整，也有可能是#%Y-%m-%d
    time1 = time.strptime(date, "%Y/%m/%d")  
    ts = int(time.mktime(time1))*1000
    jz = float(jz)
    alist.append([ts,jz])
#
json.dump(alist,fp2)
fp2.write('}')
fp2.close()
fp.close()
------------------------------------------------------------------
#開啟CMD，切換到檔案目錄中
#python date_json.py 2330.csv
#正常執行後，會產生2330.json
```

### 建立靜態網站

```
<!DOCTYPE html>
<html>
<head>
        <meta charset="utf-8">
        <meta name="viewport" content="width=device-width, initial-scale=1">
<style>
  .highcharts-axis-resizer {
 stroke: #eee;
  }
  .highcharts-axis-resizer:hover {
 stroke: #ccc;
  }
</style>
        <script src="https://img.highcharts.com.cn/jquery/jquery-1.8.3.min.js"></script>
        <script src="https://img.highcharts.com.cn/highstock/highstock.js"></script>
        <script src="https://img.highcharts.com.cn/highcharts/modules/exporting.js"></script>
        <script src="https://img.highcharts.com.cn/highcharts-plugins/highcharts-zh_CN.js"></script>
        <script src="https://img.highcharts.com.cn/highcharts/themes/grid-light.js"></script>
</head>
<body>
        <div id="container" style="min-width:400px;height:400px"></div>     #min-width:400px;height:400px請依需求調整
<script>
#取得本地端JSON資料，就是上一步驟產生的json檔
$.getJSON('2330.json', function (data) {
    if(data.code !== 1) {
        alert('讀取數據失敗!');
        return false;
    }
    data = data.data;
    Highcharts.setOptions({ global: { useUTC: false } });
    Highcharts.each(data, function(d) {
        d.length = 2;
    });
    Highcharts.stockChart('container', {
        rangeSelector: {
            selected: 2
        },
        title: {
            text: '2330股票價格'
        },
        plotOptions: {
            series: {
                showInLegend: true
            }
        },
        tooltip: {
            split: false,
            shared: true
        },
        series: [{
            // type: 'line',
            id: '2330',
            name: '股價',
            data: data
        }]
    });
});
 
</script>
</body>
</html>
```