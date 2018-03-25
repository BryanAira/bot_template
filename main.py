from flask import Flask


app = Flask(__name__)


@app.route('/')
def index():
    return '<H1>Test Flask app</h1>'


@app.route('/s')
def indexs():
    return '<H1>Test Flask app S</h1>'


if __name__ == '__main__':

    with open('asfa.txt', 'w', encoding='utf-8') as f:
        f.write('sssss')

    app.run()
