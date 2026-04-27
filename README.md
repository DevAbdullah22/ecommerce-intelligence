# 🛒 E-Commerce Intelligence Platform

An end-to-end Data Science and Machine Learning project built on the Brazilian
E-Commerce (Olist) dataset (~100K real orders).

---

## Business Problem

E-commerce companies generate massive volumes of transactional data daily,
but most businesses struggle to convert this data into strategic decisions.

This project solves key challenges:

- Identifying high-value customers
- Predicting customer satisfaction
- Detecting abnormal transactions
- Forecasting future sales
- Understanding customer sentiment

---

## Tech Stack

| Layer | Technology |
|---|---|
| Language | Python 3.11 |
| Data | Pandas, NumPy, SQLAlchemy |
| Database | PostgreSQL |
| Visualization | Matplotlib, Seaborn, Plotly |
| ML Models | Scikit-learn, XGBoost, Prophet |
| NLP | TextBlob, Deep-Translator |
| Experiment Tracking | MLflow |
| API | FastAPI |
| Dashboard | Streamlit |
| DevOps | Docker, Docker Compose, Git |

---

## Dataset

**Olist Brazilian E-Commerce Dataset** — 9 CSV files containing:

- 96,470 delivered orders
- 99,441 customers
- 112,650 order items
- 98,410 reviews
- 32,951 products

---

## Project Architecture

```text
Raw CSV Data
     ↓
Data Cleaning + PostgreSQL ETL
     ↓
EDA + Visualization
     ↓
Data Mining (RFM, Clustering, Apriori, Anomaly Detection)
     ↓
ML Models (Forecasting, Satisfaction, Sentiment, Recommendations)
     ↓
MLflow Experiment Tracking
     ↓
FastAPI Model Serving
     ↓
Streamlit Dashboard
     ↓
Docker Deployment
```

---

## Folder Structure

```text
ecommerce-intelligence/
├── dashboard/
│   └── app.py                  # Streamlit Dashboard
├── data/
│   ├── raw/                    # Original CSV files
│   └── processed/              # Charts and outputs
├── docker/
│   ├── Dockerfile              # API container
│   └── Dockerfile.jupyter      # Jupyter container
├── notebooks/
│   ├── 01_EDA.ipynb            # EDA + Data Cleaning + ETL
│   ├── 02_data_mining.ipynb    # RFM, Clustering, Apriori, Anomaly
│   └── 03_modeling.ipynb       # ML Models + MLflow
├── src/api/
│   └── main.py                 # FastAPI service
├── mlflow/                     # Trained models + experiments
├── tests/
│   └── test_api.py             # API tests
├── docker-compose.yml
├── requirements.txt            # API dependencies
├── requirements_full.txt       # Full environment dependencies
├── .env                        # Environment variables
└── README.md
```

---

## Machine Learning Modules

### 1. Customer Segmentation

- **RFM Analysis** → 4 segments: Champions, Loyal, Potential, At Risk
- **K-Means Clustering** → 4 clusters: High Value, Frequent, Recent, Inactive

### 2. Association Rules

- **Apriori Algorithm** → Product category co-purchase analysis
- Key insight: 95% of customers purchase only once

### 3. Anomaly Detection

- **Isolation Forest** → 4,933 suspicious transactions detected (5%)

### 4. Sales Forecasting

- **Prophet** → Daily revenue forecast, 90-day horizon
- Key insight: R$60K/day projected by end of 2018

### 5. Satisfaction Prediction

- **XGBoost Classifier** → ROC-AUC: 0.698
- Key insight: delivery_days drives 82% of satisfaction decisions

### 6. Sentiment Analysis

- **TextBlob + Google Translate** → 53% positive, 10% negative
- Validated against review scores (1-5 stars)

### 7. Recommendation System

- **Cosine Similarity** → Category-based recommendations
- 93,350 customers × 72 product categories matrix

---

## Key Business Insights

🚚 Delivery time = #1 driver of customer dissatisfaction (82%)

👥 95% of customers purchase only once — high natural churn

💄 health_beauty = top revenue category (R$ 1.26M)

🔍 4,933 suspicious orders detected automatically

📈 Growth forecast: R$ 60K/day by Nov 2018

⭐ 57.8% of customers give 5-star reviews

📅 Monday & Tuesday = highest sales days

🛒 November 2017 peak = Black Friday effect
---

## API Endpoints

### Health Check

```http
GET /health
```

### Predict Customer Satisfaction

```http
POST /predict/satisfaction

{
  "payment_value": 150.0,
  "delivery_days": 25,
  "purchase_month": 11,
  "purchase_dayofweek": 1
}
```

**Response:**

```json
{
  "low_satisfaction_probability": 0.755,
  "prediction": "low_satisfaction",
  "risk_level": "HIGH"
}
```

---

## Quick Start

### Local Environment

```bash
# 1. Create environment
conda create -n ecommerce-env python=3.11 -y
conda activate ecommerce-env
pip install -r requirements_full.txt

# 2. Run API
uvicorn src.api.main:app --reload --port 8000

# 3. Run Dashboard
streamlit run dashboard/app.py
```

### Docker Environment

```bash
# Build and run all services
docker compose up --build

# Services:
# Jupyter  → http://localhost:8888
# API      → http://localhost:8000
# Postgres → localhost:5432
```

---

## Results Summary

| Analysis | Result |
|---|---|
| Orders Analyzed | 96,470 |
| Total Revenue | R$ 16M |
| Avg Review Score | 4.09 / 5.00 |
| Anomalies Detected | 4,933 |
| Satisfaction AUC | 0.698 |
| Revenue Forecast | R$ 60K/day |
| Customer Segments | 4 |

---

## Author

**Abdullah (DevAbdullah22)**  
Software Engineer  
Machine Learning · Data Science · Full-Stack Developer
