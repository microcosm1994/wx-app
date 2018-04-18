# coding: utf-8
import requests
import json
from bs4 import BeautifulSoup

r = requests.get('https://www.qidian.com/')
r.encoding = 'utf-8'
soup = BeautifulSoup(r.text, from_encoding='utf-8')


def free_func():
    countdown = soup.select('.time-limit-wrap #numero5 li')
    free = {}
    free['freelist'] = []
    for item in countdown:
        if item.attrs['class'][0] == 'time-box':
            free['countdown'] = item.attrs['data-endtime']
        else:
            info = {}
            if len(item.select('.book-img a img')) > 0:
                info['cover'] = item.select('.book-img a img')[0]['data-original']
            if len(item.select('.name')) > 0:
                info['url'] = item.select('.name')[0]['href']
                info['title'] = item.select('.name')[0].text
            free['freelist'].append(info)
    return json.dumps(free)


def wrap_func():
    result = {}
    wrap = soup.select('#rank-list-row .rank-list')
    for item in wrap:
        if item['data-l2'] == "2" or item['data-l2'] == "4" or item['data-l2'] == "5":
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
            if item['data-l2'] == "2":
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
            if item['data-l2'] == "4":
                result['week'] = booklist
            if item['data-l2'] == "5":
                result['writer'] = booklist
    return json.dumps(result)
