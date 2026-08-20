<<<<<<< HEAD
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

# sales trends on time
def sales_trend(df):
    sales_trend = df.groupby(["Year", "Date"])["Sales"].sum().reset_index()
    
    fig, ax = plt.subplots()
    
    for year in sales_trend["Year"].unique():
        yearly_data = sales_trend[sales_trend["Year"] == year]
        ax.plot(yearly_data["Date"], yearly_data["Sales"], label=str(year))
    
    ax.set_xlabel("Date")
    ax.set_ylabel("Sales")
    ax.set_title("Daily Sales Trend by Year")
    ax.legend()
    
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

# sales VS customers
def sales_vs_customers(df):
    grouped = df.groupby("Date")[["Sales", "Customers"]].sum()
    fig, ax = plt.subplots()
    ax.scatter(grouped["Customers"], grouped["Sales"])
    ax.set_xlabel("Customers")
    ax.set_ylabel("Sales")
    ax.set_title("Sales vs Customers")
    return fig

# Store Performance Distribution
def store_performance_distribution(df):
    store_sales = df.groupby("Store")["Sales"].sum()
    fig, ax = plt.subplots()
    ax.hist(store_sales, bins=30)
    ax.set_xlabel("Total Sales per Store")
    ax.set_ylabel("Frequency")
    ax.set_title("Store Performance Distribution")
    return fig

# promotion impacts on sales 
def promo_impact(df):
    promo_sales = df.groupby("Promo")["Sales"].mean()
    fig, ax = plt.subplots()
    ax.bar(promo_sales.index, promo_sales.values)
    ax.set_xticklabels(["No Promo", "Promo"])
    ax.set_xlabel("Promotion")
    ax.set_ylabel("Average Sales")
    ax.set_title("Impact of Promotion on Sales")
    return fig

# Days of week sales
def sales_by_day(df):
    df["DayName"] = df["Date"].dt.day_name()
    sales_day = df.groupby("DayName")["Sales"].mean()
    fig, ax = plt.subplots()
    ax.bar(sales_day.index, sales_day.values)
    ax.set_xticklabels(sales_day.index, rotation=45)
    ax.set_xlabel("Day")
    ax.set_ylabel("Average Sales")
    ax.set_title("Sales by Day of Week")
    return fig

# storetype vs customers
def customers_by_storetype(df):
    customers = df.groupby("StoreType")["Customers"].mean()
    fig, ax = plt.subplots()
    ax.bar(customers.index, customers.values)
    ax.set_xlabel("Store Type")
    ax.set_ylabel("Avg Customers")
    ax.set_title("Customers by Store Type")
    return fig

# revenue per customer
def revenue_per_customer(df):
    df["RevenuePerCustomer"] = df["Sales"] / df["Customers"]
    rpc = df.groupby("StoreType")["RevenuePerCustomer"].mean()
    
    fig, ax = plt.subplots()
    ax.bar(rpc.index, rpc.values)
    ax.set_xlabel("Store Type")
    ax.set_ylabel("Revenue per Customer")
    ax.set_title("Revenue per Customer by Store Type")
    return fig

# competition distance impact 
def competition_bins(df):
    df["CompetitionDistance"] = df["CompetitionDistance"].fillna(df["CompetitionDistance"].median())
    
    df["CompBin"] = pd.cut(df["CompetitionDistance"], bins=5)
    comp_sales = df.groupby("CompBin")["Sales"].mean()
    
    fig, ax = plt.subplots()
    ax.bar(range(len(comp_sales)), comp_sales.values)
    ax.set_xticks(range(len(comp_sales)))
    ax.set_xticklabels(comp_sales.index, rotation=45)
    ax.set_xlabel("Competition Distance Range")
    ax.set_ylabel("Avg Sales")
    ax.set_title("Competition Distance Impact")
    return fig

# Which storeType have more customers and which month have more customers

# how much competitors actively participating at which location
=======
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

# sales trends on time
def sales_trend(df):
    sales_trend = df.groupby(["Year", "Date"])["Sales"].sum().reset_index()
    
    fig, ax = plt.subplots()
    
    for year in sales_trend["Year"].unique():
        yearly_data = sales_trend[sales_trend["Year"] == year]
        ax.plot(yearly_data["Date"], yearly_data["Sales"], label=str(year))
    
    ax.set_xlabel("Date")
    ax.set_ylabel("Sales")
    ax.set_title("Daily Sales Trend by Year")
    ax.legend()
    
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

# sales VS customers
def sales_vs_customers(df):
    grouped = df.groupby("Date")[["Sales", "Customers"]].sum()
    fig, ax = plt.subplots()
    ax.scatter(grouped["Customers"], grouped["Sales"])
    ax.set_xlabel("Customers")
    ax.set_ylabel("Sales")
    ax.set_title("Sales vs Customers")
    return fig

# Store Performance Distribution
def store_performance_distribution(df):
    store_sales = df.groupby("Store")["Sales"].sum()
    fig, ax = plt.subplots()
    ax.hist(store_sales, bins=30)
    ax.set_xlabel("Total Sales per Store")
    ax.set_ylabel("Frequency")
    ax.set_title("Store Performance Distribution")
    return fig

# promotion impacts on sales 
def promo_impact(df):
    promo_sales = df.groupby("Promo")["Sales"].mean()
    fig, ax = plt.subplots()
    ax.bar(promo_sales.index, promo_sales.values)
    ax.set_xticklabels(["No Promo", "Promo"])
    ax.set_xlabel("Promotion")
    ax.set_ylabel("Average Sales")
    ax.set_title("Impact of Promotion on Sales")
    return fig

# Days of week sales
def sales_by_day(df):
    df["DayName"] = df["Date"].dt.day_name()
    sales_day = df.groupby("DayName")["Sales"].mean()
    fig, ax = plt.subplots()
    ax.bar(sales_day.index, sales_day.values)
    ax.set_xticklabels(sales_day.index, rotation=45)
    ax.set_xlabel("Day")
    ax.set_ylabel("Average Sales")
    ax.set_title("Sales by Day of Week")
    return fig

# storetype vs customers
def customers_by_storetype(df):
    customers = df.groupby("StoreType")["Customers"].mean()
    fig, ax = plt.subplots()
    ax.bar(customers.index, customers.values)
    ax.set_xlabel("Store Type")
    ax.set_ylabel("Avg Customers")
    ax.set_title("Customers by Store Type")
    return fig

# revenue per customer
def revenue_per_customer(df):
    df["RevenuePerCustomer"] = df["Sales"] / df["Customers"]
    rpc = df.groupby("StoreType")["RevenuePerCustomer"].mean()
    
    fig, ax = plt.subplots()
    ax.bar(rpc.index, rpc.values)
    ax.set_xlabel("Store Type")
    ax.set_ylabel("Revenue per Customer")
    ax.set_title("Revenue per Customer by Store Type")
    return fig

# competition distance impact 
def competition_bins(df):
    df["CompetitionDistance"] = df["CompetitionDistance"].fillna(df["CompetitionDistance"].median())
    
    df["CompBin"] = pd.cut(df["CompetitionDistance"], bins=5)
    comp_sales = df.groupby("CompBin")["Sales"].mean()
    
    fig, ax = plt.subplots()
    ax.bar(range(len(comp_sales)), comp_sales.values)
    ax.set_xticks(range(len(comp_sales)))
    ax.set_xticklabels(comp_sales.index, rotation=45)
    ax.set_xlabel("Competition Distance Range")
    ax.set_ylabel("Avg Sales")
    ax.set_title("Competition Distance Impact")
    return fig

# Which storeType have more customers and which month have more customers

# how much competitors actively participating at which location
>>>>>>> 219835bee29bc6a6c72333761d73d9695c1c441f
