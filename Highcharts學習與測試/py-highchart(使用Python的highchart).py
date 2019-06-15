# -*- coding: UTF-8 -*-
from highcharts import Highchart
from FinMind.Mining import Mind
import pandas as pd
import datetime

#_2330 = Mind.Stock('2330','2019-01-01')
#StockPrice=_2330.StockPrice
#close=StockPrice.drop(labels=['Trading_Volume','Trading_money','open','max','min','spread','Trading_turnover','stock_id','update_time','create_time','country'],axis=1)
#close.to_json('2330.json')

chart = Highchart()

chart.set_options('chart', {'inverted': False})

options = {
    'title': {
        'text': '台積電股價'
    },
    'subtitle': {
        'text': '使用FinMind'
    },
    'xAxis': {
        'reversed': False,
        'title': {
            'enabled': True,
            'text': '日期'
        },
        'labels': {
            'formatter': 'function () {\
                return this.value;\
            }'
        },
        'maxPadding': 0.05,
        'showLastLabel': True
    },
    'yAxis': {
        'title': {
            'text': '股價'
        },
        'labels': {
            'formatter': "function () {\
                return this.value;\
            }"
        },
        'lineWidth': 2
    },
    'legend': {
        'enabled': False
    },
    'tooltip': {
        'headerFormat': '<b>{series.name}</b><br/>',
        'pointFormat': '{point.x} : {point.y}元'
    }
}

chart.set_dict_options(options)


data=[[1546387200000,219.5],
    [1546473600000,215.5],
    [1546560000000,208.0],
    [1546819200000,213.0],
    [1546905600000,211.0],
    [1546992000000,215.5],
    [1547078400000,216.0],
    [1547164800000,220.5],
    [1547424000000,218.5],
    [1547510400000,221.0],
    [1547596800000,217.5],
    [1547683200000,220.5],
    [1547769600000,218.5],
    [1548028800000,221.0],
    [1548115200000,223.0],
    [1548201600000,220.5],
    [1548288000000,222.5],
    [1548374400000,226.0],
    [1548633600000,229.0],
    [1548720000000,222.5],
    [1548806400000,221.0],
    [1549843200000,228.0],
    [1549929600000,230.0],
    [1550016000000,229.0],
    [1550102400000,227.0],
    [1550188800000,227.0],
    [1550448000000,230.0],
    [1550534400000,229.0],
    [1550620800000,234.5],
    [1550707200000,236.5],
    [1550793600000,236.5],
    [1551052800000,238.0],
    [1551139200000,239.5],
    [1551225600000,239.0],
    [1551657600000,235.5],
    [1551744000000,233.0],
    [1551830400000,234.0],
    [1551916800000,234.0],
    [1552003200000,230.0],
    [1552262400000,230.5],
    [1552348800000,235.5],
    [1552435200000,237.0],
    [1552521600000,234.5],
    [1552608000000,239.0],
    [1552867200000,241.0],
    [1552953600000,240.5],
    [1553040000000,242.0],
    [1553126400000,245.5],
    [1553212800000,248.5],
    [1553472000000,241.5],
    [1553558400000,244.0],
    [1553644800000,241.5],
    [1553731200000,242.0],
    [1553817600000,245.5],
    [1554076800000,245.5],
    [1554163200000,246.0],
    [1554249600000,246.5],
    [1554681600000,253.0],
    [1554768000000,254.0],
    [1554854400000,254.0],
    [1554940800000,252.0],
    [1555027200000,252.0],
    [1555286400000,255.5],
    [1555372800000,257.0],
    [1555459200000,261.5],
    [1555545600000,264.5],
    [1555632000000,264.5],
    [1555891200000,266.0],
    [1555977600000,268.0],
    [1556064000000,269.0],
    [1556150400000,267.5],
    [1556236800000,260.0],
    [1556496000000,259.5],
    [1556582400000,259.0],
    [1556755200000,259.0],
    [1556841600000,265.0],
    [1557100800000,259.0],
    [1557187200000,262.5],
    [1557273600000,260.0],
    [1557360000000,256.5],
    [1557446400000,256.0],
    [1557705600000,250.5],
    [1557792000000,248.5],
    [1557878400000,249.0],
    [1557964800000,247.0],
    [1558051200000,241.5],
    [1558310400000,238.0],
    [1558396800000,234.0],
    [1558483200000,238.0],
    [1558569600000,230.0],
    [1558656000000,233.0],
    [1558915200000,231.0],
    [1559001600000,230.5],
    [1559088000000,229.5],
    [1559174400000,231.0],
    [1559260800000,235.5],
    [1559520000000,238.0],
    [1559606400000,233.0],
    [1559692800000,235.0],
    [1559779200000,232.0],
    [1560124800000,240.0],
    [1560211200000,244.5],
    [1560297600000,246.0],
    [1560384000000,240.0],
    [1560470400000,236.0]
]


chart.add_data_set(data,'line','股價',tooltip = {
    'valueDecimals': 2
    }) 

chart.save_file()