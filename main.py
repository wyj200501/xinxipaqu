# 这是一个示例 Python 脚本。
import bs4
import requests
from bs4 import BeautifulSoup
import os

url = 'https://sci.upc.edu.cn/2016/0926/c6970a96344/page.htm'
header = {
 'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36 Edg/116.0.1938.76'
}

def d(c):
 c = BeautifulSoup(c,'html.parser')
 # print(c.original_encoding)
 title = c.find('td',class_ = 'infotitle')
 with open(title.text + '.txt' ,'w',encoding='utf-8') as f:
   table = c.find('table',class_ = 'MsoNormalTable')
   trk = table.findAll('tr')
   for tr in trk:
       tds = tr.findAll('td')
       for td in tds:
            for child in td.children:
                print("td = " + str(child))
                if child.name == 'p':
                    f.writelines(os.linesep)
                if type(child) is not bs4.NavigableString and None != child.text and "" != child.text:
                    f.write(child.text)
                print(child)
if __name__ == '__main__':
    r = requests.get(url, header)
    d(r.content)
