from flask import Flask, request
import requests
import json

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def hello_world():
    url = 'https://cospace.cc/api/works/ranking?p=1&size=20&type=fixed_day&original=0'
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:53.0) Gecko/20100101 Firefox/53.0',
        'Accept - Language': 'zh - CN, zh;q = 0.8, en - US;q = 0.5, en;q = 0.3'
    }
    r = requests.get(url, headers=headers)
    data = r.json()
    result = ''
    for item in data:
        if item == 'data':
            d = data[item]
            result = d['works']
            for value in result:
                print(value)
                print(type(value))
    return json.dumps(result)


@app.route('/find/<username>')
def find(username):
    return 'find %s' % username


if __name__ == '__main__':
    app.debug = True
    app.run()
