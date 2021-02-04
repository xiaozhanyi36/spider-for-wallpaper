import requests
import os
url="https://api.ixiaowai.cn/api/api.php"
def download_img(url):
    os.mkdir("img")
    maxn=int(input("几张？："))
    for i in range(1,maxn):
        s=str(i)
        r = requests.get(url)
        if r.status_code==200:
            with open('./img/img'+s+'.png', 'wb') as f:
                f.write(r.content)
                print("第"+s+"张下载成功")
download_img(url)
