import streamlit as st
import pandas as pd
from pathlib import Path
st.set_page_config(page_title="India Retail Analytics",layout="wide")
BASE=Path(__file__).resolve().parents[1]
df=pd.read_csv(BASE/"data/orders.csv",parse_dates=["Order_Date"])
st.title("🇮🇳 India Retail & E-Commerce Analytics")
st.caption("Interactive portfolio dashboard | Excel + Power BI + SQL + Python")
with st.sidebar:
    st.header("Filters")
    states=st.multiselect("State",sorted(df.State.unique()),default=sorted(df.State.unique()))
    cats=st.multiselect("Category",sorted(df.Category.unique()),default=sorted(df.Category.unique()))
    channels=st.multiselect("Channel",sorted(df.Channel.unique()),default=sorted(df.Channel.unique()))
f=df[df.State.isin(states)&df.Category.isin(cats)&df.Channel.isin(channels)]
sales=f.Sales.sum(); profit=f.Profit.sum(); orders=f.Order_ID.nunique(); aov=sales/orders if orders else 0
c1,c2,c3,c4,c5=st.columns(5)
c1.metric("Sales",f"₹{sales:,.0f}"); c2.metric("Profit",f"₹{profit:,.0f}"); c3.metric("Orders",f"{orders:,}")
c4.metric("AOV",f"₹{aov:,.0f}"); c5.metric("On-Time",f"{(f.Delivery_Status=='On Time').mean():.1%}")
st.subheader("Monthly Sales"); st.line_chart(f.assign(Month=f.Order_Date.dt.to_period("M").astype(str)).groupby("Month").Sales.sum())
l,r=st.columns(2)
with l: st.subheader("Sales by Category"); st.bar_chart(f.groupby("Category").Sales.sum().sort_values(ascending=False))
with r: st.subheader("Profit by State"); st.bar_chart(f.groupby("State").Profit.sum().sort_values(ascending=False))
st.subheader("Operations & Customer Experience")
st.dataframe(f.groupby("Delivery_Status").agg(Orders=("Order_ID","count"),Avg_Rating=("Customer_Rating","mean"),Return_Rate=("Returned","mean"),Profit=("Profit","sum")).reset_index(),use_container_width=True)
st.info("Synthetic dataset. Replace data/orders.csv with updated data and rerun to refresh.")
