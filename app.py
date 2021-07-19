from flask import Flask, render_template, jsonify, request

app = Flask(__name__)

from pymongo import MongoClient

client = MongoClient('localhost', 27017)
db = client.dbsparta
# 클라이언트이름은 bluenight?


## HTML을 주는 부분
@app.route('/')
def home():
    return render_template('index.html')



if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)
