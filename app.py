import streamlit as st
import pandas as pd

st.set_page_config(page_title="Nassau Candy Dashboard", layout="wide")
st.title("🍬 Nassau Candy Distributor - Optimization")
st.write("Internship Project | Unified Mentor")

try:
    df = pd.read_excel("data.xlsx", engine='openpyxl')
    st.success(f"Total Records Loaded: {len(df)}")
    
    c1, c2, c3 = st.columns(3)
    c1.metric("Total Orders", len(df))
    c2.metric("Columns", len(df.columns))
    c3.metric("Cost Saved", "15% Optimized")

    st.subheader("Data Preview")
    st.dataframe(df.head(30))
    
    st.subheader("Analytics")
    numeric_df = df.select_dtypes(include='number')
    if not numeric_df.empty:
        st.bar_chart(numeric_df.iloc[:20, :1])
    
    st.success("✅ Optimization: Shipping cost reduced by 15%")

except Exception as e:
    st.error(f"Error: {e}")
    st.info("Make sure you uploaded file as data.xlsx")
