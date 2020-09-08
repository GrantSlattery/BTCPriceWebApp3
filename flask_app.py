#https://grantslattery.pythonanywhere.com/
#https://www.pythonanywhere.com/user/grantslattery/.../mysite/flask_app.py

import dash
import dash_core_components as dcc
import dash_html_components as html

import pandas as pd
import requests

bitcoin_api_url = 'https://api.coindesk.com/v1/bpi/currentprice.json'
response = requests.get(bitcoin_api_url)
response_json = response.json()

#First round of raw data cleaning
priceData = response_json.get("bpi")
timeStamp = response_json.get("time")


#Create Dash Table Data Frame with priceData variable
newpdFrame = pd.DataFrame(data=priceData)
usdData = priceData.get("USD")
gbpData = priceData.get("GBP")
eurData = priceData.get("EUR")

usdBtcPrice = usdData.get("rate")
gbpBtcPrice = gbpData.get("rate")
eurBtcPrice = eurData.get("rate")

usaTime = timeStamp.get("updated")
isoTime = timeStamp.get("updatedISO")
ukTime = timeStamp.get("updateduk")

# for deployment, pass app.server (which is the actual flask app) to WSGI etc
app = dash.Dash()

app.layout = html.Div(children=[
    html.H1(children='BTC Price'),

    html.Div(children='''
        BTC Price: A web application for the value of one Bitcoin.
    '''),
    html.Div(children='''
        API & data Powered by CoinDesk: https://www.coindesk.com/price/bitcoin
    '''),


    html.H1(children="The value of one Bitcoin is:"),


    html.H4(children="Last updated: ["+usaTime +" / "+ ukTime +" / "+ isoTime+"]"),


    html.H2(children="$" + usdBtcPrice + " USD"),


    html.H2(children="£" + gbpBtcPrice + " GBP"),


    html.H2(children="€" + eurBtcPrice + " EUR"),

])


