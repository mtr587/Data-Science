import yfinance as yf
import matplotlib.pyplot as plt
import time
import pandas as pd

# 完成代码
# 设置股票代码和日期
# 过了晚上8:45就不能用
# 如果spy，qqq有一天预测不准，那么就停下来，看股票
# ticker = input("Enter stock you want to know: ")
# date = input("Enter date (YYYY-MM-DD): ")

ticker = 'spy'
date = '2023-09-06'

# 获取期权链数据
stock = yf.Ticker(ticker)
option_chain = stock.option_chain(date)
a = stock.info
# print(a)
for key, value in a.items():
    print(key, ':', value)

fix_price = 440

while True:
    # 提取期权数据
    calls = option_chain.calls
    puts = option_chain.puts

    pd.set_option('display.max_rows', None)
    pd.set_option('display.max_columns', None)
    # print(calls)
    calls_oi_sum = sum(calls['openInterest'])
    puts_oi_sum = sum(puts['openInterest'])
    calls_vol_sum = sum(calls['volume'])
    puts_vol_sum = sum(puts['volume'])
    print(calls_vol_sum)
    print(puts_vol_sum)

    if calls_oi_sum > puts_oi_sum:
        difference = ((calls_oi_sum / puts_oi_sum) - 1) * 100
    elif puts_oi_sum > calls_oi_sum:
        difference = ((puts_oi_sum / calls_oi_sum) - 1) * 100

    # 设置子图
    fig, (ax, ax2) = plt.subplots(2, 1, figsize=(10, 6))

    # 绘制oi柱状图
    width = 0.3
    call_bars = ax.bar(calls['strike'] - width, calls['openInterest'], color='blue', width=width, label='Call Optionss')
    put_bars = ax.bar(puts['strike'], puts['openInterest'], color='red',width=width, label='Put Options')

    screenshoot_time = time.ctime()
    ax.set_xlabel('Strike Price')
    ax.set_ylabel('Open Interest')
    ax.set_title(f'Options for {ticker} on {date} at {screenshoot_time}\n calls oi sum: {calls_oi_sum}    puts oi sum: {puts_oi_sum}\n ')
    ax.tick_params(axis='x', rotation=45)
    ax.bar_label(call_bars, fontsize=6)
    ax.bar_label(put_bars, fontsize=6)

    # 图标范围
    try:
        if ticker == 'spy' or ticker == 'qqq' or ticker == '^spx':
            ax.set_xlim(a['open']*0.97, a['open']*1.03)
        else:
            ax.set_xlim(a['open'] * 0.8, a['open'] * 1.2)
    except KeyError:
        # open不可用时目标范围
        ax.set_xlim(fix_price*0.97, fix_price*1.03)

    # 添加图例
    ax.legend()

    # 绘制volume柱状图
    width = 0.3
    call_bars = ax2.bar(calls['strike'] - width, calls['volume'], color='blue', width=width, label='Call Volume')
    put_bars = ax2.bar(puts['strike'], puts['volume'], color='red', width=width, label='Put Volume')

    screenshoot_time = time.ctime()
    ax2.set_xlabel('Strike Price')
    ax2.set_ylabel('Open Volume')
    # ax2.set_title(
        # f'calls volume sum: {calls_vol_sum}    puts volume sum: {puts_vol_sum}')
    ax2.tick_params(axis='x', rotation=45)
    ax2.bar_label(call_bars, fontsize=6)
    ax2.bar_label(put_bars, fontsize=6)

    # 图标范围
    try:
        if ticker == 'spy' or ticker == 'qqq' or ticker == '^spx':
            ax2.set_xlim(a['open'] * 0.97, a['open'] * 1.03)
        else:
            ax2.set_xlim(a['open'] * 0.8, a['open'] * 1.2)
    except KeyError:
        # open不可用时目标范围
        ax2.set_xlim(fix_price*0.97, fix_price*1.03)

    # 添加图例
    ax2.legend()


    # 调整布局
    plt.tight_layout()

    # 显示图表
    plt.show()

    time.sleep(5)

    plt.close()

# {round(difference, 2)}% difference