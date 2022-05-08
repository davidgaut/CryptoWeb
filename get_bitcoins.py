import requests
def get_bitcoins():
    response = requests.get('https://api.coindesk.com/v1/bpi/currentprice.json')
    data = response.json()
    print(data)
    return data

def get_last_quote(df):
    data          = get_bitcoins()
    time_update   = data['time']['updated']
    rate_float_eu = data['bpi']['EUR']['rate_float']
    quotes = (time_update,rate_float_eu)
    df.append(quotes)
    return quotes, df
