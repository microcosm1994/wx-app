# coding: utf-8
import requests
import json
from bs4 import BeautifulSoup

r = requests.get('https://www.qidian.com/')
r.encoding = 'utf-8'
soup = BeautifulSoup(r.text, from_encoding='utf-8')
list_soup = ''


def free_func():
    countdown = soup.select('.time-limit-wrap #numero5 li')
    free = []
    for item in countdown:
        if item.attrs['class'][0] != 'time-box':
            info = {}
            if len(item.select('.book-img a img')) > 0:
                info['cover'] = item.select('.book-img a img')[0]['data-original']
            if len(item.select('.name')) > 0:
                info['url'] = item.select('.name')[0]['href']
                info['title'] = item.select('.name')[0].text
            free.append(info)
    return json.dumps(free)


def wrap_func():
    result = {}
    wrap = soup.select('#rank-list-row .rank-list')
    for item in wrap:
        if item['data-l2'] == "2":
            books_url = 'http:' + item.select('.wrap-title a')[0]['href']
            books_html = requests.get(books_url)
            books_soup = BeautifulSoup(books_html.text, from_encoding='utf-8')
            books = books_soup.select('.rank-body .book-img-text li')
            booklist = []
            num = 0
            for key in books:
                if num < 10:
                    info = {}
                    if len(key.select('.book-img-box a img')) > 0:
                        info['cover'] = key.select('.book-img-box a img')[0]['src']
                    if len(key.select('.book-mid-info h4 a')) > 0:
                        info['url'] = key.select('.book-mid-info h4 a')[0]['href']
                        info['title'] = key.select('.book-mid-info h4 a')[0].text
                    if len(key.select('.book-mid-info .author .name')) > 0:
                        info['actor'] = key.select('.book-mid-info .author .name')[0].text
                    booklist.append(info)
                num += 1
            index = 0
            wraplist = []
            wraplist1 = []
            for element in booklist:
                if index < 3:
                    wraplist1.append(element)
                else:
                    wraplist.append(element)
                index += 1
            result['wrapbox'] = wraplist
            result['wrap'] = wraplist1
    return json.dumps(result)


def week_func():
    wrap = soup.select('#rank-list-row .rank-list')
    for item in wrap:
        if item['data-l2'] == "4":
            books_url = 'http:' + item.select('.wrap-title a')[0]['href']
            books_html = requests.get(books_url)
            books_soup = BeautifulSoup(books_html.text, from_encoding='utf-8')
            books = books_soup.select('.rank-body .book-img-text li')
            booklist = []
            num = 0
            for key in books:
                if num < 10:
                    info = {}
                    if len(key.select('.book-img-box a img')) > 0:
                        info['cover'] = key.select('.book-img-box a img')[0]['src']
                    if len(key.select('.book-mid-info h4 a')) > 0:
                        info['url'] = key.select('.book-mid-info h4 a')[0]['href']
                        info['title'] = key.select('.book-mid-info h4 a')[0].text
                    if len(key.select('.book-mid-info .author .name')) > 0:
                        info['actor'] = key.select('.book-mid-info .author .name')[0].text
                    booklist.append(info)
                num += 1
    return json.dumps(booklist)


def writer_func():
    wrap = soup.select('#rank-list-row .rank-list')
    for item in wrap:
        if item['data-l2'] == "5":
            books_url = 'http:' + item.select('.wrap-title a')[0]['href']
            books_html = requests.get(books_url)
            books_soup = BeautifulSoup(books_html.text, from_encoding='utf-8')
            books = books_soup.select('.rank-body .book-img-text li')
            booklist = []
            num = 0
            for key in books:
                if num < 10:
                    info = {}
                    if len(key.select('.book-img-box a img')) > 0:
                        info['cover'] = key.select('.book-img-box a img')[0]['src']
                    if len(key.select('.book-mid-info h4 a')) > 0:
                        info['url'] = key.select('.book-mid-info h4 a')[0]['href']
                        info['title'] = key.select('.book-mid-info h4 a')[0].text
                    if len(key.select('.book-mid-info .author .name')) > 0:
                        info['actor'] = key.select('.book-mid-info .author .name')[0].text
                    booklist.append(info)
                num += 1
    return json.dumps(booklist)


def detailed_func(url):
    detailed = requests.get('http:' + url)
    detailed.encoding = 'utf-8'
    detailed_soup = BeautifulSoup(detailed.text, from_encoding='utf-8').select('.book-detail-wrap')[0]
    global list_soup
    list_soup = BeautifulSoup(detailed.text, from_encoding='utf-8').select('.book-detail-wrap')[0]
    result = {}
    # 封面
    if len(detailed_soup.select('.book-information .book-img a img')) > 0:
        result['cover'] = detailed_soup.select('.book-information .book-img a img')[0]['src']
    # 标题
    if len(detailed_soup.select('.book-information .book-info h1 em')) > 0:
        result['title'] = detailed_soup.select('.book-information .book-info h1 em')[0].text
    # 作者
    if len(detailed_soup.select('.book-information .book-info h1 span a')) > 0:
        result['actor'] = detailed_soup.select('.book-information .book-info h1 span a')[0].text
    # 类型
    if len(detailed_soup.select('.book-information .book-info .tag a')) > 0:
        result['type'] = detailed_soup.select('.book-information .book-info .tag a')[0].text
    # 文案
    if len(detailed_soup.select('.book-information .book-info .intro')) > 0:
        result['slogan'] = detailed_soup.select('.book-information .book-info .intro')[0].text
    # 状态
    if len(detailed_soup.select('.book-information .book-info .tag span')) > 0:
        result['status'] = detailed_soup.select('.book-information .book-info .tag span')[0].text
    # 作品信息
    if len(detailed_soup.select('.book-info-detail .book-intro p')) > 0:
        result['des'] = detailed_soup.select('.book-info-detail .book-intro p')[0].text
    # 最近更新
    if len(detailed_soup.select('.book-info-detail .book-state .update')) > 0:
        result['updatetext'] = detailed_soup.select('.book-info-detail .book-state .update .detail .cf a')[0].text
        result['updateurl'] = detailed_soup.select('.book-info-detail .book-state .update .detail .cf a')[0]['href']
        result['updatetime'] = detailed_soup.select('.book-info-detail .book-state .update .detail .cf .time')[0].text
    return json.dumps(result)


def read_func(url):
    detailed1 = requests.get('http:' + url)
    detailed1.encoding = 'utf-8'
    detailed1_soup = BeautifulSoup(detailed1.text, from_encoding='utf-8').select('.book-detail-wrap')[0]
    # 试读文章
    if len(detailed1_soup.select('.book-information .book-info p .J-getJumpUrl')) > 0:
        read_url = detailed1_soup.select('.book-information .book-info p .J-getJumpUrl')[0]['href']
    read = requests.get('http:' + read_url)
    read.encoding = 'utf-8'
    read_soup = BeautifulSoup(read.text, from_encoding='utf-8')
    result = {}
    if len(read_soup.select('.wrap .read-main-wrap #j_chapterBox .text-wrap .main-text-wrap')) > 0:
        # 标题
        result['title'] = read_soup.select('.read-main-wrap #j_chapterBox .text-wrap .main-text-wrap .text-head h3')[
            0].text
        # 内容
        result['content'] = read_soup.select('.read-main-wrap #j_chapterBox .text-wrap .main-text-wrap .read-content')[0].text
    if len(read_soup.select('.read-main-wrap .chapter-control')) > 0:
        # 下一章
        result['next'] = read_soup.select('.read-main-wrap .chapter-control #j_chapterNext')[0]['href']
        # 上一章
        result['prev'] = read_soup.select('.read-main-wrap .chapter-control #j_chapterPrev')[0]['href']
    return json.dumps(result)


def list_func():
    result = []
    if len(list_soup.select('.catalog-content-wrap .volume-wrap .volume')) > 0:
        volumelist = list_soup.select('.catalog-content-wrap .volume-wrap .volume')
        for item in volumelist:
            volume = {}
            volume['title'] = item.select('h3').text
            if len(item.select('ul li')) > 0:
                content = []
                for key in item.select('ul li'):
                    content_info = {}
                    content_info['title'] = key.select('a')[0].text
                    content_info['url'] = key.select('a')[0]['href']
                    content.append(content_info)
                volume['content'] = content
            result.append(volume)
    return json.dumps(result)
