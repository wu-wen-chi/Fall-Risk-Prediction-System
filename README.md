[![Built with](https://img.shields.io/badge/Built%20with-Stima%20API-blueviolet?logo=robot)](https://apertis.ai)

<img src="https://img.shields.io/badge/Python-3.8.8-blue"/>　<img src="https://img.shields.io/badge/Streamlit-pink"/>　<img src="https://img.shields.io/badge/FastAPI-green"/>　<img src="https://img.shields.io/badge/Pandas-lightblue"/>　<img src="https://img.shields.io/badge/github-gray"/>

# 論文介紹網站－跌倒風險預測系統

本專案是一個基於機器學習的跌倒風險預測系統，旨在透過步態分析與特徵工程，預測帕金森氏症患者的跌倒風險。系統包含前端網站與後端 API。

網站連結：https://fall-risk-prediction-system-jytyfpxot8fq7s7jcwhqtd.streamlit.app/

## 功能介紹

1. **跌倒風險預測系統**
   - 上傳病患數據（CSV 格式）。
   - 使用預訓練模型進行風險預測。
   - 提供預測結果的下載功能。

2. **研究方法展示**
   - 特徵工程與步態分析方法。
   - 交叉驗證與績效評估指標。

3. **資料可視化**
   - 步態參數與關節活動範圍的圖表展示。

## 系統架構

- **前端**：使用 [Streamlit](https://streamlit.io/) 建立互動式網頁。
- **後端**：使用 [FastAPI](https://fastapi.tiangolo.com/) 提供 API 服務。
- **機器學習模型**：基於 scikit-learn 訓練的跌倒風險預測模型，需先打包模型為pkl檔。

## 安裝與執行

### 1. 環境需求

- Python 3.8+
- pip 套件管理工具

### 2. 安裝步驟

1. Clone此專案到本地端：
   ```bash
   git clone https://github.com/wu-wen-chi/Fall-Risk-Prediction-System.git
   cd Fall-Risk-Prediction-System