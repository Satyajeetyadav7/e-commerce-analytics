# Rerunnable synthetic data generator
import numpy as np, pandas as pd
from pathlib import Path
SEED=42; N=50000; rng=np.random.default_rng(SEED)
out=Path(__file__).resolve().parents[1]/"data"; out.mkdir(exist_ok=True)
dates=pd.date_range("2025-01-01","2026-10-31",freq="D")
cats=["Electronics","Home & Kitchen","Fashion","Beauty & Personal Care","Grocery","Sports & Fitness"]
states=["Punjab","Delhi","Haryana","Maharashtra","Karnataka","Tamil Nadu","Telangana","Uttar Pradesh","Gujarat","West Bengal","Rajasthan","Kerala"]
df=pd.DataFrame({"Order_ID":np.arange(1000001,1000001+N),"Order_Date":rng.choice(dates,N),
"Customer_ID":rng.integers(10001,17001,N),"State":rng.choice(states,N),
"Category":rng.choice(cats,N),"Channel":rng.choice(["Website","Mobile App","Marketplace"],N,p=[.34,.48,.18]),
"Quantity":rng.choice([1,2,3,4],N,p=[.63,.25,.09,.03])})
df["Sales"]=np.round(rng.uniform(250,12000,N)*df["Quantity"],2)
df["Discount_Pct"]=np.round(rng.uniform(0,.45,N),4)
df["Profit"]=np.round(df["Sales"]*(rng.uniform(.08,.30,N)-df["Discount_Pct"]*.35),2)
df["Promised_Days"]=rng.integers(2,7,N); df["Delivery_Days"]=np.maximum(1,df["Promised_Days"]+rng.integers(-1,3,N))
df["Delivery_Status"]=np.where(df["Delivery_Days"]<=df["Promised_Days"],"On Time","Late")
df["Customer_Rating"]=np.round(np.clip(rng.normal(4.2,.5,N)-.4*(df["Delivery_Status"]=="Late"),1,5),1)
df["Returned"]=(rng.random(N)<.08).astype(int)
df.to_csv(out/"orders.csv",index=False)
print(f"Generated {len(df):,} orders.")
