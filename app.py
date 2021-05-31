import streamlit as st
import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt
from numpy import mean, std
from utils.yf_utils import get_tickers_dataframe
from utils.jdk_rs_utils import rs_ratio, rs_momentum

st.title('Relative Rotation Graph w $SPY benchmark')

@st.cache
def load_data():
    
    spdr_tickers = [
        'XLB', 
        'XLE', 
        'XLF', 
        'XLI',
        'XLK',
        'XLP',
        'XLRE',
        'XLU',
        'XLV', 
        'XLY',
        'SPY'
    ]
    
    data = get_tickers_dataframe(tickers=spdr_tickers) 

    prices_df = pd.DataFrame()
    prices_df['XLF'] = data['XLF']['Close']
    prices_df['XLE'] = data['XLE']['Close']
    
    rs_ratio_df = rs_ratio(prices_df, data['SPY']['Close'])
    rm_momentum_df = rs_momentum(prices_df)
    
    return rs_ratio_df, rm_momentum_df

ratio, momentum = load_data()

st.subheader('JdK RS-Ratio')
st.dataframe(ratio)

print(ratio.columns)

st.subheader('JdK RS-Momentum')
st.dataframe(momentum)

fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)

# Move left y-axis and bottim x-axis to centre, passing through (0,0)
ax.spines['left'].set_position('center')
ax.spines['bottom'].set_position('center')

# Eliminate upper and right axes
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')

# Show ticks in the left and lower axes only
ax.xaxis.set_ticks_position('bottom')
ax.yaxis.set_ticks_position('left')


ax.plot(ratio['XLF_rs'], momentum['XLF_rm'], '-o', label='XLF')
ax.scatter(ratio['XLE_rs'][-1],momentum['XLE_rm'][-1], marker='s')

ax.plot(ratio['XLE_rs'], momentum['XLE_rm'], '-o', label='XLE')
ax.scatter(ratio['XLE_rs'][-1],momentum['XLE_rm'][-1], marker='s')

st.pyplot(fig)
