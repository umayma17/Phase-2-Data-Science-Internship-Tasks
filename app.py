import pandas as pd
import streamlit as st

# -------------------------
# PAGE TITLE
# -------------------------
st.title("📊 Superstore Sales Dashboard")

# -------------------------
# LOAD DATA
# -------------------------
df = pd.read_csv("superstore.csv")

# Clean column names (IMPORTANT FIX)
df.columns = df.columns.str.strip()

# -------------------------
# SHOW DATA
# -------------------------
st.subheader("Dataset Preview")
st.dataframe(df.head())

# -------------------------
# CHECK COLUMNS
# -------------------------
st.write("Columns in file:", df.columns)

# -------------------------
# SIDEBAR FILTER (optional but useful)
# -------------------------
if "Region" in df.columns:
    region = st.sidebar.selectbox("Select Region", df["Region"].unique())
    df = df[df["Region"] == region]

# -------------------------
# TOP CUSTOMERS
# -------------------------
if "Customer Name" in df.columns and "Sales" in df.columns:
    st.subheader("Top Customers")

    top_customers = df.groupby("Customer Name")["Sales"].sum() \
        .sort_values(ascending=False).head(10)

    st.dataframe(top_customers)

# -------------------------
# TOP PRODUCTS
# -------------------------
if "Product Name" in df.columns and "Sales" in df.columns:
    st.subheader("Top Products")

    top_products = df.groupby("Product Name")["Sales"].sum() \
        .sort_values(ascending=False).head(10)

    st.dataframe(top_products)

# -------------------------
# CATEGORY WISE SALES
# -------------------------
if "Category" in df.columns and "Sales" in df.columns:
    st.subheader("Category Wise Sales")

    category_sales = df.groupby("Category")["Sales"].sum()

    st.bar_chart(category_sales)

# -------------------------
# REGION WISE SALES
# -------------------------
if "Region" in df.columns and "Sales" in df.columns:
    st.subheader("Region Wise Sales")

    region_sales = df.groupby("Region")["Sales"].sum()

    st.bar_chart(region_sales)