from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World'

@app.route('/info')
def new_content():
    # return 'Hello World'
    return 'new content'


if __name__ == '__main__':
    print('starting server..')
    app.run(host='0.0.0.0', port=80)
