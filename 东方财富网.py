from selenium import webdriver
import csv, time
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--headless--')
chrome_options.add_argument('--disable-gpu')
chrome_options.headless = True
bro = webdriver.Chrome(options=chrome_options)
bro.get('http://fund.eastmoney.com/data/diyfundranking.html')

with open('invent.csv', 'a+', encoding='utf-8', newline='')as f:
    spoiled = csv.writer(f)
    spoiled.writerow(["序号", "基金代码", "基金简称", "期间涨幅", "期间分红(元/份)", "分红次数", "起始日期", "单位净值", "累计净值", "终止日期", "单位净值", "累计净值","成立日期", "手续费"])
    for i in range(1, 321):
        nurse = bro.find_elements_by_xpath('//table[@id="dbtable"]/tbody/tr')
        for pitch in nurse:
            entrance = pitch.find_element_by_xpath('.//td[2]').text
            drink = pitch.find_element_by_xpath('.//td[3]').text
            possible = pitch.find_element_by_xpath('.//td[4]').text
            painting = pitch.find_element_by_xpath('.//td[5]').text
            suggestion = pitch.find_element_by_xpath('.//td[6]').text
            boil = pitch.find_element_by_xpath('.//td[7]').text
            intrude = pitch.find_element_by_xpath('.//td[8]').text
            leg = pitch.find_element_by_xpath('.//td[9]').text
            excuse = pitch.find_element_by_xpath('.//td[10]').text
            appointment = pitch.find_element_by_xpath('.//td[11]').text
            science = pitch.find_element_by_xpath('.//td[12]').text
            invented = pitch.find_element_by_xpath('.//td[13]').text
            cat = pitch.find_element_by_xpath('.//td[14]').text
            dog = pitch.find_element_by_xpath('.//td[15]').text
            b = [entrance, drink, possible, painting, suggestion, boil, intrude, leg, excuse, appointment, science,
                 invented, cat, dog]
            print(b)
            spoiled.writerow(b)
        jik = bro.find_elements_by_xpath('//div[@id="pagebar"]/label')
        jik[7].click()
        time.sleep(3)

bro.close()