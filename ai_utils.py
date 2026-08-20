<<<<<<< HEAD
from langchain_mistralai import ChatMistralAI
import streamlit as st
from langchain_core.messages import HumanMessage
import os
from dotenv import load_dotenv

load_dotenv()

# client = ChatMistralAI(
#     api_key=os.getenv("MISTRAL_API_KEY"),
#     model="mistral-small"
# )
api_key = st.secrets.get("MISTRAL_API_KEY", os.getenv("MISTRAL_API_KEY"))

client = ChatMistralAI(
    api_key=api_key,
    model="mistral-small"
)

def generate_ai_recommendation(df):

    if df.empty:
        return "No data available for generating insights."

    total_sales = df["Sales"].sum()
    avg_sales = df["Sales"].mean()
    total_customers = df["Customers"].sum()

    promo_effect = df.groupby("Promo")["Sales"].mean().to_dict()
    holiday_effect = df.groupby("Holiday")["Sales"].mean().to_dict()

    prompt = f"""
You are a business analyst.

Analyze this retail dataset summary:

Total Sales: {total_sales}
Average Sales: {avg_sales}
Total Customers: {total_customers}
Promotion Impact: {promo_effect}
Holiday Impact: {holiday_effect}

Provide:
1. Key insights
2. Business recommendations

Keep it concise and professional.
"""

    response = client.invoke(
        [HumanMessage(content=prompt)]
    )

=======
from langchain_mistralai import ChatMistralAI
from langchain_core.messages import HumanMessage
import os
from dotenv import load_dotenv

load_dotenv()

client = ChatMistralAI(
    api_key=os.getenv("MISTRAL_API_KEY"),
    model="mistral-small"
)

def generate_ai_recommendation(df):

    if df.empty:
        return "No data available for generating insights."

    total_sales = df["Sales"].sum()
    avg_sales = df["Sales"].mean()
    total_customers = df["Customers"].sum()

    promo_effect = df.groupby("Promo")["Sales"].mean().to_dict()
    holiday_effect = df.groupby("Holiday")["Sales"].mean().to_dict()

    prompt = f"""
You are a business analyst.

Analyze this retail dataset summary:

Total Sales: {total_sales}
Average Sales: {avg_sales}
Total Customers: {total_customers}
Promotion Impact: {promo_effect}
Holiday Impact: {holiday_effect}

Provide:
1. Key insights
2. Business recommendations

Keep it concise and professional.
"""

    response = client.invoke(
        [HumanMessage(content=prompt)]
    )

>>>>>>> 219835bee29bc6a6c72333761d73d9695c1c441f
    return response.content