
def apply_vcp_filters(df):
    # Sample VCP logic from Chartink filters
    df = df.copy()
    df = df[
        (df['atr_14'] < df['atr_14_10d_ago']) &
        ((df['atr_14'] / df['close']) < 0.08) &
        (df['close'] > 0.75 * df['52w_high']) &
        (df['ema_50'] > df['ema_150']) &
        (df['ema_150'] > df['ema_200']) &
        (df['close'] > df['ema_50']) &
        (df['close'] > 10) &
        ((df['close'] * df['volume']) > 1000000)
    ]
    return df
