#%% Main file for Cloud computing Project
from get_bitcoins import get_last_quote
import plotly.graph_objects as go
from plotly.subplots import make_subplots
from flask import Flask, render_template, request
import json
import plotly
import yfinance as yf
from joblib import load
from make_model import make_X, yf_dict
import db

# Make App
app = Flask(__name__)

# Basic Prediction Model
pipe = load('simple_model.joblib') 

# Instantiate Database
db.init_db()

#%% Get Crypto Data 
# Last Quote
@app.route('/')
def print_price_single():
    df = list()
    quotes, df = get_last_quote(df)
    current = 'Last update at {:s}, the EU floating rate is {:.4f}.\n'.format(*quotes)
    print(current)
    return render_template('page_index.html',current=current)

def plot_crypto(cm_name,yf_dict=yf_dict):
    '''Plot a cryptocurrency TS'''
    # obtain the Bitcoin ticker in USD
    cm = yf.Ticker(yf_dict[cm_name])
    # save the historical market data to a dataframe
    cm_values = cm.history(start="2020-09-21")
    cm_values

    fig = make_subplots(rows=2, cols=1)
    for col in ['Low','Close','High']:
        fig.add_trace(
            go.Scatter(y=cm_values[[col]].values.ravel(), x=cm_values.index, name=col),
            row=1, col=1)
    fig.add_trace(
        go.Scatter(y=cm_values[["Volume"]].values.ravel(), x=cm_values.index, name='Volume'),
        row=2, col=1)
    fig.update_yaxes(title_text="Dollars", row=1, col=1)
    fig.update_yaxes(title_text="Units", row=1, col=1)
    fig.update_xaxes(title_text="Date", row=2, col=1)
    fig.update_layout(title=cm_name,height=1600//2, width=1200,
                   xaxis_title='', yaxis_title='')

    graphJSON = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
    print(fig.data[0])
    return graphJSON

@app.route('/history', methods=['POST', 'GET'])
def cb():
    return plot_crypto(request.args.get('data'))

@app.route('/history/<endpoint>')
def make_plot(endpoint,currency=yf_dict.keys()):
    return render_template('chartsajax.html',  graphJSON=plot_crypto(endpoint), currency=currency)

@app.route('/history_intermediary', methods=['POST', 'GET'])
def history_intermediary():
    return render_template('history_intermediary.html')

# Make predictions
@app.route('/prediction_intermediary', methods=['POST', 'GET'])
def prediction_intermediary():
    return render_template('prediction_intermediary.html')

# Store prediction
@app.route('/prediction/<currency>', methods=['GET'])
def prediction(currency : str):
    # Make Prediction of Close price for each currency
    tickers    = list([currency])
    X, y       = make_X(tickers)
    X_pred     = X.sort_index()[-len(tickers):]
    prediction = pipe.predict(X_pred)
    prediction = round(prediction[0],4)
    db.insert(currency.replace('-','_'),prediction)
    return render_template('chartsajax2.html',  prediction=prediction, currency=currency)

@app.route('/prediction_history')
def show_prediction_history():
    data = db.list()
    table = json.dumps(data,default=str)
    return render_template('show_table.html',  table=table)

def plot_crypto(cm_name,yf_dict=yf_dict):
    '''Plot a cryptocurrency TS'''
    # obtain the Bitcoin ticker in USD
    cm = yf.Ticker(yf_dict[cm_name])
    # save the historical market data to a dataframe
    cm_values = cm.history(start="2020-09-21")

    fig = make_subplots(rows=2, cols=1)
    for col in ['Low','Close','High']:
        fig.add_trace(
            go.Scatter(y=cm_values[[col]].values.ravel(), x=cm_values.index, name=col),
            row=1, col=1)
    fig.add_trace(
        go.Scatter(y=cm_values[["Volume"]].values.ravel(), x=cm_values.index, name='Volume'),
        row=2, col=1)
    fig.update_yaxes(title_text="Dollars", row=1, col=1)
    fig.update_yaxes(title_text="Units", row=1, col=1)
    fig.update_xaxes(title_text="Date", row=2, col=1)
    fig.update_layout(title=cm_name,height=1600//2, width=1200,
                   xaxis_title='', yaxis_title='')

    graphJSON = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
    print(fig.data[0])
    return graphJSON