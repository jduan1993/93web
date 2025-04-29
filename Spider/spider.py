import requests
import socket
from ast import literal_eval
from urllib import request, error, parse
from bs4 import BeautifulSoup

'''
代理服务器类：Proxy
get_proxy(type), test(proxy, type)
网络爬虫类：WebSpider
get_html_results(url), get_json_results(url)
'''

# 请求头
headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/84.0.4147.125 Safari/537.36',
    'cookie': '__cfduid = d3682c6df9b78f81f050a557a328625ae1598318496;_ga = GA1.2.1603310247.1598318500;_gid = '
              'GA1.2.115911572.1598423146',
    'referer': 'https://cn.bing.com/'
}


class Proxy:
    def __init__(self):
        # IP地址来源
        self.proxy_url = 'http://www.xiladaili.com/'
        self.test_url = 'https://www.bing.com/'
        self.timeout = 5

    # 爬取代理 IP 地址
    def get_proxy(self, proxy_type):
        proxy_req = request.Request(url=self.proxy_url, headers=headers)
        proxy_res = request.urlopen(proxy_req).read()
        soup = BeautifulSoup(proxy_res, 'lxml')

        html_results = soup.find_all('table', attrs={'class': 'fl-table'})
        for hr in html_results:
            html_tr = hr.find_all('tr')
            for htr in html_tr:
                if len(htr.find_all('td')) > 5 or len(htr.find_all('tr')) > 5:
                    proxy = htr.find_all('td')[0].get_text()
                    transfer_type = htr.find_all('td')[2].get_text().split(',')
                    resp_speed = htr.find_all('td')[4].get_text()
                    if proxy_type in transfer_type and float(resp_speed) > 3:
                        if self.test(proxy, proxy_type):
                            return proxy
                        else:
                            continue
        host_name = socket.gethostname()
        return socket.gethostbyname(host_name)

    # 测试 IP 地址
    def test(self, proxy, proxy_type):
        try:
            requests.get(url=self.test_url, headers=headers, timeout=self.timeout, proxies={proxy_type: proxy})
        except RuntimeError:
            return False
        else:
            return True



class WebSpider:
    def __init__(self):
        # 代理
        self.proxy_switch = False
        if self.proxy_switch:
            self.proxy = {'http': Proxy().get_proxy('HTTP'), 'https': Proxy().get_proxy('HTTPS')}

    # 爬取网站 HTML 信息 （上海市文旅推广网）
    def get_html_results(self, html_url):
        req = request.Request(url=html_url, headers=headers)
        if self.proxy_switch:
            try:
                proxy_handler = request.ProxyHandler(self.proxy)
                opener = request.build_opener(proxy_handler)
                res = opener.open(req)
            except error.URLError:
                res = request.urlopen(req)
        else:
            res = request.urlopen(req)

        soup = BeautifulSoup(res, 'lxml')

        try:
            return soup.find('p', attrs={'class': 'p_piclist_tit2'}).text
        except AttributeError:
            pass

    # 爬取网站 JSON 信息 （上海市文旅局）
    def get_json_results(self, json_url):
        if self.proxy_switch:
            try:
                res = requests.get(url=json_url, headers=headers, roxies=self.proxy)
            except error.URLError:
                res = requests.get(url=json_url, headers=headers)
        else:
            res = requests.get(url=json_url, headers=headers)

        str_left = res.text.find('"')
        str_right = res.text.find('"', str_left + 1)
        dict_str = res.text[str_left + 1:str_right]
        return literal_eval(dict_str)


if __name__ == '__main__':
    # 网站测试源
    # url = 'http://lysh.eastday.com/lyj/Scenic_A/map/index.html?type=9'
    word = parse.quote('上海科技馆')
    url = 'http://chs.meet-in-shanghai.net/others/advancedsearch.php?sel=1&placename=%s' % word
    print(url)
    # JSON 测试源
    json_src = 'http://61.152.117.25/SqlHelper/passenger/PassengerInfo.asmx/QueryRealtimeInfo?&username=dfw&password' \
               '=eastday&district=0'

    print('HTTP代理为：' + Proxy().get_proxy('HTTP'))
    print('HTTPS代理为：' + Proxy().get_proxy('HTTPS'))

    print(WebSpider().get_html_results(url))
    print(WebSpider().get_json_results(json_src))
