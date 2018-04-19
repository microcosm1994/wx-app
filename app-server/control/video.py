# coding: utf-8
import requests
from bs4 import BeautifulSoup
import json

url = 'https://movie.douban.com/'
headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:53.0) Gecko/20100101 Firefox/53.0',
    'Accept - Language': 'zh - CN, zh;q = 0.8, en - US;q = 0.5, en;q = 0.3'
}
r = requests.get(url, headers=headers)
r.encoding = 'utf-8'
soup = BeautifulSoup(r.text, from_encoding='utf-8')


# 豆瓣电影首页数据
def frist():
    result = {}
    screening = soup.select('.screening-bd .ui-slide-content .ui-slide-item')
    if len(soup.select('.screening-bd .ui-slide-content .ui-slide-item')):
        screening_data = []
        for item in screening:
            obj = {}
            if len(item.select('ul')) != 0:
                obj['cover'] = item.select('.poster a img')[0]['src']
                obj['url'] = item.select('.poster a')[0]['href']
                obj['title'] = item.select('.title a')[0].string
                if len(item.select('.rating .subject-rate')) != 0:
                    obj['rating'] = item.select('.rating .subject-rate')[0].string
                else:
                    obj['rating'] = '0.0'
                obj['ticket'] = item.select('.ticket_btn span a')[0]['href']
                screening_data.append(obj)
        hotmovie = requests.get(
            'https://movie.douban.com/j/search_subjects?type=movie&tag=%E7%83%AD%E9%97%A8&page_limit=50&page_start=0').text
        result['screening_data'] = screening_data
        result['hotmovie_data'] = json.loads(hotmovie)['subjects']
    return json.dumps(result)


# 豆瓣电影电影详情数据
def detailed_func(options):
    result = {}
    detailed_url = json.loads(options)['url']
    print options
    detailed_headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:53.0) Gecko/20100101 Firefox/53.0',
        'Accept - Language': 'zh - CN, zh;q = 0.8, en - US;q = 0.5, en;q = 0.3'
    }
    detailed = requests.get(detailed_url, headers=detailed_headers)
    detailed.encoding = 'utf-8'
    detailed_soup = BeautifulSoup(detailed.text, from_encoding='utf-8')
    # 影片信息
    if len(detailed_soup.select('#info .pl')) > 0:
        info = ''
        for item in detailed_soup.select('#info .pl'):
            value = ''
            if item.next_sibling != ' ':
                value = item.next_sibling
            else:
                if len(item.find_next_siblings('span')) > 0:
                    value = item.find_next_siblings('span')[0].string
            info = info + item.string + value
            if len(item.find_next_siblings('span', 'attrs')) > 0:
                index = 0
                for sibling in item.find_next_siblings('span', 'attrs')[0].children:
                    index += 1
                    if index < 4:
                        if sibling.string:
                            info = info + sibling.string
        result['info'] = info
    # 影片标题
    if len(detailed_soup.select('h1 span')) > 0:
        title = ''
        for item in detailed_soup.select('h1 span'):
            title = title + item.string
        result['title'] = title
    # 剧情简介
    if len(detailed_soup.select('.related-info .indent span')) > 0:
        synopsis = detailed_soup.select('.related-info .indent span')[0].text.lstrip()
        result['synopsis'] = synopsis
    # 影人
    if len(detailed_soup.select('.celebrities .celebrities-list li')) > 0:
        celebrities = detailed_soup.select('.celebrities .celebrities-list li')
        actors = []
        for item in celebrities:
            actor = {}
            if len(item.select('.avatar')) > 0:
                actor['img'] = item.select('.avatar')[0]['style'].lstrip('background-image: url(').rstrip(')')
            if len(item.select('.info .name .name')) > 0:
                actor['name'] = item.select('.info .name .name')[0].string
            if len(item.select('.info .role')) > 0:
                actor['status'] = item.select('.info .role')[0].string
            actors.append(actor)
        result['actors'] = actors
    # 剧照列表
    if len(detailed_soup.select('.related-pic .related-pic-bd li')) > 0:
        related = detailed_soup.select('.related-pic .related-pic-bd li')
        photolist = []
        for item in related:
            photolist.append(item.a.img['src'])
        result['photoList'] = photolist
    # 评分
    if len(detailed_soup.select('.rating_self strong')) > 0:
        grade = detailed_soup.select('.rating_self strong')[0].string
        result['grade'] = grade
    # 相关电影
    if len(detailed_soup.select('.recommendations-bd dl')) > 0:
        aboutlist = detailed_soup.select('.recommendations-bd dl')
        aboutmovies = []
        for item in aboutlist:
            movie = {
                'cover': item.dt.a.img['src'],
                'title': item.dd.a.text
            }
            aboutmovies.append(movie)
        result['aboutmovies'] = aboutmovies
    # 影片评论
    if len(detailed_soup.select('#hot-comments .comment-item')) > 0:
        commentlist = detailed_soup.select('#hot-comments .comment-item')
        comment = []
        for item in commentlist:
            user = {}
            user['nickname'] = item.select('.comment .comment-info a')[0].text
            user['time'] = item.select('.comment .comment-info .comment-time ')[0].text.lstrip()
            user['like'] = item.select('.comment .comment-vote .votes')[0].text
            user['content'] = item.select('.comment p')[0].text
            comment.append(user)
        result['comment'] = comment
    # 返回数据结果
    result['cover'] = json.loads(options)['cover']
    return json.dumps(result)


# 豆瓣电影搜索
def search_func(value):
    response = requests.get('https://movie.douban.com/j/subject_suggest?q=' + value, headers=headers)
    response.encoding = 'utf-8'
    return json.dumps(response.json())
