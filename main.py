from flask import Flask
from flask import render_template
from flask import request
import pandas as pd
import joblib
import numpy as np

app = Flask(__name__)
app.config['MAX_CONTENT_LENGTH'] = 50 * 1000 * 1000


@app.route('/', methods=['POST', 'GET'])
def homepage():
    return render_template('index.html')


@app.route('/form', methods=['POST', 'GET'])
def formpage():
    return render_template('form.html')


def transform_and_process_data(df):
    df.dropna(thresh=5, inplace=True)

    player_fifa_api_id = df['player_fifa_api_id'].unique() 