from bs4 import BeautifulSoup
import requests
import numba


def crawl_proxies():
    proxies=[]
    link = 'https://www.sslproxies.org/'

    r = requests.det(link)
    s = BeautifulSoup(r.text, 'html.parser')
    for i in s.find_all('tr')[:30]:
        try:
            data = i.find_all('td')
            adress = data[0].text
            port = data[1].text
            type_ = data[4].text
            proxy = address + ':' + port
            proxies.append({'https':proxy})

        except:
            pass

        return proxies

    proxies = crawl_proxies()
    pront(proxies)