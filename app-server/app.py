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
    if type == 'frist':
        return control.book.frist()


if __name__ == '__main__':
    app.debug = True
    app.run(threaded=True)
