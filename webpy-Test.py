#!/usr/bin/python
# -*- coding: UTF-8 -*-
# 文件名：webpy-Test.py

import web
import MySQLdb
import MySQLdb.cursors
        
#定义模板文件夹        
render = web.template.render('templates')

#python 三种响应的方式 
# 模板文件获取render.index('参数') 
# 结果数据获取model.selet('sql') 
# URL跳转web.seeother(url)


#url映射（路由）:
# url完全匹配 '/index','index',
# url模糊匹配 '/blog/\d+','blog',
# url带组匹配 '/(.*)', 'hello',
# 匹配范围大的url要放在下面

urls = (
    '/articles','Articles',
    '/index','Index',
    '/blog/\d+','Blog',
    '/(.*)', 'hello'
)
app = web.application(urls, globals())

class Articles:
    def GET(self):
        conn = MySQLdb.connect(host='localhost',user='root',passwd='nihh',db='TESTDB',port=3306,cursorclass=MySQLdb.cursors.DictCursor)
        cur = conn.cursor()
        cur.execute("select * from EMPLOYEE")
        r = cur.fetchall()
        cur.close()
        conn.close()
        return render.articles(r)
        # return r




class Index:
    def GET(self):
        #获取请求参数 web.input()
        query = web.input()
        # return 'index method'
        # return query
        
        # return web.seeother('/article')
        return web.seeother('http://www.baidu.com')



class Blog:
    def GET(self):
        # query = web.input()
        # return 'blog method'
        # return "blog method : %s" % query

        #获取请求头 web.ctx.env
        return web.ctx.env
        
    def POST(self):
        data = web.input()
        # return 'blog post method'
        return "blog post method : %s" % data

class hello:        
    def GET(self, name):
        # if not name: 
        #     name = 'World'
        # return 'Hello, ' + name + '!'
        
        # return "<html>ssssdsdss</html>"
        # return open("python-test.html",'r').read()
        # return open("webpy-form.html",'r').read()
        # print name
        return render.mytemplate1(name)

                
if __name__ == "__main__":
    app.run()