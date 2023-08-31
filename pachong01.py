from bs4 import BeautifulSoup
import urllib.request

url = "https://www.jianshu.com/p/deb8002bbba6"

# define a header to address the error: 'HTTP Error 403: Forbidden'
user_agent = 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.0.7) Gecko/2009021910 Firefox/3.0.7'
headers={'User-Agent':user_agent,} 

request=urllib.request.Request(url,None,headers) #The assembled request
response = urllib.request.urlopen(request)
html =response.read()

# 解析网页内容
soup = BeautifulSoup(html, 'html.parser')
usefulurls=[]
pageurls = soup.find_all('a')
for link in pageurls:
    url = link.get('href')
    if url[0:5]!='https':
      pass # 排除不符合要求的网址
    elif len(url)<36:
      pass # 排除不符合要求的网址
    else:
      usefulurls.append(url)
