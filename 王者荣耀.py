import requests
import json
import csv
from lxml import html
def get_hero():
    #请求信息
    skin = 'https://game.gtimg.cn/images/yxzj/img201606/skin/hero-info/{}/{}-bigskin-1.jpg'
    url = 'https://pvp.qq.com/web201605/js/herolist.json'
url = 'https://pvp.qq.com/web201605/herolist.shtml'
header = {
    'user-agent':' Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36 Edg/106.0.1370.52'
}
response = requests.get(url,headers = header)
    res = response.text
    # print(res)
    #使用json模块
    info = json.loads(res)
    for he in info:
        ename = he['ename']
        cname = he['cname']
        img = skin.format(ename,ename)
        print(ename,cname,img)
    pass
# get_hero()

def get_hero2():
    url = 'https://pvp.qq.com/web201605/herolist.shtml'
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36'
    }
    # 请求网页
    response = requests.get(url, headers=headers)
    response.encoding = 'gbk'
    res = response.text
    #转化对象
    page = html.etree.HTML(res)
    hero_li = page.xpath('//ul[@class="herolist clearfix"]/li')
    for item in hero_li:
        name = item.xpath('.//img/@alt')[0]
        img = item.xpath('.//img/@src')[0]
        'https://game.gtimg.cn/images/yxzj/img201606/heroimg/110/110.jpg'
        'https://game.gtimg.cn/images/yxzj/img201606/skin/hero-info/110/110-bigskin-1.jpg'
        #小头像
        a = 'https:' + img
        #皮肤
        b = a.replace('/heroimg/','/skin/hero-info/').replace('.jpg','-bigskin-1.jpg')
        print(name,b)
    pass
get_hero2()

