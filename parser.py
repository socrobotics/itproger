import requests
from bs4 import BeautifulSoup as bs4

headers = {
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.1 Safari/605.1.15'
}

url = 'https://socrobotic.io'
session = requests.Session()
try:
    req = session.get(url, params=headers)
    if req.status_code == 200:
        soup = bs4(req.content, 'html.parser')
        print(soup)
    else:
        print('Ошибка')
except Exception:
    print('Ошибка в самом URL адресе')