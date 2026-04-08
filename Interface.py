import streamlit as st
import pandas as pd
from Analysis import *
from ai_utils import generate_ai_recommendation

st.set_page_config(page_title="Rossmann Sales Dashboard", layout="wide")

# -----------------------------
# Load Data
# -----------------------------
@st.cache_data
def get_data():
    df = load_data()
    df = preprocess_data(df)
    return df

df = get_data()

# -----------------------------
# SIDEBAR FILTERS (SLICERS)
# -----------------------------
st.sidebar.header("🔎 Advanced Filters")

store_type = st.sidebar.multiselect(
    "Store Type",
    df["StoreType"].unique(),
    default=df["StoreType"].unique()
)


year = st.sidebar.multiselect(
    "Year",
    df["Year"].unique(),
    default=df["Year"].unique()
)

month = st.sidebar.multiselect(
    "Month",
    df["Month"].unique(),
    default=df["Month"].unique()
)


# Promo Filter
promo = st.sidebar.selectbox(
    "Promotion",
    ["All", "Promo", "No Promo"]
)

# Holiday Filter
holiday = st.sidebar.selectbox(
    "Holiday",
    ["All", "Holiday", "Non-Holiday"]
)

# Date Range
date_range = st.sidebar.date_input(
    "Date Range",
    [df["Date"].min(), df["Date"].max()]
)

# Competition Distance
comp_min = float(df["CompetitionDistance"].min())
comp_max = float(df["CompetitionDistance"].max())

comp_dist = st.sidebar.slider(
    "Competition Distance",
    comp_min,
    comp_max,
    (comp_min, comp_max)
)

# Reset Button
if st.sidebar.button("🔄 Reset Filters"):
    st.experimental_rerun()

# -----------------------------
# APPLY FILTERS
# -----------------------------
filtered_df = df.copy()

filtered_df = filtered_df[filtered_df["StoreType"].isin(store_type)]
filtered_df = filtered_df[filtered_df["Year"].isin(year)]
filtered_df = filtered_df[filtered_df["Month"].isin(month)]

# Promo Filter
if promo == "Promo":
    filtered_df = filtered_df[filtered_df["Promo"] == 1]
elif promo == "No Promo":
    filtered_df = filtered_df[filtered_df["Promo"] == 0]

# Holiday Filter
if holiday == "Holiday":
    filtered_df = filtered_df[filtered_df["Holiday"] == 1]
elif holiday == "Non-Holiday":
    filtered_df = filtered_df[filtered_df["Holiday"] == 0]

# Date Filter
filtered_df = filtered_df[
    (filtered_df["Date"] >= pd.to_datetime(date_range[0])) &
    (filtered_df["Date"] <= pd.to_datetime(date_range[1]))
]


# -----------------------------
# TITLE
# -----------------------------
st.title("📊 Rossmann Retail Sales Dashboard")

# TABS (STORYTELLING)
# -----------------------------
tab1, tab2, tab3 = st.tabs(["📊 Executive Summary", "🔍 Key Insights", "🎯 Recommendations"])

# TAB 1: EXECUTIVE SUMMARY
# -----------------------------
with tab1:
    st.header("📊 Executive Summary")

    if filtered_df.empty:
        st.warning("No data available for selected filters.")
    else:
        col1, col2, col3, col4 = st.columns(4)

        col1.metric("💰 Total Sales", f"{filtered_df['Sales'].sum():,.0f}")
        col2.metric("👥 Customers", f"{filtered_df['Customers'].sum():,.0f}")
        col3.metric("📈 Avg Daily Sales", f"{filtered_df.groupby('Date')['Sales'].sum().mean():,.0f}")
        col4.metric("💵 Revenue/Customer", f"{(filtered_df['Sales'].sum()/filtered_df['Customers'].sum()):.2f}")

        st.markdown("### 📌 Overview")
        st.write("This dashboard analyzes retail performance based on sales, customer behavior, promotions, and competition.")

        # -----------------------------
        # SALES INSIGHTS
        # -----------------------------
        st.subheader("📈 Sales Insights")

        col1, col2 = st.columns(2)

        with col1:
            st.pyplot(sales_trend(filtered_df))

        with col2:
            st.pyplot(sales_by_store(filtered_df))

        # -----------------------------
        # OPERATIONS ANALYSIS
        # -----------------------------
        col1, col2 = st.columns(2)

        with col1:
            st.pyplot(sales_by_day(filtered_df))

        with col2:
            st.pyplot(promo_impact(filtered_df))

        # -----------------------------
        # CUSTOMER ANALYSIS
        # -----------------------------
        st.subheader("👥 Customer & Store Analysis")

        col1, col2 = st.columns(2)

        with col1:
            st.pyplot(sales_vs_customers(filtered_df))

        with col2:
            st.pyplot(customers_by_storetype(filtered_df))

        # -----------------------------
        # PERFORMANCE ANALYSIS
        # -----------------------------
        col1, col2 = st.columns(2)

        with col1:
            st.pyplot(store_performance_distribution(filtered_df))

        with col2:
            st.pyplot(revenue_per_customer(filtered_df))

        # -----------------------------
        # COMPETITION & HOLIDAY
        # -----------------------------
        st.subheader("🧭 Competition & Holiday Impact")

        col1, col2 = st.columns(2)

        with col1:
            st.pyplot(competition_bins(filtered_df))

        with col2:
            st.pyplot(sales_by_holiday(filtered_df))

        # -----------------------------
        # TOP & BOTTOM STORES
        # -----------------------------
        st.subheader("🏆 Top & Bottom Stores")

        col1, col2 = st.columns(2)

        with col1:
            st.write("### Top 10 Stores")
            top_stores = filtered_df.groupby("Store")["Sales"].sum().sort_values(ascending=False).head(10)
            st.dataframe(top_stores)

        with col2:
            st.write("### Bottom 10 Stores")
            bottom_stores = filtered_df.groupby("Store")["Sales"].sum().sort_values().head(10)
            st.dataframe(bottom_stores)

        # -----------------------------
        # DOWNLOAD DATA
        # -----------------------------
        st.subheader("📥 Download Data")

        csv = filtered_df.to_csv(index=False).encode("utf-8")

        st.download_button(
            label="Download Filtered Data",
            data=csv,
            file_name="filtered_data.csv",
            mime="text/csv"
        )

# -----------------------------
# TAB 2: KEY INSIGHTS
# -----------------------------
with tab2:
    st.header("🔍 Key Business Insights")
    
    if filtered_df.empty:
        st.warning("⚠️ No data available for selected filters.")
    else:
        # -----------------------------
        # 1. Top Store Type
        # -----------------------------
        top_store_type = filtered_df.groupby("StoreType")["Sales"].sum().idxmax()
        top_store_sales = filtered_df.groupby("StoreType")["Sales"].sum().max()

        st.write(f"🏪 **Top Performing Store Type:** {top_store_type} with total sales of {top_store_sales:,.0f}")

        # -----------------------------
        # 2. Best Day for Sales
        # -----------------------------
        filtered_df["DayName"] = filtered_df["Date"].dt.day_name()
        best_day = filtered_df.groupby("DayName")["Sales"].mean().idxmax()

        st.write(f"📅 **Best Sales Day:** {best_day} shows highest average sales.")

        # -----------------------------
        # 3. Promotion Impact
        # -----------------------------
        promo_sales = filtered_df.groupby("Promo")["Sales"].mean()

        if len(promo_sales) > 1:
            increase = ((promo_sales[1] - promo_sales[0]) / promo_sales[0]) * 100
            st.write(f"🎯 **Promotion Impact:** Sales increase by {increase:.2f}% during promotions.")

        # -----------------------------
        # 4. Holiday Impact
        # -----------------------------
        holiday_sales = filtered_df.groupby("Holiday")["Sales"].mean()

        if len(holiday_sales) > 1:
            diff = holiday_sales[1] - holiday_sales[0]
            st.write(f"🎄 **Holiday Effect:** Sales change by {diff:,.0f} on holidays compared to non-holidays.")

        # -----------------------------
        # 5. Revenue Efficiency
        # -----------------------------
        filtered_df["RevenuePerCustomer"] = filtered_df["Sales"] / filtered_df["Customers"]
        best_rpc_store = filtered_df.groupby("StoreType")["RevenuePerCustomer"].mean().idxmax()

        st.write(f"💰 **Best Revenue Efficiency:** Store Type {best_rpc_store} generates highest revenue per customer.")

        # -----------------------------
        # 6. Competition Insight
        # -----------------------------
        if "CompetitionDistance" in filtered_df.columns:
            corr = filtered_df[["Sales", "CompetitionDistance"]].corr().iloc[0,1]

            if corr < 0:
                st.write("📉 **Competition Insight:** Closer competitors negatively impact sales.")
            else:
                st.write("📈 **Competition Insight:** Competition distance has limited or positive impact on sales.")

        # -----------------------------
        # 7. Top Store
        # -----------------------------
        top_store = filtered_df.groupby("Store")["Sales"].sum().idxmax()
        st.write(f"🏆 **Top Store:** Store {top_store} generates the highest revenue.")

        # -----------------------------
        # 8. Worst Store
        # -----------------------------
        worst_store = filtered_df.groupby("Store")["Sales"].sum().idxmin()
        st.write(f"⚠️ **Underperforming Store:** Store {worst_store} has the lowest sales.")

# TAB 3: RECOMMENDATIONS
# -----------------------------
with tab3:
    st.header("🎯 AI-Powered Recommendations")

    if filtered_df.empty:
        st.warning("No data available.")
    else:
        if st.button("Generate AI Insights"):
            with st.spinner("Analyzing data..."):
                result = generate_ai_recommendation(filtered_df)

            st.success("✅ AI Insights Generated")
            st.write(result)