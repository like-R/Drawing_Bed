import requests
import base64
import json




# 上传文件
def upload_file_to_github_drawing_bed():
    file_name = "屏幕截图(1).png"  #文件名
    token = ""
#     url = "https://api.github.com/repos/Ike-li/Drawing_Bed/contents/"+file_name  # 用户名、库名、路径
    url = "https://api.github.com/repos/[user]/[repo]/contents/[path]/"+file_name  # 用户名、库名、路径
    headers = {"Authorization": "token " + token}
    # content = file_base64(file_data)
    f = open(r'C:\Users\ASUS_Ike\Pictures\Screenshots\屏幕截图(1).png', 'rb')
    fnb64 = base64.b64encode(f.read()).decode('utf-8')
    content = fnb64
    # print(content)
    data = {
        "message": "message",
        "committer": {
#             "name": "Ike-li",
#             "email": "sinyercy@163.com"
          "name": "[user]",
          "email": "user@163.com"
          
        },
        "content": content
    }
    data = json.dumps(data)
    req = requests.put(url=url, data=data, headers=headers)
    req.encoding = "utf-8"
    re_data = json.loads(req.text)
    print(re_data)
    print(re_data['content']['sha'])
    print("https://cdn.jsdelivr.net/gh/Ike-li/Drawing_Bed/pictures"+file_name)
# 在国内默认的down_url可能会无法访问，因此使用CDN访问


if __name__ == '__main__':
    # fdata = open_file('bg-dropdown.png')
    upload_file_to_github_drawing_bed()
