from fastapi import FastAPI, UploadFile, File, HTTPException
import pandas as pd
import io
from joblib import load

app = FastAPI()

# 載入模型
import os
# 取得當前檔案所在的資料夾路徑
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
model_path = os.path.join(BASE_DIR, "model_pkl", "Y1_Y1_off_stacking_model.pkl")

try:
    model = load(model_path)
    print("Model loaded successfully.")
except FileNotFoundError:
    print("Error: model.pkl not found. Make sure the model is saved.")
    model = None

@app.post("/predict")
async def predict_batch(file: UploadFile = File(...)):
    # 1. 檢查檔案格式
    if not file.filename.endswith('.csv'):
        raise HTTPException(status_code=400, detail="僅支援 CSV 檔案")

    # 2. 讀取檔案內容
    contents = await file.read()
    df = pd.read_csv(io.BytesIO(contents))

    # 3. 數據預處理 (確保欄位順序與訓練時一致)
    if 'Tinetti' in df.columns:
        df = df.drop(columns=['Tinetti'])

    try:
        # 假設模型直接接受 DataFrame 或轉換為陣列
        predictions = model.predict(df)
        
        # 4. 將預測結果併入原表格並回傳
        df['prediction_Tinetti_result'] = predictions
        
        # 轉換成字典格式回傳給前端
        return df.to_dict(orient='records')
        
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"預測過程中出錯: {str(e)}")\
        
# 4. 運行 Flask 應用
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
    
if model is None:
    raise HTTPException(status_code=500, detail="模型未加載，請檢查伺服器配置。")
