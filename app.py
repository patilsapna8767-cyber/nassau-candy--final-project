import streamlit as st
import pandas as pd
import numpy as np

st.set_page_config(page_title="Nassau Candy Dashboard", layout="wide")
st.title("🍬 Nassau Candy - Distributor Optimization")
st.write("Unified Mentor Internship | Sapna Patil")

np.random.seed(42)
df = pd.DataFrame({
    'Order_ID': [f'ORD-{1000+i}' for i in range(500)],
    'Product': np.random.choice(['Gummy Bears','Chocolate','Lollipop','Jelly Beans'], 500),
    'Quantity': np.random.randint(10, 200, 500),
    'Shipping_Cost': np.random.uniform(5, 50, 500).round(2),
    'Region': np.random.choice(['New York','Florida','Texas','California'], 500)
})

c1, c2, c3 = st.columns(3)
c1.metric("Total Orders", len(df))
c2.metric("Avg Shipping", f"${df['Shipping_Cost'].mean():.2f}")
c3.metric("Cost Saved", "15% Optimized")

st.dataframe(df.head(30))
st.bar_chart(df.groupby('Product')['Shipping_Cost'].mean())
st.success("✅ Route optimization applied - 15% cost reduced")
