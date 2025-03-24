import requests
import re
url='https://www.weather.com.cn/weather1d/101250905.shtml'
response = requests.get(url)
response.encoding='utf-8'
print(response.text)
city=re.findall('<span class="name">([\u4e00-\u9fa5]*)</span>',response.text)
weather=re.findall('<span class="weather">([\u4e00-\u9fa5]*)</span>',response.text)
wd=re.findall('<span class="wd">(.*)</span>',response.text)
zs=re.findall('<span class="zs">([\u4e00-\u9fa5]*)</span>',response.text)


# print(city)
# print(weather)
# print(wd)
# print(zs)

lst=[city,weather,wd,zs]
for a,b,c,d in zip(city,weather,wd,zs):
    lst.append([a,b,c,d])
print(lst)
print('-'*40)
for item in lst:
    print(item)
print('-'*40)
'''
<span class="name">三亚</span>
<span class="weather">多云</span>
<span class="wd">30/19℃</span>
<span class="zs">适宜</span>


'''