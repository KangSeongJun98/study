import requests
import json

page = 1
size = 20
url = f'https://m.stock.naver.com/api/stocks/marketValue/KOSPI?page={page}&pageSize={size}'
res = requests.get(url)
jsonObj = json.loads(res.text)
arr = jsonObj['stocks']
for row in arr:
    print(row['itemCode'], row['stockName'], row['closePrice'])