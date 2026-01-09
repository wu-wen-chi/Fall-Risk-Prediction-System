import streamlit as st
import base64

# 用於讀取並轉換圖片為 base64 編碼
def get_image_base64(path):
    with open(path, "rb") as img_file:
        return base64.b64encode(img_file.read()).decode()

st.set_page_config(layout="wide", page_title="論文")

st.subheader("特徵工程與說明")
st.divider()
st.markdown("##### 1. 如何提取特徵？")

st.markdown('''
    * 以 30 hz 的取樣頻率結合骨骼追蹤演算法，紀錄受試者 25 個關節在三維空間上的步態週期變化。
    * 為了避免造成特徵維度不一致問題，研究中統一擷取每位受試者連續兩個完整步態週期做分析區間。
''')

kinnetv2_img_base64 = get_image_base64("./images/Kinectv2_human_joint.png")
st.markdown(
    f"""
    <div style="display: flex; justify-content: center;">
        <img src="data:image/png;base64,{kinnetv2_img_base64}" width="400">
    </div>
    """,
    unsafe_allow_html=True
)
    
st.divider()

st.markdown("##### 2. 如何提取步態週期？")

# 建立 2 個欄位，比例設為 [1, 1] 
col1, col2 = st.columns([1, 1])

with col1:
    st.markdown('''
    * 計算左右腳距離：計算左右腳間在 z 軸上的距離變化，行程波形訊號。
    * 找出谷值：根據波形訊號找出交叉點索引，作為谷值位置。
    * 找出峰值：在每兩個交叉點間找出距離最大值作為峰值。
    * 確定步態週期起始點：設定初始峰值（ >= 0.2 ），並找到相應初始的谷值最為步態週期起始點。
    * 組合峰值與谷值：將峰值與谷值依序排序，形成完整步態週期起始點集合。
    * 分割步態週期：以五個點作為一個步態週期（即 2 個峰值與 3 個谷值）。
    ''')

with col2:
    st.video("./vedio/gait_cycle.mp4")

st.divider()

st.markdown("##### 3. 特徵分類表")

st.markdown("* __步態時空參數__：基於步態時空參數，量化受試者的行走模式，進而反映其步態節奏性與穩定性。")

gait_img_base64 = get_image_base64("./images/gait_parameters.png")
st.markdown(
    f"""
    <div style="display: flex; justify-content: center;">
        <img src="data:image/png;base64,{gait_img_base64}" width="500">
    </div>
    """,
    unsafe_allow_html=True
)

st.markdown("* __關節活動範圍角度__：以向量點積方式計算各個關節在完整步態週期內的最大最小角度差，作為活動範圍特徵，以反應關節運動幅度。")

rom_img_base64 = get_image_base64("./images/rom_parameters.png")
st.markdown(
    f"""
    <div style="display: flex; justify-content: center;">
        <img src="data:image/png;base64,{rom_img_base64}" width="600">
    </div>
    """,
    unsafe_allow_html=True
)