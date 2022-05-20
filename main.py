from flask import Flask
from flask import render_template
from flask import request
import pandas as pd
import joblib
import numpy as np

app = Flask(__name__)
app.config['MAX_CONTENT_LENGTH'] = 50 * 1000 * 1000