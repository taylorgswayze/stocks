import csv
import time
import requests
import json


api_rows = []
with open('30DayByMinute.csv') as file:
    csv_reader = csv.reader(file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        api_rows.append(str(row).strip("['").strip("']"))
        line_count += 1

    for url in api_rows:
        data = requests.get(url).json()
        time.sleep(.2)
        print()



tickers = [‘AAPL','ABT','ABX','AES','AIG','AKS','AMAT','AMD','ATVI','AUY','AVP','AXP','BA','BAC','BB','BBD','BILI','BK','BRK.B','BSX','BVN','C','CAG','CAT','CE','CHK','COP','CSCO','CTL','CVS','CVX','DIS','DNR','DVN','DWDP','ECA','ERIC','ESV','F','FB','FCX','GE','GFI','GG','GM','GNW','GS','HAL','HD','HMNY','HPE','HPQ','IBM','INFY','INTC','JNJ','JPM','KEY','KGC','KO','LYG','MCD','MGM','MMM','MO','MRIN','MRK','MRO','MS','MSFT','MU','NBR','NEM','NKE','NLST','NLY','NOK','NVDA','ORCL','PBR','PFE','PG','PM','PPL','QCOM','RAD','RF','RIG','S','SLB','SMCI','SNAP','SQ','SWN','SYMC','T','TRV','TSM','TWTR','TXN','UNH','USB','UTX','V','VALE','VZ','WBA','WFC','WFT','WMB','WMT','WY','XOM','ZNGA’]