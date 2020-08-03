import time

import requests
from bs4 import BeautifulSoup


# pip install bs4
# pip install lxml

def whilee():
    try:
        dta = []

        def get_html(site):
            r = requests.get(site)
            return r.text

        def get_page_data(html):
            soup = BeautifulSoup(html, 'lxml')
            line = soup.find('table', id='theProxyList').find('tbody').find_all('tr')

            for tr in line:
                td = tr.find_all('td')
                ip = td[1].text
                port = td[2].text

                data = str(ip + ":" + port)
                dta.append(data)

        def main():
            try:
                with open('proxy.txt', 'w') as fa:
                    fa.write('')
                for ul in range(1, 7):
                    url = 'http://foxtools.ru/Proxy?al=False&am=False&ah=False&ahs=True&http=True&https=False&pf=80&pt=80&page=' + str(
                        ul)
                    get_page_data(get_html(url))


            except Exception as errorsite:
                print(errorsite)

        if __name__ == '__main__':
            main()

        proxy_list = dta

        def get_proxy():
            for index, proxy in enumerate(proxy_list):
                url = 'http://' + proxy
                try:
                    r = requests.get('https://ya.ru', proxies={'http': url})
                    if r.status_code == 200:
                        print(index + 1, ">>", proxy)
                    with open('proxy.txt', 'a') as f:
                        f.write(proxy + "\n")
                except requests.exceptions.ConnectionError:
                    continue

        get_proxy()
    except Exception as error:
        print(error)


while True:
    whilee()
    time.sleep(600)
