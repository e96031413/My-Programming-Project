

from highcharts import Highstock
#from highcharts.highstock.highstock_helper import jsonp_loader
import pandas as pd
import os
import datetime 
from FinMind.Data import Load

os.chdir(r'C:\Users\Yanwei\Desktop')

def date2millisecond(date):
    
    if isinstance(date,pd.core.series.Series):
        date = [ datetime.datetime.combine(x, datetime.datetime.min.time()) 
                for x in date ]
        date = [ d + datetime.timedelta(minutes = 1) for d in date ]
        second = [ d - datetime.datetime(1970,1,1,0,0,0) for d in date ]
        second = [ (s.days*24*60*60+s.seconds)*1000 for s in second ] 

    else:
        if isinstance(date,str):
            date = datetime.datetime.strptime(date,'%Y-%m-%d %H:%M:%S')
        elif isinstance(date,datetime.date):
            date = datetime.datetime.combine(date, datetime.datetime.min.time() )
        date = date + datetime.timedelta(minutes = 1)
        second = date - datetime.datetime(1970,1,1,0,0,0)    
        second = (second.days*24*60*60+second.seconds)*1000

    return second

chart = Highstock()

data = Load.FinData(dataset = 'TaiwanStockPrice',
                    select = '2330',date = '2018-10-10')

print(' change type of dataframe to highcharts ')
data['date'] = date2millisecond(data['date'])
list_data = []
for i in range(len(data)):
    tem = [ int(data.loc[i,'date']),float(data.loc[i,'max']),float(data.loc[i,'min']) ]
    list_data.append(tem)

chart.add_data_set(list_data, 'arearange', 'Temperatures')

options = {
    'rangeSelector' : {
        'selected' : 2
    },

    'title' : {
        'text' : 'Temperature variation by day'
    },

}

chart.set_dict_options(options)
# This will generate and save a .html file at the location you assign
chart.save_file()


