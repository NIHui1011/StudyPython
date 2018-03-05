#coding:utf8

import urllib2
import urllib
import sys
import re

def get_weather():

    provice = raw_input('输入省份名（请使用拼音）：')
    city = raw_input('输入城市名（请使用拼音）：')
    url = 'http://qq.ip138.com/weather/' + provice +'/'+ city + '.htm'
    print url

    weatherhtml = urllib2.urlopen(url)
    res = weatherhtml.read().decode('GB2312')
    print res

    f = open('weather.txt','wb')
    f.write(weatherhtml.read())
    f.close

     #正则表达式获取天气信息  
    pattern = 'Title.+<b>(.+)</b>'  
    Title = re.search(pattern,res).group(1)  
  
    pattern = '>(\d*-\d*-\d*.+?)<'  
    date = re.findall(pattern,res)  
  
    pattern = 'alt="(.+?)"'  
    weather = re.findall(pattern,res)  
  
    print ("%35.30s"%Title)  
    length = len(date)  
    for i in range (0,length):  
        print ('%33.20s'%date[i], '\t%s'%weather[i])  





if __name__ == "__main__":
    get_weather()