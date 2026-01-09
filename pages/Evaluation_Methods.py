import streamlit as st
import base64

def get_image_base64(path):
    with open(path, "rb") as img_file:
        return base64.b64encode(img_file.read()).decode()

st.set_page_config(layout="wide", page_title="論文")

st.subheader("績效評估方法")
st.divider()
st.markdown("##### 1. 交叉驗證（Cross-Validation）")
st.markdown("* __五折交叉驗證__：將資料集分成五個子集，依次使用其中四個子集進行模型訓練，剩餘一個子集用於測試，重複五次以確保每個子集都被用作測試集，以增強結果穩定性與可信度。")
cv_img_base64 = get_image_base64("./images/cross_validation.png")
st.markdown(
    f"""
    <div style="display: flex; justify-content: center;">
        <img src="data:image/png;base64,{cv_img_base64}" width="500">
    </div>
    """,
    unsafe_allow_html=True
)

st.markdown("##### 2. 績效指標")
st.markdown('''
    * __平均絕對誤差（Mean Absolute Error, MAE）__：衡量預測值與實際值之間的平均絕對差異，反映模型預測的準確性。
    * __均方誤差（Mean Squared Error, MSE）__：計算預測值與實際值之間差異的平方的平均值，對較大誤差較為敏感。
    * __決定係數（R-squared, R²）__：表示模型解釋變異的比例，衡量模型對資料的擬合程度，範圍從 0 到 1，值越接近 1 表示模型表現越好。
''')

st.markdown("##### 3. 殘差圖（Residual Plot）")
st.markdown('''
    * 用於視覺化預測值與實際值之間的差異，輔助識別模型是否存在系統性偏差或異常點。
''')
rp_img_base64 = get_image_base64("./images/residual_plot.png")
st.markdown(
    f"""
    <div style="display: flex; justify-content: center;">
        <img src="data:image/png;base64,{rp_img_base64}" width="500">
    </div>
    """,
    unsafe_allow_html=True
)