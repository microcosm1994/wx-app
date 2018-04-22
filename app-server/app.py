from flask import Flask, request
import control
import json

app = Flask(__name__)


@app.route('/video/<type>', methods=['GET', 'POST'])
def video(type):
    if type == 'frist':
        return control.video.frist()
    if type == 'detailed':
        return control.video.detailed_func(request.data)
    if type == 'search':
        return control.video.search_func(request.args.get('q'))


@app.route('/book/<type>', methods=['GET', 'POST'])
def book(type):
    if type == 'free':
        return control.book.free_func()
    if type == 'wrap':
        return control.book.wrap_func()
    if type == 'week':
        return control.book.week_func()
    if type == 'writer':
        return control.book.writer_func()
    if type == 'detailed':
        return control.book.detailed_func(request.args.get('url'))
    if type == 'detailed_read':
        return control.book.read_func(request.args.get('url'), request.args.get('type'))
    if type == 'detailed_list':
        return control.book.list_func(request.args.get('url'))
    if type == 'groom':
        return control.book.groom_func()
    if type == 'search':
        return control.book.search_func(request.args.get('value'))



if __name__ == '__main__':
    app.debug = True
    app.run(threaded=True)
