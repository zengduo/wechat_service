# -*- coding: utf-8 -*-
import requests
from pypinyin import lazy_pinyin


city = u'西安'

pinyin = lazy_pinyin(city)

pinyin = pinyin[0] + pinyin[1]


url = "http://www.pm25.in/api/querys/aqi_details.json?city={0}&token=4esfG6UEhGzNkbszfjAp".format(pinyin)

r = requests.get(url)

encoding = r.encoding

dict1 = r.json()

content = str()
# item['position_name'], item['pm2_5'], item['quality']
for item in ["{} {} {}\n".format(item['position_name'].encode('utf-8', "ignore"), item['pm2_5'], item['quality'].encode('utf-8', "ignore")) for item in sorted(dict1, key=lambda d: d['pm2_5']) if item['quality'] and item['position_name'] and item['pm2_5']]:
    content += item

print content

# for i in [item['position_name'] for item in sorted(dict1, key=lambda d: d['pm2_5']) if item['quality'] and item['position_name'] and item['pm2_5']]:
#     print i, i.encode(encoding, 'ignore')

