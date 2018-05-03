from flask import Flask
from flask import request, jsonify, make_response, render_template, redirect

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')


if __name__ == '__main__':
    app.run(
        port=5000,
        debug=True,
    )
