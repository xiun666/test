import requests
import json
url1 = 'https://www.douyin.com/aweme/v1/web/hot/search/list/?device_platform=webapp&aid=6383&channel=channel_pc_web&detail_list=1&source=6&pc_client_type=1&version_code=170400&version_name=17.4.0&cookie_enabled=true&screen_width=1280&screen_height=720&browser_language=zh-CN&browser_platform=Win32&browser_name=Edge&browser_version=106.0.1370.47&browser_online=true&engine_name=Blink&engine_version=106.0.0.0&os_name=Windows&os_version=10&cpu_core_num=8&device_memory=8&platform=PC&downlink=10&effective_type=4g&round_trip_time=100&webid=7156420363432642088&msToken=nmjU49rk0oG6DG7D58n54HL9tZzhbA3UDK0Eal-Pjuy1iWo8E_XEB8t3f2qUCUdycuY6kf7WuI5vF72dqSXz3zTlprITpHD50aB_nLAIeJAIiKD23vG-O49nvzrtsQ==&X-Bogus=DFSzswVOydTANCAjS/vr9l9WX7jh'
url = 'https://www.douyin.com/aweme/v1/web/page/data/?device_platform=webapp&aid=6383&channel=channel_pc_web&module_count=2&spider=0&pc_client_type=1&version_code=170400&version_name=17.4.0&cookie_enabled=true&screen_width=1280&screen_height=720&browser_language=zh-CN&browser_platform=Win32&browser_name=Edge&browser_version=106.0.1370.47&browser_online=true&engine_name=Blink&engine_version=106.0.0.0&os_name=Windows&os_version=10&cpu_core_num=8&device_memory=8&platform=PC&downlink=10&effective_type=4g&round_trip_time=100&webid=7156420363432642088&msToken=nmjU49rk0oG6DG7D58n54HL9tZzhbA3UDK0Eal-Pjuy1iWo8E_XEB8t3f2qUCUdycuY6kf7WuI5vF72dqSXz3zTlprITpHD50aB_nLAIeJAIiKD23vG-O49nvzrtsQ==&X-Bogus=DFSzswVOhLkANCAjS/vr9l9WX7nT'
header ={
    'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36 Edg/106.0.1370.47',
    'referer':'https://www.douyin.com/discover'
}
# 发送 请求requests.get()
response = requests.get(url1,headers=header)
# 获取网页源码
page = response.text
# print(page)   # 字符串
# 使用json 模块
info = json.loads(page)
# print(info)  #字典类型
# print(type(page),type(info))

#字典取值
word_list = info['data']['word_list'] #info['data']字典

# print(len(word_list))
for item in word_list:
    word = item['word']
    print(word)