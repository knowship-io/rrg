import yfinance as yf
import pandas as pd

def get_tickers_dataframe(tickers:list, period:str = '1mo', interval:str = '1d')-> pd.DataFrame:
    """
    Fetch ticker symbol data from yahoo finance.

    KWARGS
    tickers -- list of tickers to fetch information for
    period  -- (optional, default is '1mo') data retrival time horizon
               valid periods: 1d,5d,1mo,3mo,6mo,1y,2y,5y,10y,ytd,max
    interval -- (optional, default is '1d') fetch data by interval (including intraday if period < 60 days)
                valid intervals: 1m,2m,5m,15m,30m,60m,90m,1h,1d,5d,1wk,1mo,3mo
    """
    data = yf.download(  # or pdr.get_data_yahoo(...
        # tickers list or string as well
        tickers = " ".join(tickers),

        # use "period" instead of start/end
        # valid periods: 1d,5d,1mo,3mo,6mo,1y,2y,5y,10y,ytd,max
        # (optional, default is '1mo')
        period = period,

        # fetch data by interval (including intraday if period < 60 days)
        # valid intervals: 1m,2m,5m,15m,30m,60m,90m,1h,1d,5d,1wk,1mo,3mo
        # (optional, default is '1d')
        interval = interval,

        # group by ticker (to access via data['SPY'])
        # (optional, default is 'column')
        group_by = 'ticker',

        # adjust all OHLC automatically
        # (optional, default is False)
        auto_adjust = True,

        # use threads for mass downloading? (True/False/Integer)
        # (optional, default is True)
        threads = True,

        # proxy URL scheme use use when downloading?
        # (optional, default is None)
        proxy = None
    )

    return data
