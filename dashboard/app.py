import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from sqlalchemy import create_engine

# ── إعداد الصفحة ──
st.set_page_config(
    page_title="E-Commerce Intelligence",
    page_icon="🛒",
    layout="wide"
)

# ── الاتصال بقاعدة البيانات ──
@st.cache_resource  # يحفظ الاتصال في الذاكرة بدل ما يعيده كل مرة
def get_engine():
    return create_engine(
        "postgresql://abkar_user:123@localhost:5432/ecommerce_db"
    )

# ── تحميل البيانات مع cache ──
@st.cache_data  # يحفظ البيانات بدل ما يحملها كل مرة
def load_data():
    engine = get_engine()

    orders = pd.read_sql("""
        SELECT order_id, customer_id, order_status,
               order_purchase_timestamp
        FROM orders
        WHERE order_status = 'delivered'
    """, engine)

    payments = pd.read_sql(
        "SELECT order_id, payment_value FROM payments", engine
    )

    reviews = pd.read_sql(
        "SELECT order_id, review_score FROM reviews", engine
    )

    items = pd.read_sql(
        "SELECT order_id, product_id, price FROM order_items", engine
    )

    orders["order_purchase_timestamp"] = pd.to_datetime(
        orders["order_purchase_timestamp"]
    )

    return orders, payments, reviews, items

# ── تحميل البيانات ──
orders, payments, reviews, items = load_data()

# ربط الجداول
df = orders.merge(payments, on="order_id", how="left")
df["month"] = df["order_purchase_timestamp"].dt.to_period("M").astype(str)

# ── Header ──
st.title("🛒 E-Commerce Intelligence Platform")
st.markdown("**Brazilian E-Commerce (Olist) — ~100K Orders Analysis**")
st.divider()

# ── KPI Cards ──
col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric(
        label="📦 Total Orders",
        value=f"{len(orders):,}"
    )

with col2:
    total_rev = payments["payment_value"].sum()
    st.metric(
        label="💰 Total Revenue",
        value=f"R$ {total_rev/1e6:.2f}M"
    )

with col3:
    avg_score = reviews["review_score"].mean()
    st.metric(
        label="⭐ Avg Review Score",
        value=f"{avg_score:.2f} / 5.00"
    )

with col4:
    avg_order = payments["payment_value"].mean()
    st.metric(
        label="🛍️ Avg Order Value",
        value=f"R$ {avg_order:.0f}"
    )

st.divider()

# ── الرسوم البيانية ──
col_left, col_right = st.columns(2)

with col_left:
    st.subheader("📈 Monthly Revenue Trend")
    monthly = df.groupby("month")["payment_value"].sum().reset_index()
    fig = px.line(
        monthly, x="month", y="payment_value",
        labels={"payment_value": "Revenue (R$)", "month": "Month"}
    )
    fig.update_traces(line_color="#aa96da", line_width=2)
    st.plotly_chart(fig, use_container_width=True)

with col_right:
    st.subheader("⭐ Review Score Distribution")
    score_counts = reviews["review_score"].value_counts().sort_index()
    fig2 = px.bar(
        x=score_counts.index,
        y=score_counts.values,
        labels={"x": "Score", "y": "Count"},
        color=score_counts.index,
        color_continuous_scale=["#e74c3c","#e67e22","#f1c40f","#2ecc71","#27ae60"]
    )
    st.plotly_chart(fig2, use_container_width=True)

st.divider()

# ── Satisfaction Predictor ──
st.subheader("🤖 Live Satisfaction Predictor")
st.markdown("تنبأ برضا العميل قبل التسليم")

import requests

pred_col1, pred_col2 = st.columns(2)

with pred_col1:
    payment_val  = st.slider("💳 Payment Value (R$)", 10, 2000, 150)
    delivery_d   = st.slider("🚚 Delivery Days",       1,   60,  12)

with pred_col2:
    month        = st.selectbox("📅 Purchase Month", range(1, 13), index=10)
    day_of_week  = st.selectbox("📆 Day of Week",
                                ["Monday","Tuesday","Wednesday",
                                 "Thursday","Friday","Saturday","Sunday"])
    dow_map      = {"Monday":0,"Tuesday":1,"Wednesday":2,
                    "Thursday":3,"Friday":4,"Saturday":5,"Sunday":6}

if st.button("🔮 Predict Satisfaction", type="primary"):
    try:
        response = requests.post(
            "http://localhost:8000/predict/satisfaction",
            json={
                "payment_value"      : payment_val,
                "delivery_days"      : delivery_d,
                "purchase_month"     : month,
                "purchase_dayofweek" : dow_map[day_of_week]
            }
        )
        result = response.json()
        prob   = result["low_satisfaction_probability"]
        risk   = result["risk_level"]

        # عرض النتيجة
        if risk == "LOW":
            st.success(f"✅ LOW RISK — {prob*100:.1f}% chance of dissatisfaction")
        elif risk == "MEDIUM":
            st.warning(f"⚠️ MEDIUM RISK — {prob*100:.1f}% chance of dissatisfaction")
        else:
            st.error(f"🚨 HIGH RISK — {prob*100:.1f}% chance of dissatisfaction")

    except:
        st.error("❌ API غير متاح — تأكد إن الـ FastAPI شغال على port 8000")