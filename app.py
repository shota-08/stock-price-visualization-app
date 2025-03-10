import pandas as pd
import yfinance as yf
import altair as alt
import streamlit as st
import time

st.title("投信価格 可視化アプリ")

st.sidebar.write("""
# 投信価格
投資信託の価格可視化ツールです。以下のオプションから表示日数を指定できます。
""")

st.sidebar.write("""
## 表示日数選択
""")

days = st.sidebar.slider("日数", 1, 100, 20)

st.write(f"""
### 過去 **{days}日間** の価格
""")

def get_data(days, tickers):
    df = pd.DataFrame()
    for index in tickers.keys():
        tkr = yf.Ticker(tickers[index])
        time.sleep(2)
        hist = tkr.history(period=f'{days}d')
        hist.index = hist.index.strftime("%d %B %Y")
        hist = hist[["Close"]]
        hist.columns = [index]
        hist = hist.T
        hist.index.name = "Name"
        df = pd.concat([df, hist])
    return df

try:
    st.sidebar.write("""
    ## 価格の範囲指定
    """)
    ymin, ymax =  st.sidebar.slider(
        "範囲を指定してください",
        0.0, 50000.0, (0.0, 50000.0)
    )

    tickers = {
        "S&P500": "2558.T",      # 東証ETF - S&P500
        "全世界平均": "2559.T",   # 東証ETF - MSCIオールカントリー
        "日経平均": "1321.T",     # 東証ETF - 日経平均
        "TOPIX": "1308.T",       # 東証ETF - TOPIX
        "FANG+": "316A.T",       # 東証ETF - FANG+
        "NASDAQ100": "2568.T",   # 東証ETF - NASDAQ100
        "米国総合株式": "2557.T", # 東証ETF - 米国総合株式（VTI連動）
        "新興国株式": "1658.T",   # 東証ETF - MSCIエマージング（新興国株）
        "金": "1540.T"           # 東証ETF - 純金信託（金価格連動型）
    }

    df = get_data(days, tickers)
    index = st.multiselect(
        "投資信託を選択してください",
        list(df.index),
        ['S&P500', '全世界平均']
    )

    if not index:
        st.error("投資信託を選択してください")
    else:
        data = df.loc[index]
        st.write("### 価格 (JPY)", data.sort_index())
        data = data.T.reset_index()
        data = pd.melt(data, id_vars=["Date"]).rename(
            columns={"value":"Prices (JPN)"}
        )
        chart = (
            alt.Chart(data)
            .mark_line(opacity=0.8, clip=True)
            .encode(
                x="Date:T",
                y=alt.Y("Prices (JPN)", stack=None, scale=alt.Scale(domain=[ymin, ymax])),
                color="Name:N"
            )
        )
        st.altair_chart(chart, use_container_width=True)
except Exception as e:
    st.error(f"error: {e}")