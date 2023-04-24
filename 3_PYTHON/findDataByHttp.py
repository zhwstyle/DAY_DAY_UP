import requests  # 导包
import json
host = ""  # 部署的服务器地址
# 请求地址
url = "www.baidu.com" # 拼接地址
header = {
}
# 参数
body = {}

# 发送请求
r = requests.post(url=url, headers=header, json=body)
res=r.text
# jsonData=json.dumps(res,ensure_ascii=False)
jsonData=json.loads(res)
listData=jsonData['data']['list']
for i in listData:
    # i['uri']
    file = open('/5_SOLUTION/GET_DATA/data.txt','a',encoding='utf-8')
    file.writelines( i['uri'] +"\n")
    # 输出返回
    print(i['uri'])

