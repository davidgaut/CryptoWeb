#%% Make simple prediction pipeline
from datetime import datetime
from sklearn.preprocessing import StandardScaler, OrdinalEncoder
from sklearn.impute import SimpleImputer
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression
from datetime import datetime
import yfinance as yf
import pandas as pd
from joblib import dump, load

# %%
# Yfinance Crypto Codes
yf_dict = {
'Bitcoin_Cash' 	            :'BCH-USD',
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

# %% Pipeline
categorical_features = ['Asset_ID']
numeric_features = ['Open', 'High', 'Low', 'Close', 'Volume', 'Date']

numeric_transformer = Pipeline(steps =[
                                    ("imputer", SimpleImputer(strategy="mean", )), # to deal with missing numeric data
                                    ("scaling", StandardScaler())
                                    ])

categorical_transformer = Pipeline(steps=[
                                    ("imputer", SimpleImputer(strategy="constant", fill_value=0)),
                                    ("onehot", OrdinalEncoder())
                                    ]) # to deal with missing categorical data 
                                    
preproc = ColumnTransformer(transformers=[("num", numeric_transformer, numeric_features),
                                          ("cat", categorical_transformer, categorical_features)])

name, model = ("linear", LinearRegression())
pipe = Pipeline(steps=[('preprocessor', preproc), (name, model)])

# Make data set
tickers = list(yf_dict.values())
def make_X(tickers):
    table = pd.DataFrame()
    for tick in tickers:
        tmp = yf.Ticker(tick).history(start="2020-09-21")
        tmp['Asset_ID'] = tick
        table = pd.concat((table,tmp))
    try:
        table = table.drop(columns=['Dividends','Stock Splits'])
    except Exception as e:
        print('Nothing Dropped')

    X   = table.reset_index().iloc[1:]
    idx = X['Date']
    X['Date'] = X['Date'].apply(lambda X: datetime.strftime(X,'%m'))
    X['Timestamp'] = idx
    X = X.set_index('Timestamp')
    y = table.Close.shift(1).iloc[1:]
    return X, y

X, y = make_X(tickers)

# Fit simple pipeline
pipe.fit(X,y)

# Save model
dump(pipe, 'simple_model.joblib')
pipe = load('simple_model.joblib') 