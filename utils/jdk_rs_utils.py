
def rs_ratio(prices_df, benchmark, window=1):
    
    for series in prices_df:
        rs = (prices_df[series].divide(benchmark)) * 100
        rs_ratio = rs.rolling(window).mean()
        rel_ratio = 100 + ((rs_ratio - rs_ratio.mean()) / rs_ratio.std() + 1)
        prices_df[f'{series}_rs'] = rel_ratio
    prices_df.dropna(axis=0, how='all', inplace=True)
    
    return prices_df

def rs_momentum(prices_df, window=1):
    
    for series in prices_df:
        rm = (prices_df[series].pct_change()) * 100
        rm_ratio = rm.rolling(window).mean()
        rel_ratio = 100 + ((rm_ratio - rm_ratio.mean()) / rm_ratio.std() + 1)
        prices_df[f'{series}_rm'] = rel_ratio
    prices_df.dropna(axis=0, how='all', inplace=True)
    
    return prices_df
