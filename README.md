# 📊 Rossmann Retail Analytics Dashboard (AI-Powered)

An end-to-end data analytics and business intelligence project that analyzes Rossmann store sales data using an interactive Streamlit dashboard, MySQL database integration, and AI-powered insights.

---

## 🚀 Project Overview

This project provides a **business-focused analytics dashboard** to explore sales performance, customer behavior, promotions, and competition impact.

It also integrates **AI-generated insights** to deliver dynamic business recommendations based on real-time filtered data.

---

## 🧠 Key Features

- 📊 Interactive dashboard built with Streamlit
- 🔎 Advanced filters (Store Type, Date Range, Promotion, Holiday, Competition Distance)
- 📈 Time-series analysis (daily trends, seasonality)
- 👥 Customer behavior & revenue analysis
- 🎯 Promotion impact analysis
- 🧭 Competition distance impact
- 🏪 Top & bottom store performance tracking
- 🤖 AI-powered business insights using LLM API
- 🛢️ MySQL database integration (replacing static CSV files)
- 📥 Download filtered data as CSV

---

## 🏗️ Tech Stack

- Python (Pandas, NumPy)
- Streamlit (Dashboard)
- Matplotlib & Seaborn (Visualization)
- MySQL (Database)
- OpenAI API (AI Insights)
- dotenv (Environment management)

---

## 📁 Project Structure
rossmann-dashboard/
│
├── Interface.py # Streamlit dashboard
├── analysis.py # Data processing & visualization
├── ai_utils.py # AI recommendations
├── .env # API keys (not pushed)
├── requirements.txt
├── train.csv
├── store.csv


---

## ⚙️ Setup Instructions

### 1️⃣ Clone the repository

```bash
git clone https://github.com/your-username/rossmann-dashboard.git
cd rossmann-dashboard

2️⃣ Install dependencies
pip install -r requirements.txt

3️⃣ Setup environment variables

Create a .env file:

OPENAI_API_KEY=your_api_key

4️⃣ Run the application
streamlit run app.py

📊 Dashboard Sections
📌 Executive Summary
KPIs (Sales, Customers, Revenue)
Overall performance overview

🔍 Key Insights
Store performance
Promotion effectiveness
Customer behavior patterns

🎯 Recommendations
AI-generated business strategies
Data-driven decision suggestions

💡 Business Value
Helps identify top-performing stores
Evaluates effectiveness of promotions
Understands customer purchasing patterns
Provides actionable insights for decision-making
