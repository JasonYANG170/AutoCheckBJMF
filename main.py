import requests
import re
import time
import os
from bs4 import BeautifulSoup

# 主机用户
ClassID = input("请输入班级ID：")
X = input("请输入纬度：")
Y = input("请输入经度：")
ACC = input("请输入海拔：")
SearchTime = input("请输入检索时长（建议>60s）：")
MyCookie = input("请输入你的Cookie：")
token = input("请输入pushplus密钥：")

# 输出用户输入的内容
print("开始执行检索")

# GitHub Actions自动任务
# ClassID = os.environ['ClassID']
# X = os.environ['X']
# Y = os.environ['Y']
# ACC = os.environ['ACC']
# SearchTime = os.environ['SearchTime']
# MyCookie = os.environ['MyCookie']
# token = os.environ['e']

# 本地面板运行
#ClassID = ''
#X = ''
#Y = ''
#ACC = ''
#SearchTime = 60
#MyCookie = ''
#token = ''  #在pushplus网站中可以找到

title = '班级魔法自动签到任务'  # 改成你要的标题内容
url = 'http://k8n.cn/student/course/' + ClassID + '/punchs'

headers = {
    'User-Agent': 'Mozilla/5.0 (Linux; Android 12; PAL-AL00 Build/HUAWEIPAL-AL00; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/116.0.0.0 Mobile Safari/537.36 XWEB/1160065 MMWEBSDK/20231202 MMWEBID/1136 MicroMessenger/8.0.47.2560(0x28002F35) WeChat/arm64 Weixin NetType/4G Language/zh_CN ABI/arm64',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/wxpic,image/tpg,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'X-Requested-With': 'com.tencent.mm',
    'Referer': 'http://k8n.cn/student/course/75717',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'zh-CN,zh-SG;q=0.9,zh;q=0.8,en-SG;q=0.7,en-US;q=0.6,en;q=0.5',
    'Cookie': MyCookie
}

while True:
    response = requests.get(url, headers=headers)
    print("响应:", response)

    # 创建 Beautiful Soup 对象解析 HTML
    soup = BeautifulSoup(response.text, 'html.parser')

    # 使用正则表达式从 HTML 文本中提取所有 punch_gps() 中的数字
    pattern = re.compile(r'punch_gps\((\d+)\)')
    matches = pattern.findall(response.text)

    if matches:
        for match in matches:
            print(match)
            url = "http://k8n.cn/student/punchs/course/" + ClassID + "/" + match
            payload = {
                'id': match,
                'lat': X,
                'lng': Y,
                'acc': ACC,
                'res': '',
                'gps_addr': ''
            }

            response = requests.post(url, headers=headers, data=payload)

            if response.status_code == 200:
                print("请求成功")
                print("响应:", response)

                # 解析响应的 HTML 内容
                soup_response = BeautifulSoup(response.text, 'html.parser')
                h1_tag = soup_response.find('h1')

                if h1_tag:
                    h1_text = h1_tag.text
                    print(h1_text)
                    # encoding:utf-8
                    url = 'http://www.pushplus.plus/send?token=' + token + '&title=' + title + '&content=' + h1_text  # 不使用请注释
                    requests.get(url)  # 不使用请注释
                    continue  # 返回到查找进行中的签到循环
                else:
                    print("未找到 <h1> 标签")
            else:
                print("请求失败，状态码:", response.status_code)
    else:
        print("未找到在进行的签到")

    # 可以设置一个间隔时间，避免过于频繁地请求
    time.sleep(SearchTime)  # 暂停10秒后重新尝试
