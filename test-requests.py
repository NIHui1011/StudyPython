# -*- coding:UTF-8 -*-

import requests

def request():
    url = "http://www.baidu.com"
    respose = requests.get(url)
    print "header:"
    print respose.headers
    print "content:"
    print respose.text

    print respose.status_code
    print ''
    # print respose.json()

if __name__=='__main__':
    request()