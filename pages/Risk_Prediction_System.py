import streamlit as st
import requests
import pandas as pd

API_URL = "http://localhost:8000/predict"

st.set_page_config(layout="wide", page_title="論文")

st.subheader("跌倒風險預測系統")

# 1. 檔案上傳元件
uploaded_file = st.file_uploader("請上傳病患資料（僅限 CSV 格式）", type=["csv"])

if uploaded_file is not None:
    # 顯示上傳的資料預覽
    df_input = pd.read_csv(uploaded_file)
    st.write("檔案預覽：", df_input.head())

    if st.button("開始預測"):
        # 將檔案指標重置（因為讀取預覽時已經移動過指標）
        uploaded_file.seek(0)
        
        # 2. 封裝檔案準備發送
        files = {"file": (uploaded_file.name, uploaded_file.getvalue(), "text/csv")}
        
        with st.spinner('模型分析中，請稍候...'):
            try:
                response = requests.post(API_URL, files=files)
                
                if response.status_code == 200:
                    results = response.json()
                    df_result = pd.DataFrame(results)
                    
                    st.success("預測完成！")
                    
                    # 3. 顯示結果表格
                    st.subheader("預測結果")
                    st.dataframe(df_result)
                    
                    # 4. 提供下載功能
                    csv = df_result.to_csv(index=False).encode('utf-8')
                    st.download_button(
                        label="下載完整預測報告",
                        data=csv,
                        file_name="patient_predictions.csv",
                        mime="text/csv",
                    )
                else:
                    st.error(f"預測失敗：{response.text}")
            except Exception as e:
                st.error(f"連線錯誤: {e}")