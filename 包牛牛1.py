import requests
import urllib.parse
from lxml import html
for a in range(5):
    url = 'http://www.bao66.cn/web/'
header = {
'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36'
}
response = requests.get(url,headers=header)
response.encoding = 'utf-8'
# 获取网页源码
info = response.text
print(info)
hhh = html.etree.HTML(response.text)
res = hhh.xpath('//ul[@class="product_box"]')
for a in res[0]:
    name = a.xpath('.//div/p/@title')
    img = a.xpath('.//p[@class="code"]/a/text()')
    jg = a.xpath('.//p[@class="desc_hover"]//b/text()')
    print(name,img,jg)