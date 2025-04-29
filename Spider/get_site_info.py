from urllib import parse

import spider
import mysql.connector

ws = spider.WebSpider()
db = mysql.connector.connect(host='localhost', user='93web', password='firstwebsite1', database='93web')
c = db.cursor()

site_url = 'http://61.152.117.25/SqlHelper/passenger/PassengerInfo.asmx/QueryRealtimeInfo?&username=dfw&password' \
           '=eastday&district=0'
for s in ws.get_json_results(site_url)['Rows']:
    search_str = s['NAME']
    word = parse.quote(search_str)
    search_url = 'http://chs.meet-in-shanghai.net/others/advancedsearch.php?sel=1&placename=%s' % word
    address = ws.get_html_results(search_url)
    if address:
        print(address)
        start = address.find("：")
        add_str = address[start+1:]
        print(add_str)
        end_1 = add_str.find("市")
        province = city = add_str[0:end_1+1]
        print(province)
        print(city)
        end_2 = add_str.find("区")
        district = add_str[end_1+1:end_2+1]
        print(district)
        add = add_str[end_2+1:]
        print(add)
        sql = 'INSERT INTO 93web.address_info(site_name, province, city, district, address) VALUES(%s, %s, %s, %s, %s)'
        val = (search_str, province, city, district, add)
    else:
        print(search_str)
        sql = 'INSERT INTO 93web.address_info(site_name, address) VALUES(%s, %s)'
        val = (search_str, '')
    c.execute(sql, val)
    db.commit()
    c = db.cursor()
    db.close()