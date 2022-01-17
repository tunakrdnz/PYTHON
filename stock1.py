import yfinance as yf 
import streamlit as st
import pandas as pd 


st.write("""
# Simple Stock  Price App


Shown are the stock closing price and volume of Google!
""")

tickerSymbol = 'GOOGL'

tickerData = yf.Ticker(tickerSymbol)

tickerDf = tickerData.history(period='1d', start='2017-1-17', end='2022-1-17')

st.line_chart(tickerDf.Close)
st.line_chart(tickerDf.Volume)
