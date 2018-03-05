#coding:utf8
from bs4 import BeautifulSoup
import re
import urlparse

class HtmlParser(object):

    def _get_new_urls(self,page_url,soup):
        new_urls = set()
        # /view/123.htm
        # soup.encode('utf-8')
        links =  soup.find_all('a',class_=(""" ed_inner_link """))
        # print soup
        print links

        for link in links:
            new_url = link['href']
            new_all_url = urlparse.urljoin("http://baike.sogou.com/",new_url)
            new_urls.add(new_all_url)
        
        return new_urls



    
    def _get_new_data(self,page_url,soup):
        res_data = {}
        res_data['url'] = page_url

        
        #<dd class="lemmaWgt-lemmaTitle-title"> <h1>Python</h1>
        title_node = soup.find('div',class_="lemma_name").find('h1')
        res_data['title'] = title_node.get_text()
       

        summary_node = soup.find('div',class_="abstract")
        # print summary_node
        res_data['summary'] = summary_node.get_text()


        return res_data


    def parse(self,page_url,html_cont):
        if page_url is None or html_cont is None:
            return
        soup = BeautifulSoup(html_cont,'html.parser',from_encoding='utf-8')
        
        new_urls = self._get_new_urls(page_url,soup)
        new_data = self._get_new_data(page_url,soup)

        return new_urls,new_data

        

            