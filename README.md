# 🛒 Walmart Store Item Sales Forecasting

![Python](https://img.shields.io/badge/Python-3.13-blue)
![FastAPI](https://img.shields.io/badge/FastAPI-0.115-green)
![React](https://img.shields.io/badge/React-19-blue)
![TypeScript](https://img.shields.io/badge/TypeScript-5.x-blue)
![Docker](https://img.shields.io/badge/Docker-Ready-blue)
![License](https://img.shields.io/badge/License-MIT-yellow)

A full-stack Machine Learning application that predicts future Walmart store-item sales using a trained regression model. The project provides a FastAPI backend for inference, a React + TypeScript frontend for user interaction, and an analytics dashboard for visualizing sales trends.

---

# 📌 Table of Contents

- Project Overview
- Features
- Demo
- Project Architecture
- Folder Structure
- Technology Stack
- Machine Learning Pipeline
- API Endpoints
- Installation
- Docker
- Dataset
- Screenshots
- Future Improvements
- License

---

# 📖 Project Overview

This project predicts future sales for a Walmart store and item based on:

- Date
- Store ID
- Item ID

The backend loads a trained Machine Learning model and exposes REST APIs through FastAPI.

The frontend provides:

- Sales prediction form
- Prediction results
- Interactive analytics dashboard
- Sales visualizations

The project follows a modular architecture suitable for production-ready ML applications.

---

# ✨ Features

## Backend

- FastAPI REST API
- Trained Machine Learning model
- Input validation using Pydantic
- Logging
- Modular project structure
- Docker support

---

## Frontend

- React + TypeScript
- Tailwind CSS
- Responsive UI
- Prediction Form
- Prediction Result
- Analytics Dashboard

---

## Analytics

- Monthly Sales Trend
- Weekly Sales Trend
- Store-wise Sales
- Item-wise Sales
- Sales Heatmap
- KPI Cards

---

# 🏗 Project Architecture

```
                +----------------------+
                |     React Frontend   |
                |                      |
                | Prediction Form      |
                | Analytics Dashboard  |
                +----------+-----------+
                           |
                    HTTP REST API
                           |
                           ▼
                +----------------------+
                |      FastAPI         |
                |                      |
                | /predict             |
                | /analytics           |
                +----------+-----------+
                           |
                    Prediction Engine
                           |
                           ▼
                +----------------------+
                | Trained ML Pipeline  |
                | Joblib Model         |
                +----------------------+
```

---

# 📂 Project Structure

```text
walmart_project/
│
├── data/
│   ├── raw/
│   └── processed/
│
├── frontend/
│   ├── src/
│   ├── public/
│   ├── package.json
│   └── Dockerfile
│
├── models/
│
├── notebooks/
│
├── src/
│   ├── api/
│   ├── preprocessing/
│   ├── training/
│   ├── prediction/
│   ├── config.py
│   ├── logger.py
│   └── predict.py
│
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
├── README.md
└── .gitignore
```

---

# 🛠 Technology Stack

## Backend

- Python
- FastAPI
- Scikit-Learn
- Pandas
- NumPy
- Joblib
- Pydantic

---

## Frontend

- React
- TypeScript
- Vite
- Tailwind CSS
- Axios
- Recharts

---

## DevOps

- Docker
- Docker Compose
- Git
- GitHub

---

# 🤖 Machine Learning Pipeline

The project follows a complete Machine Learning workflow.

```
Raw Dataset
      │
      ▼
Data Cleaning
      │
      ▼
Feature Engineering
      │
      ▼
Train/Test Split
      │
      ▼
Model Training
      │
      ▼
Model Evaluation
      │
      ▼
Model Serialization (.pkl)
      │
      ▼
FastAPI Inference
      │
      ▼
React Frontend
```

---

# 🌐 API Endpoints

## Home

```
GET /
```

Returns API information.

---

## Health

```
GET /health
```

Returns application health status.

---

## Prediction

```
POST /predict
```

Request

```json
{
    "date":"2018-01-01",
    "store":1,
    "item":5
}
```

Response

```json
{
    "predicted_sales":42.75
}
```

---

## Analytics

```
GET /analytics
```

Returns dashboard statistics including

- Average Sales
- Total Sales
- Monthly Sales
- Weekly Sales
- Store Sales
- Item Sales
- Heatmap Data

---

# 🚀 Installation

## Clone Repository

```bash
git clone git@github.com:inamullahcraker-cloud/Mall_sales_prediction.git

cd Mall-sales-prediction
```

---

## Backend

Create Virtual Environment

```bash
python -m venv .venv
```

Activate

Linux

```bash
source .venv/bin/activate
```

Windows

```bash
.venv\Scripts\activate
```

Install Dependencies

```bash
pip install -r requirements.txt
```

Run FastAPI

```bash
uvicorn src.api.api:app --reload
```

Backend

```
http://127.0.0.1:8000
```

Swagger

```
http://127.0.0.1:8000/docs
```

---

## Frontend

```bash
cd frontend
```

Install packages

```bash
npm install
```

Run

```bash
npm run dev
```

Frontend

```
http://localhost:5173
```

---

# 🐳 Docker

Build

```bash
docker compose build
```

Run

```bash
docker compose up
```

Backend

```
http://localhost:8000
```

Frontend

```
http://localhost:3000
```

---

# 📊 Dataset

The project uses the Walmart Store Item Sales Forecasting dataset.

Repository includes

- Raw dataset

Generated processed data is not included because it can be reproduced using the preprocessing pipeline.

---

# 📈 Model Performance

| Metric | Value |
|---------|-------|
| Model | Regression |
| Framework | Scikit-Learn |
| Prediction API | FastAPI |
| Frontend | React |



# 📸 Screenshots

## Home Page

> Add screenshot here

---

## Prediction

> Add screenshot here

---

## Analytics Dashboard

> Add screenshot here

---

# 🔮 Future Improvements

- Authentication
- Model versioning
- CI/CD using GitHub Actions
- Cloud Deployment
- Database Integration
- Real-time Forecasting
- Advanced Time-Series Models
- Monitoring Dashboard
- Automated Retraining Pipeline

---

# 👨‍💻 Author

**Inamullah**

Computer Science Student

ML Engineer

GitHub:

https://github.com/inamullahcraker-cloud

---

# 📄 License

This project is licensed under the MIT License.
