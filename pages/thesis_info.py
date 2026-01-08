import streamlit as st

st.set_page_config(page_title="論文介紹")
# st.header("")
st.subheader("運用多維度步態特徵與機器學習演算法於帕金森氏症患者跌倒風險預測之長期性研究")
st.subheader("Using Multidimensional Gait Features and Machine Learning algorithms in the Fall Risk Prediction of the Parkinson’s Patients in the Longitudinal research")

st.divider()

st.markdown("<h5 style='text-align: center;'>摘要：</h5>", unsafe_allow_html=True)
st.markdown("""帕金森氏症為一種常見於高齡族群的慢性神經退化性疾病，其步態異常與跌倒風險密切相關。隨著病程進展，患者可能出現凍結步態與姿勢不穩等症狀，顯著提升跌倒風險。因此，本研究結合非侵入式Kinect 設備與機器學習技術，蒐集患者兩年度之三維空間數據，並擷取步態時空參數與關節活動範圍角度等多維特徵，以Tinetti 步態評估量表分數作為連續型預測目標。為探討單年度與跨年度資料對模型效能之影響，本研究建構四種模型（Y1-Y1， Y2-Y2， Y1-Y2， YC-Y2）， 並分別使用SVR 隨機森林迴歸 XGBoost LightGBM CatBoost與Stacking等六種迴歸模型進行跌倒風險預測。進一步運用 SHAP 方法量化特徵對模型預測結果之貢獻，進行模型解釋性分析。研究結果顯示，利用第一與第二年度資料預測第二年跌倒風險（YC-Y2）時展現出最為優異的預測能力。其中，CatBoost模型於藥前階段的MAE僅0.96；MSE為0.49；R²高達0.98，顯示其具備極高的預測準確性與穩定性；而藥後階段，CatBoost模型亦表現優異，模型績效的MAE僅0.89，； MSE為0.56；R²達 0.92。此結果顯示，跨年度資料整合有助於模型學習更全面的風險特徵，相較於僅使用單一年度資料訓練的模型更具穩定性與解釋力。特徵分析亦表明，步幅長度為模型幾乎一致選用之核心特徵，顯示其對跌倒風險具有高度的預測價值。上述結果證實長期資料結合多維步態特徵與先進機器學習技術，能有效提升帕金森氏症患者跌倒風險預測之準確性與穩定性，未來可作為臨床輔助評估工具，強化個別化風險管理與早期介入策略之發展。""")

st.divider()

st.markdown("<h6 style='text-align: center;'>實驗流程涵蓋藥前與藥後兩階段的步態測試，並由醫師進行步態量表分數評估</h6>", unsafe_allow_html=True)
# 建立 3 個欄位，比例設為 [1, 2, 1] (中間較寬)
col1, col2, col3 = st.columns([1, 2, 1])

with col2:
    st.image("./images/Experimental_space.png", caption="實驗空間與Kinect V2設備配置示意圖")

st.divider()