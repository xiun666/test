# 导包
import requests
from lxml import html
import csv
# 链接
url = 'https://ke.qq.com/course/list?mt=1001&st=2064'
# 请求头信息
headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36'
}
# 请求网页
response = requests.get(url,headers = headers)
# 指定编码格式
response.encoding = 'utf-8'
# 转化文档树对象
page1 = html.etree.HTML(response.text)
# 得到最后一页的页数
page_li = page1.xpath('//ul[@unselectable="unselectable"]//a[@rel="nofollow"]/text()')
page_num = int(page_li[-1])
# print(page_num)
with open('tx.csv','a+',newline='') as f:
    obj = csv.writer(f)
    row = ['课程名字','课程链接']
    obj.writerow(row)
    for i in range(1,page_num+1):   # i 1---34
        # 拼接每一页的课程链接
        page_link = url+'&page='+str(i)
        res = requests.get(page_link,headers = headers)
        res.encoding = 'utf-8'
        page = html.etree.HTML(res.text)
        # print(page_link)
        # 得到所有课程列表
        course_li = page.xpath('//div[@class="course-list"]/div')
        # 循环遍历得到每一个课程
        for course in course_li:
            # 课程名字
            name = course.xpath('.//h3[@class="kc-course-card-name"]/@title')
            # 不完整的课程链接
            link = course.xpath('.//a[@class="kc-course-card js-report-link kc-list-course-card kc-course-card-column"]/@href')
            if name:
                name = name[0]
            else:
                name = ''
            # 完整的课程链接
            if link:
                course_link = 'https://ke.qq.com'+link[0]
            else:
                course_link = ''
            # 将信息写入csv文件
            obj.writerow([name,course_link])
            # print(name,course_link)
        # 页数
        'https://ke.qq.com/course/list?mt=1001&st=2064&page=1'
        'https://ke.qq.com/course/list?mt=1001&st=2064&page=2'
        'https://ke.qq.com/course/list?mt=1001&st=2064&page=3'