# import time

# import redis
# from flask import Flask

# app = Flask(__name__)
# cache = redis.Redis(host='redis', port=6379)

# def get_hit_count():
#     retries = 5
#     while True:
#         try:
#             return cache.incr('hits')
#         except redis.exceptions.ConnectionError as exc:
#             if retries == 0:
#                 raise exc
#             retries -= 1
#             time.sleep(0.5)

import io
import random
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.figure import Figure
from flask import Flask, render_template, Response, request
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
# from get_bitcoins import get_bitcoins
import pandas as pd
import json
import plotly
import plotly.express as px
import yfinance as yf

app = Flask(__name__)
df  = pd.DataFrame()

if __name__ == '__main__':
   app.run(debug = True)

@app.route('/', methods=['GET', 'POST'])
def list_pages():
    return render_template('page_index.html', title='Details')

@app.route('/test')
def chartTest():
    lnprice=np.log(price)
    plt.plot(lnprice)
    return render_template('index.html', name = plt.show())

@app.route('/plot.png')
def plot_png():
    fig = create_figure()
    output = io.BytesIO()
    FigureCanvas(fig).print_png(output)
    return Response(output.getvalue(), mimetype='image/png')

def create_figure():
    fig = Figure()
    axis = fig.add_subplot(1, 1, 1)
    xs = range(100)
    ys = [random.randint(1, 50) for x in xs]
    axis.plot(xs, ys)
    return fig

def get_last_quote(df):
    data          = get_bitcoins()
    time_update   = data['time']['updated']
    rate_float_eu = data['bpi']['EUR']['rate_float']
    quotes = (time_update,rate_float_eu)
    df.append(quotes)
    return quotes, df

@app.route('/bitcoin_price_single')
def print_price_single():
    quotes, df = get_last_quote(df)
    return 'Last update at {:s}, the EU floating rate is {:.4f}.\n'.format(quotes)


@app.route('/callback', methods=['POST', 'GET'])
def cb1():
    return gm1(request.args.get('data'))
   
@app.route('/id1')
def index1():
    return render_template('chartsajax.html',  graphJSON=gm1())

def gm1(country='United Kingdom'):
    df  = pd.DataFrame(px.data.gapminder())
    fig = px.line(df[df['country']==country], x="year", y="GDPperCap")
    
    graphJSON = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
    print(fig.data[0])
    return graphJSON

@app.route('/id2')
def index2():
    return render_template('index3.html')

@app.route('/callback/<endpoint>')
def cb2(endpoint):   
    if endpoint == "getStock":
        return gm2(request.args.get('data'),request.args.get('period'),request.args.get('interval'))
    elif endpoint == "getInfo":
        stock = request.args.get('data')
        st = yf.Ticker(stock)
        return json.dumps(st.info)
    else:
        return "Bad endpoint", 400

# Return the JSON data for the Plotly graph
def gm2(stock,period, interval):
    st = yf.Ticker(stock)
    # Create a line graph
    df = st.history(period=(period), interval=interval)
    df=df.reset_index()
    df.columns = ['Date-Time']+list(df.columns[1:])
    max = (df['Open'].max())
    min = (df['Open'].min())
    range = max - min
    margin = range * 0.05
    max = max + margin
    min = min - margin
    fig = px.area(df, x='Date-Time', y="Open",
        hover_data=("Open","Close","Volume"), 
        range_y=(min,max), template="seaborn" )

    # Create a JSON representation of the graph
    graphJSON = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
    return graphJSON

# Assign in posgreSQL


# %% Plot Crypto
cm_name='Bitcoin Cash'
@app.route('/CryptoPlots/<endpoint>')
def cb3(endpoint):   
    if endpoint == "Indiv":
        return plot_long_ts(cm_name,yf_dict)
    elif endpoint == "getInfo":
        stock = request.args.get('data')
        st = yf.Ticker(stock)
        return json.dumps(st.info)
    else:
        return "Bad endpoint", 400

# Yfinance Crypto Codes
yf_dict = {'Bitcoin Cash' 	:'BCH-USD',
'Binance Coin' 	            :'BNB-USD',
'Bitcoin' 	                :'BTC-USD',
'EOS.IO' 	                :'EOS-USD',
'Ethereum Classic'          :'ETC-USD',
'Ethereum' 	                :'ETH-USD',
'Litecoin' 	                :'LTC-USD',
'Monero' 	                :'XMR-USD',
'TRON' 	                    :'TRX-USD',
'Stellar' 	                :'XLM-USD',
'Cardano' 	                :'ADA-USD',
'IOTA' 	                    :'MIOTA-USD',
'Maker' 	                :'MKR-USD',
'Dogecoin' 	                :'DOGE-USD'}

import mplfinance as mpf


def plot_long_ts(cm_name,yf_dict):
    # obtain the Bitcoin ticker in USD
    cm = yf.Ticker(yf_dict[cm_name])
    # save the historical market data to a dataframe
    cm_values = cm.history(start="2020-09-21")

    fig = mpf.figure(figsize=(10, 7));
    fig = mpf.plot(cm_values,type='candle',volume=True,
            figratio=(3,1),style='yahoo',title=cm_name,)
    graphJSON = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
    print(fig.data[0])
    return graphJSON

def gm3(country='United Kingdom'):
    df  = pd.DataFrame(px.data.gapminder())
    fig = px.line(df[df['country']==country], x="year", y="GDPperCap")
    
    graphJSON = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
    print(fig.data[0])
    return graphJSON

import base64
from io import BytesIO

from flask import Flask
from matplotlib.figure import Figure
@app.route("/test11")
def hello():
    # obtain the Bitcoin ticker in USD
    cm = yf.Ticker(yf_dict[cm_name])
    # save the historical market data to a dataframe
    cm_values = cm.history(start="2020-09-21")
    # Generate the figure **without using pyplot**.
    fig = Figure()
    # fig = mpf.figure(figsize=(10, 7));
    ax = fig.subplots(2,1)
    # ax.plot([1, 2])
    mpf.plot(cm_values,type='candle',volume=ax[1],
            figratio=(3,1),style='yahoo',title=cm_name,ax=ax[0])
    # Save it to a temporary buffer.
    buf = BytesIO()
    fig.savefig(buf, format="png")
    # Embed the result in the html output.
    data = base64.b64encode(buf.getbuffer()).decode("ascii")
    return f"<img src='data:image/png;base64,{data}'/>"