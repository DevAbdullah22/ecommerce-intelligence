# 🛒 E-Commerce Intelligence Platform

An end-to-end data intelligence platform built on the Brazilian E-Commerce
(Olist) dataset (~100K real orders).

## 🏗️ Architecture

Data Engineering → EDA → Data Mining → ML Models → MLOps → Dashboard

## 📊 Key Results

| Analysis | Result |
|---|---|
| Total Orders Analyzed | 96,470 |
| Total Revenue | R$ 16M |
| Avg Review Score | 4.09 / 5.00 |
| Anomalies Detected | 4,933 orders |
| Satisfaction Model AUC | 0.698 |
| Revenue Forecast | R$ 60K/day by Nov 2018 |

## 🔑 Key Insights

1. **Delivery Time** is the #1 driver of customer dissatisfaction (82% feature importance)
2. **95%** of customers purchase only once — high churn by nature
3. **health_beauty** is the top revenue category (R$ 1.26M)
4. **Black Friday 2017** peak: 7,400+ orders in one month
5. **57.8%** of customers give 5-star reviews

## 🛠️ Tech Stack

| Layer | Technology |
|---|---|
| Data Engineering | pandas, PostgreSQL, SQLAlchemy |
| EDA & Visualization | matplotlib, seaborn, plotly |
| Data Mining | scikit-learn, mlxtend |
| ML Models | Prophet, XGBoost, TextBlob |
| MLOps | MLflow, FastAPI, Docker |
| Dashboard | Streamlit |

## 🚀 Quick Start

### 1. Setup Environment

```bash
conda create -n ecommerce-env python=3.11 -y
conda activate ecommerce-env
pip install -r requirements.txt
```

### 2. Run API

```bash
uvicorn src.api.main:app --reload --port 8000
```

### 3. Run Dashboard

```bash
streamlit run dashboard/app.py
```

### 4. Run with Docker

```bash
docker build -f docker/Dockerfile -t ecommerce-api .
docker run -p 8000:8000 ecommerce-api
```

## 📁 Project Structure

ecommerce-intelligence/
├── data/
│   ├── raw/          # Original CSV files
│   └── processed/    # Charts and outputs
├── notebooks/
│   ├── 01_EDA.ipynb
│   ├── 02_data_mining.ipynb
│   └── 03_modeling.ipynb
├── src/api/          # FastAPI service
├── dashboard/        # Streamlit app
├── mlflow/           # Trained models
├── docker/           # Dockerfile
└── tests/            # API tests

## 👤 Author

Abdullah (DevAbdullah22)
