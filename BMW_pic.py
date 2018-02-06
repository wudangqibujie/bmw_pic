import requests
import urllib
from lxml import etree
user_agent = "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36"
headers = {'User-Agent':user_agent}
r = requests.get("https://car.autohome.com.cn/pic/series/65.html#pvareaid=2042214",headers=headers)
print(r.status_code)
html = etree.HTML(r.text)
img_urls = html.xpath('//div[@class="uibox"]/div[2]/ul/li/a/img/@src')
img_urls=img_urls[2:]
# print(img_urls)
i=0
for img_url in img_urls:
    urllib.request.urlretrieve('https:'+img_url,'img'+str(i)+'.jpg')
    i += 1
