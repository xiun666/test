# 导包
from selenium import webdriver
import csv, time
#以无界面的形式启动谷歌浏览器
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--headless--')
chrome_options.add_argument('--disable-gpu')
chrome_options.headless = True
bro = webdriver.Chrome(options=chrome_options)

# 直接启动谷歌浏览器
# bro = webdriver.Chrome()

#访问东方财富网
bro.get('http://fund.eastmoney.com/data/diyfundranking.html')

# 文本操作，写入csv文件，默认有空行，加上newline参数无空行
with open('invent.csv', 'a+', encoding='utf-8-sig',newline='')as f:
    spoiled = csv.writer(f) #获取写对象
    spoiled.writerow(["序号", "基金代码", "基金简称", "期间涨幅", "期间分红(元/份)", "分红次数", "起始日期", "单位净值", "累计净值", "终止日期", "单位净值", "累计净值","成立日期", "手续费"])# 写入列名
    #循环实现翻页
    for i in range(1, 321):
        #获取当前页面所有基金信息所在tr标签
        nurse = bro.find_elements_by_xpath('//table[@id="dbtable"]/tbody/tr')
        #遍历获取每一个基金，使用解析方法获取每个所需信息比如序号，基金名称等
        for pitch in nurse:
            entrance = pitch.find_element_by_xpath('.//td[2]').text  #序号
            drink = pitch.find_element_by_xpath('.//td[3]').text #基金代码
            possible = pitch.find_element_by_xpath('.//td[4]').text #基金简称
            painting = pitch.find_element_by_xpath('.//td[5]').text # 期间涨幅
            suggestion = pitch.find_element_by_xpath('.//td[6]').text #期间分红
            boil = pitch.find_element_by_xpath('.//td[7]').text #分红次数
            intrude = pitch.find_element_by_xpath('.//td[8]').text #起始日期
            leg = pitch.find_element_by_xpath('.//td[9]').text #单位净值
            excuse = pitch.find_element_by_xpath('.//td[10]').text #累计净值
            appointment = pitch.find_element_by_xpath('.//td[11]').text #终止日期
            science = pitch.find_element_by_xpath('.//td[12]').text #单位净值
            invented = pitch.find_element_by_xpath('.//td[13]').text #累计净值
            cat = pitch.find_element_by_xpath('.//td[14]').text #成立日期
            dog = pitch.find_element_by_xpath('.//td[15]').text #手续费
            #转化为列表形式
            b = [entrance, drink, possible, painting, suggestion, boil, intrude, leg, excuse, appointment, science,invented, cat, dog]
            print(b)
            #写入csv文件
            spoiled.writerow(b)
        #找到下一页按钮，点击实现翻页
        jik = bro.find_elements_by_xpath('//div[@id="pagebar"]/label')
        jik[7].click()
        time.sleep(3)
#关闭浏览
bro.close()
