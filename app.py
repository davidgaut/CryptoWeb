
import io
import random
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.figure import Figure
from plotly.subplots import make_subplots
from flask import Flask, render_template, Response, request
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import pandas as pd
import json
import plotly
import plotly.express as px
import yfinance as yf


app = Flask(__name__)



#%% Get Crypto Data 
# Yfinance Crypto Codes
yf_dict = {'Bitcoin_Cash' 	:'BCH-USD',
'Binance_Coin' 	            :'BNB-USD',
'Bitcoin' 	                :'BTC-USD',
'EOS.IO' 	                :'EOS-USD',
'Ethereum_Classic'          :'ETC-USD',
'Ethereum' 	                :'ETH-USD',
'Litecoin' 	                :'LTC-USD',
'Monero' 	                :'XMR-USD',
'TRON' 	                    :'TRX-USD',
'Stellar' 	                :'XLM-USD',
'Cardano' 	                :'ADA-USD',
'IOTA' 	                    :'MIOTA-USD',
'Maker' 	                :'MKR-USD',
'Dogecoin' 	                :'DOGE-USD'}

# Last Quote
# @app.route('/bitcoin_price_single')
# def print_price_single():
#     quotes, df = get_last_quote(df)
#     return 'Last update at {:s}, the EU floating rate is {:.4f}.\n'.format(quotes)
import plotly.graph_objects as go

def plot_crypto(cm_name,yf_dict=yf_dict):
    '''Plot a cryptocurrency TS'''
    # obtain the Bitcoin ticker in USD
    cm = yf.Ticker(yf_dict[cm_name])
    # save the historical market data to a dataframe
    cm_values = cm.history(start="2020-09-21")
    cm_values
    # fig = px.line(cm_values, y=["High","Close","Low"], x=cm_values.index,title=cm_name)

    fig = make_subplots(rows=2, cols=1)
    for col in ['Low','Close','High']:
        fig.add_trace(
            go.Scatter(y=cm_values[[col]].values.ravel(), x=cm_values.index, name=col),
            row=1, col=1
        )
    fig.update_yaxes(title_text="Dollars", row=1, col=1)

    fig.add_trace(
        go.Scatter(y=cm_values[["Volume"]].values.ravel(), x=cm_values.index, name='Volume'),
        row=2, col=1
    )
    fig.update_yaxes(title_text="Units", row=2, col=1)
    fig.update_xaxes(title_text="Date", row=2, col=1)
    fig.update_layout(title=cm_name,height=1600//2, width=1200,
                   xaxis_title='',
                   yaxis_title='')

    graphJSON = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
    print(fig.data[0])
    return graphJSON

@app.route('/callback', methods=['POST', 'GET'])
def cb():
    return plot_crypto(request.args.get('data'))

@app.route('/CryptoPlot')
def make_plot(cc='Bitcoin'):
    return render_template('chartsajax.html',  graphJSON=plot_crypto(cc))
