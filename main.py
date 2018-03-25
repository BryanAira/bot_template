from flask import Flask


app = Flask(__name__)


@app.route('/')
def index():
    return '<H1>Test Flask app</h1>'


if __name__ == '__main__':
    app.run()
