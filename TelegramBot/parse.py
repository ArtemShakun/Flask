import requests
from bs4 import BeautifulSoup
from random import choice


def get_proxy():
    html = requests.get('https://free-proxy-list.net/').text
    soup = BeautifulSoup(html, 'lxml')
    trs = soup.find('table', id='proxylisttable').find_all('tr')[1:16]

    proxies = []

    for tr in trs:
        tds = tr.find_all('td')
        ip = tds[0].text.strip()
        port = tds[1].text.strip()
        schema = 'https' if 'yes' in tds[6].text.strip() else 'http'
        proxy = {'schema':schema, 'address':ip + ':' + port}
        proxies.append(proxy)
    return choice(proxies)

def get_date():
    p = get_proxy()
    proxy = { p['schema']:p['address'] }
    url = 'https://weather.i.ua/Chernigov/'
    html = requests.get(url).text
    soup = BeautifulSoup(html, 'lxml')
    first = soup.find('div', {'class':"widget-weather_summary"}).find_all('ul', {'class':'summary'})
    for i in first:
        tm = i.find('li', {'class':'summary_item'}).find('span', {'class':'icon-xl'}).text

    resalt = 'Сейчас в Чернигове: ' + tm
    return resalt
