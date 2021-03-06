# coding:utf8
import url_manager
import html_downloader
import html_outputer
import html_parser


class SpiderMain(object):

    def __init__(self):
        self.urls = url_manager.UrlManager() #url管理器
        self.downloader = html_downloader.HtmlDownloader() #下载器
        self.parser = html_parser.HtmlParser() #解析器
        self.outputer = html_outputer.HtmlOutputer() #输出器

    def craw(self,root_url):
        count = 1

        self.urls.add_new_url(root_url)

        while self.urls.has_new_url():
            try:
                new_url = self.urls.get_new_url()
                print 'craw %d : %s' % (count,new_url)

                html_cont = self.downloader.download(new_url)
                new_urls,new_data = self.parser.parse(new_url,html_cont)
                self.urls.add_new_urls(new_urls)
                self.outputer.collect_data(new_data)

                # 目标爬取1000个界面
                if count == 1000:
                    break
                count = count + 1
            
            except:
                print 'craw failed'

        self.outputer.output_html()


if __name__=="__main__":
    root_url = "http://baike.sogou.com/v10545752.htm"
    obj_spider = SpiderMain()
    obj_spider.craw(root_url)