from flask import Flask

app = Flask(__name__)


@app.route('/info')
def hello_world():
    # return 'Hello World'
    return 'new content'


if __name__ == '__main__':
    print('starting server..')
    app.run(port=80)
