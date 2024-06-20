from flask import Flask, render_template, send_from_directory
import pandas as pd
from sqlalchemy import create_engine

app = Flask(__name__, static_folder='my-react-app/build/static', template_folder='templates')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/new-group')
def new_group():
    return render_template('new_group.html')

@app.route('/test')
def print_lucky():
    return 'lucky'

# おまじない
if __name__ == '__main__':
    app.run(host='0.0.0.0', port = 5000, debug = True)