from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import joblib
import numpy as np
import os


# قراءة بيانات الاتصال من الـ environment
DB_USER     = os.getenv("POSTGRES_USER",     "abkar_user")
DB_PASSWORD = os.getenv("POSTGRES_PASSWORD", "123")
DB_HOST     = os.getenv("POSTGRES_HOST",     "localhost")
DB_PORT     = os.getenv("POSTGRES_PORT",     "5432")
DB_NAME     = os.getenv("POSTGRES_DB",       "ecommerce_db")

# تحميل النموذج عند بدء التشغيل
MODEL_PATH = os.path.join(
    os.path.dirname(__file__), "../../mlflow/satisfaction_model.pkl"
)

app   = FastAPI(title="E-Commerce Intelligence API", version="1.0")
model = joblib.load(MODEL_PATH)

# ── تعريف شكل الـ Request ──
class OrderFeatures(BaseModel):
    payment_value      : float   # قيمة الطلب
    delivery_days      : float   # أيام التسليم
    purchase_month     : int     # شهر الشراء (1-12)
    purchase_dayofweek : int     # يوم الأسبوع (0=Monday)

# ── تعريف شكل الـ Response ──
class PredictionResponse(BaseModel):
    low_satisfaction_probability : float
    prediction                   : str
    risk_level                   : str

@app.get("/")
def root():
    return {"message": "E-Commerce Intelligence API is running ✅"}

@app.get("/health")
def health():
    return {"status": "healthy", "model": "satisfaction_model_v1"}

@app.post("/predict/satisfaction", response_model=PredictionResponse)
def predict_satisfaction(order: OrderFeatures):
    try:
        # تجهيز البيانات بنفس ترتيب التدريب
        features = np.array([[
            order.payment_value,
            order.delivery_days,
            order.purchase_month,
            order.purchase_dayofweek
        ]])

        # التنبؤ
        prob       = model.predict_proba(features)[0][1]
        prediction = "low_satisfaction" if prob > 0.5 else "satisfied"

        # تحديد مستوى الخطر
        if prob > 0.7:
            risk = "HIGH"
        elif prob > 0.4:
            risk = "MEDIUM"
        else:
            risk = "LOW"

        return PredictionResponse(
            low_satisfaction_probability = round(float(prob), 3),
            prediction                   = prediction,
            risk_level                   = risk
        )

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))