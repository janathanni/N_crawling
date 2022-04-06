import urllib.request, urllib.parse
from selenium import webdriver

from bs4 import BeautifulSoup

class NblogCrawling:
    def __init__(self, word : str, post_num : int = 1, header : dict = {'User-Agent' : 'Chrome/96.0.4664.110'}) -> None:
        self.page_num = post_num
        self.header = header
        self.word = urllib.parse.quote(word)
        self.base_page = f'https://search.naver.com/search.naver?query={word}&nso=&where=blog&sm=tab_opt'

    def url_get(self) -> list:
        news_urls = []

        for num in range(0, self.page_num):
            if num == 0:
                page = self.base_page + '1'

            else:
                page = self.base_page + str(num) + '1'

            req = urllib.request.Request(page, headers = self.header)
            before_soup = urllib.request.urlopen(req)

            soup = BeautifulSoup(before_soup, 'html.parser')

            for news_url in soup.find_all(attrs={'class' : "news_tit"}):
                news_urls.append(news_url.get('href'))
        
        return news_urls

    def title_get(self) -> list:
        news_titles = []

        for num in range(0, self.page_num):
            if num == 0:
                page = self.base_page + '1'

            else:
                page = self.base_page + str(num) + '1'

            req = urllib.request.Request(page, headers = self.header)
            before_soup = urllib.request.urlopen(req)

            soup = BeautifulSoup(before_soup, 'html.parser')

            for news_title in soup.find_all(attrs={'class' : "news_tit"}):
                news_titles.append(news_title.get('title'))
        
        return news_titles


    def all_get(self) -> list:
        ti_urls = []

        for num in range(0, self.page_num):
            if num == 0:
                page = self.base_page + '1'

            else:
                page = self.base_page + str(num) + '1'

            req = urllib.request.Request(page, headers = self.header)
            before_soup = urllib.request.urlopen(req)

            soup = BeautifulSoup(before_soup, 'html.parser')

            for ti_url in soup.find_all(attrs={'class' : "news_tit"}):
                ti_urls.append((ti_url.get('title'), ti_url.get('href')))
        
        return ti_urls

hehe = NblogCrawling('니니즈', 2)
print(hehe.all_get())