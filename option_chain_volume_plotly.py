import yfinance as yf
import time
import pandas as pd
import streamlit as st
import plotly.graph_objs as go

# 基本数据
ticker = 'spy'
date = '2023-09-08'
stock = yf.Ticker(ticker)
option_chain = stock.option_chain(date)
price = 450
screenshoot_time = time.ctime()

# 获取期权数据
calls = option_chain.calls
puts = option_chain.puts

# oi跟volume的和
calls_oi_sum = sum(calls['openInterest'])
puts_oi_sum = sum(puts['openInterest'])
calls_vol_sum = sum(calls['volume'])
puts_vol_sum = sum(puts['volume'])

# 差别计算
if calls_oi_sum > puts_oi_sum:
    difference = ((calls_oi_sum / puts_oi_sum) - 1) * 100
elif puts_oi_sum > calls_oi_sum:
    difference = ((puts_oi_sum / calls_oi_sum) - 1) * 100

# 画图
calls_oi_bar = go.Bar(x=calls['strike'], y=calls['openInterest'], name='call openInterest')
puts_oi_bar = go.Bar(x=calls['strike'], y=puts['openInterest'], name='put openInterest')
calls_vol_bar = go.Bar(x=calls['strike'], y=calls['volume'], name='call volume')
puts_vol_bar = go.Bar(x=calls['strike'], y=puts['volume'], name='put volume')
fig = go.Figure([calls_oi_bar, puts_oi_bar, calls_vol_bar, puts_vol_bar])
# 创建图形
fig = go.Figure([calls_oi_bar, puts_oi_bar, calls_vol_bar, puts_vol_bar])
# 标题
fig.update_layout(title=f'Options for {ticker} on {date} at {screenshoot_time}\n calls oi sum: {calls_oi_sum}    puts oi sum: {puts_oi_sum}\n ',
                  xaxis_title='strike price',
                  yaxis_title='openInterest')
# 范围
fig.update_xaxes(range=[price*0.97, price*1.03])

fig.show()

# {round(difference, 2)}% difference