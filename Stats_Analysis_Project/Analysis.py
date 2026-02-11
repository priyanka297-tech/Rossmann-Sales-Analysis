import pandas as pd
import matplotlib.pyplot as plt


def load_data():
    store = pd.read_csv("store.csv")
    train = pd.read_csv("train.csv")
    # print(train.head())

    df = pd.merge(store,train, on = "Store") 
    return df
    
# Data Preprocessing 
def preprocess_data(df):
    # sales according to year and month
    df["Date"]= pd.to_datetime(df["Date"])
    df["Year"] = df["Date"].dt.year
    df["Month"] = df["Date"].dt.month_name()
    
    # Holiday Feature
    #difference on sales of during holiday and non holiday
    df["StateHoliday"] = df["StateHoliday"].replace({"0": 0, "a": 1, "b": 1, "c": 1}).astype(int)
    df["SchoolHoliday"] = df["SchoolHoliday"].astype(int)
    df["Holiday"] = df["SchoolHoliday"] + df["StateHoliday"]
    df["Holiday"] = df["Holiday"].apply(lambda i:1 if i > 0 else 0)
    return df
    
# Visualization of data
# sales according storetype(height sales of which store as well as lowest sales of which store type)
def sales_by_store(df):
    sales_by_store_type = df.groupby("StoreType")["Sales"].sum()
    fig, ax = plt.subplots()
    ax.bar(sales_by_store_type.index, sales_by_store_type.values)
    ax.set_xlabel("Store Type")
    ax.set_ylabel("Sales Amount")
    ax.set_title("Sales by StoreType")
    return fig


def sales_by_year(df):
    sales_by_year = df.groupby("Year")["Sales"].sum()
    fig, ax = plt.subplots()
    ax.bar(sales_by_year.index, sales_by_year.values)
    ax.set_xlabel("Year")
    ax.set_ylabel("Sales Amount")
    ax.set_title("Sales by Year")
    return fig

def sales_by_month(df):
    sales_by_month = df.groupby("Month")["Sales"].sum()
    fig, ax = plt.subplots()
    ax.bar(sales_by_month.index, sales_by_month.values)
    ax.set(rotation=90)
    ax.set_xlabel("Month")
    ax.set_ylabel("Sales Amount")
    ax.set_title("Sales by Month")
    return fig

# sales behalf of competition distace
def sales_by_competition_distance(df):
    sales_by_competition_dis = df.groupby("CompetitionDistance")["Sales"].sum()
    fig, ax = plt.subplots()
    ax.bar(sales_by_competition_dis.index, sales_by_competition_dis.values)
    ax.set_xlabel("Distance")
    ax.set_ylabel("Sales Amount")
    ax.set_title("Sales by Competition Distance")
    return fig

def sales_by_holiday(df):
    sales_by_holiday = df.groupby("Holiday")["Sales"].sum()
    fig, ax = plt.subplots()
    ax.bar(sales_by_holiday.index, sales_by_holiday.values)
    # ax.set_xticks([0,1])
    ax.set_xticklabels(["Non-Holiday", "Holiday"])
    ax.set_xlabel("Holiday")
    ax.set_ylabel("Sales Amount")
    ax.set_title("Sales by Holiday")
    return fig

# Which storeType have more customers and which month have more customers

# how much competitors actively participating at which location
