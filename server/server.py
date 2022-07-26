from flask import Flask, request, render_template
from waitress import serve
import pandas as pd
import time
import re
import subprocess

def transform_data(df, is_image_exists = None, min_age = 0, max_age = 200):
    date_now = int(round(time.time()*1000))
    if is_image_exists == True:
        df.dropna(subset = ['img_path'], inplace=True)
    if min_age != None:
        date_min = int(date_now - float(min_age) * 365.25 * 24 * 60 * 60 * 1000)
        df = df.loc[df['birthts'] < date_min]
    if max_age != None:
        date_max = int(date_now - float(max_age) * 365.25 * 24 * 60 * 60 * 1000)
        df = df.loc[df['birthts'] > date_max]
    return df




app = Flask(__name__)

@app.route("/")
def get_start():
    return 'Start'

@app.route("/GET/data")
def get_data():
    is_image_exists = request.args.get('is_image_exists')
    min_age = request.args.get('min_age')
    max_age = request.args.get('max_age')
    df = pd.read_csv('all_data.csv')
    df = transform_data(df, is_image_exists=is_image_exists, min_age=min_age, max_age=max_age)
    return render_template('table_data.html',  tables=[df.to_html(classes='data')], titles=df.columns.values)

@app.route("/POST/data")
def post_data():
    add_data = request.args.get('add_data')
    if add_data == 'True':
        subprocess.Popen('add_data.py', shell=True)
    else:
        exec(open('main.py').read())
    return "Data successful post"

@app.route("/GET/stats")
def get_stats():
    is_image_exists = request.args.get('is_image_exists')
    min_age = request.args.get('min_age')
    max_age = request.args.get('max_age')
    df = pd.read_csv('all_data.csv')
    df = transform_data(df, is_image_exists=is_image_exists, min_age=min_age, max_age=max_age)
    date_now = int(round(time.time() * 1000))
    mean_year = (date_now - df['birthts'].mean())/365.25/24/60/60/1000
    return "Mean year: " + str(mean_year)


if __name__ == "__main__":
    serve(app, host="0.0.0.0", port=8080)