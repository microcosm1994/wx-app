from flask import Flask, request
from bs4 import BeautifulSoup
import requests
import json

app = Flask(__name__)


@app.route('/video/<type>', methods=['GET', 'POST'])
def video(type):
    print(type)
    url = 'https://movie.douban.com/'
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:53.0) Gecko/20100101 Firefox/53.0',
        'Accept - Language': 'zh - CN, zh;q = 0.8, en - US;q = 0.5, en;q = 0.3'
    }
    r = requests.get(url, headers=headers)
    r.encoding = 'utf-8'
    #
    soup = BeautifulSoup(r.text, from_encoding='utf-8')
    if type == 'screening':
        screening = soup.select('.screening-bd .ui-slide-content .ui-slide-item')
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
        return json.dumps(screening_data)
    if type == 'hotmovie':
        hotmovie = soup.select('.screening-bd .ui-slide-content .ui-slide-item')
        hotmovie_data = []
        for item in hotmovie:
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
                hotmovie_data.append(obj)
        return json.dumps(hotmovie_data)


@app.route('/find/<username>')
def find(username):
    return 'find %s' % username


if __name__ == '__main__':
    app.debug = True
    app.run()
