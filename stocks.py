import csv
import time
from datetime import date, timedelta
import requests
import json
from datetime import date, timedelta

def daterange(date1, date2):
    for n in range(int ((date2 - date1).days)+1):
        yield date1 + timedelta(n)

start_dt = date(2018, 12, 20)
end_dt = date(2018, 12, 21)

tickers = ['AAPL', 'ABT', 'ABX', 'AES', 'AIG', 'AKS', 'AMAT', 'AMD', 'ATVI', 'AUY', 'AVP', 'AXP', 'BA', 'BAC', 'BB', 'BBD', 'BILI', 'BK', 'BSX', 'BVN', 'C', 'CAG', 'CAT', 'CE', 'CHK', 'COP', 'CSCO', 'CTL', 'CVS', 'CVX', 'DIS', 'DNR', 'DVN', 'DWDP', 'ECA', 'ERIC', 'ESV', 'F', 'FB', 'FCX', 'GE', 'GFI', 'GG', 'GM', 'GNW', 'GS', 'HAL', 'HD', 'HMNY', 'HPE', 'HPQ', 'IBM', 'INFY', 'INTC', 'JNJ', 'JPM', 'KEY', 'KGC', 'KO', 'LYG', 'MCD', 'MGM', 'MMM', 'MO', 'MRIN', 'MRK', 'MRO', 'MS', 'MSFT', 'MU', 'NBR', 'NEM', 'NKE', 'NLST', 'NLY', 'NOK', 'NVDA', 'ORCL', 'PBR', 'PFE', 'PG', 'PM', 'PPL', 'QCOM', 'RAD', 'RF', 'RIG', 'S', 'SLB', 'SMCI', 'SNAP', 'SQ', 'SWN', 'SYMC', 'T', 'TRV', 'TSM', 'TWTR', 'TXN', 'UNH', 'USB', 'UTX', 'V', 'VALE', 'VZ', 'WBA', 'WFC', 'WFT', 'WMB', 'WMT', 'WY', 'XOM', 'ZNGA']

urllist = []
for i in tickers:
     for dt in daterange(start_dt, end_dt):
        url = 'https://api.iextrading.com/1.0/stock/' + i + '/chart/date/' + dt.strftime("%Y%m%d")
        urllist.append(url)

csv_columns=['date','minute','label','high','low','average','volume','notional','numberOfTrades','marketHigh','marketLow','marketAverage','marketAverage','marketVolume','marketNotional','marketNumberOfTrades','open','close','marketOpen','marketClose','changeOverTime','marketChangeOverTime']

for u in urllist:
    dataset = requests.get(u).json()
    with open('dataoutput.csv', 'w') as dataoutput:
        writer = csv.DictWriter(dataoutput, fieldnames=csv_columns)
        writer.writeheader()
        for data in dataset:
            writer.writerow(data)

print('success')