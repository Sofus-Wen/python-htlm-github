from flask import Flask
app = Flask(__name__)


@app.route('/foo')
def index():
    return request.base_url


if __name__ == '__main__':
    app.run()
