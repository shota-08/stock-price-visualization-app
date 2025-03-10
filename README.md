# stock-price-visualization-app

## 🤔これは何？
- このアプリは、**投資信託の価格可視化ツール** です。
- **表示日数** や **価格範囲** を指定し、東証ETFの過去価格を可視化できます。

## 🔧環境構築方法
### 1. python 仮想環境の構築
```
py -m venv .venv
```

以下のコマンドを実行し、仮想環境を有効化してください
```
.\.venv\Scripts\activate
```

### 2. 必要なライブラリをインストール
```
pip install -r requirements.txt
```

### 3. アプリの起動
```
streamlit run main.py
```

## 🚀 機能
- 指定した日数分の価格を取得可能
- 価格範囲を自由に指定可能
- 複数の投資信託を比較・可視化
- サイドバーで操作

## 📊 取得可能な投資信託

| 名称 | ティッカー |
| ---- | ---- |
| S&P500 | 2558.T |
| 全世界平均 | 2559.T |
| 日経平均 | 1321.T |
| TOPIX | 1308.T |
| FANG+ | 316A.T |
| NASDAQ100 | 2568.T |
| 米国総合株式 | 2557.T |
| 新興国株式 | 1658.T |
| 金 | 1540.T |
