import os
import requests

from flask import Flask, render_template, request


app = Flask(__name__)

BACKEND_HOST = os.environ['BACKEND_HOST']
BACKEND_PORT = os.environ.get('BACKEND_PORT', 8080)


def get_backend_url(url_path: str) -> str:
    return 'http://' + BACKEND_HOST + ':' + BACKEND_PORT + url_path

@app.route('/')
def index():
    return render_template('index.html', backend_host=BACKEND_HOST, backend_port=BACKEND_PORT)

@app.route('/add', methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        if request.form.get('Pair1') == 'Pair1':
            url = get_backend_url('/add/1=2')
            response = requests.get(url)
            if response.status_code == 200:
                return render_template('add.html', response=response)
        elif request.form.get('Pair2') == 'Pair2':
            url = get_backend_url('/add/test=test')
            response = requests.get(url)
            if response.status_code == 200:
                return render_template('add.html', response=response)
        else:
            return render_template("add.html")
    elif request.method == 'GET':   
        return render_template("add.html")

@app.route('/list-keys')
def list_keys():
    url = get_backend_url('/list/keys')
    response = requests.get(url)
    if response.status_code == 200:
        return render_template('list-keys.html', response=response.json())
    return render_template('list-keys.html')


@app.route('/list-key-values')
def list_key_values():
    url = get_backend_url('/list/key-values')
    response = requests.get(url)
    if response.status_code == 200:
        return render_template('list-key-values.html', response=response.json())
    return render_template('list-key-values.html')


@app.route('/redis-info')
def redis_check():
    url = get_backend_url('/redis-info')
    response = requests.get(url)
    if response.status_code == 200:
        return render_template('redis-info.html', response=response.json())
    return render_template('redis-info.html')

