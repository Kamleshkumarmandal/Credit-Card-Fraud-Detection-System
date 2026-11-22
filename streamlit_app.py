
import streamlit as st
import pandas as pd

st.set_page_config(page_title="Credit Card Fraud Detection", page_icon="💳", layout="wide")

st.title("💳 Credit Card Fraud Detection System")
st.caption("Transaction Monitoring Dashboard")

data = pd.DataFrame([
    ["TXN1001", "CARD001", 250, "Safe"],
    ["TXN1002", "CARD002", 8500, "Fraud"],
    ["TXN1003", "CARD003", 1200, "Safe"],
    ["TXN1004", "CARD004", 12000, "Fraud"],
    ["TXN1005", "CARD005", 450, "Safe"],
    ["TXN1006", "CARD006", 700, "Safe"]
], columns=["Transaction ID", "Card ID", "Amount", "Status"])

st.subheader("Dashboard Overview")

a, b, c = st.columns(3)
a.metric("Total Transactions", len(data))
b.metric("Fraud Detected", (data.Status == "Fraud").sum())
c.metric("Safe Transactions", (data.Status == "Safe").sum())

st.divider()

left, right = st.columns(2)

with left:
    st.subheader("Transaction Status")
    st.bar_chart(data.Status.value_counts())

with right:
    st.subheader("Transaction Amount")
    st.bar_chart(data.set_index("Transaction ID")["Amount"])

st.subheader("Transaction Records")
st.dataframe(data, use_container_width=True, hide_index=True)

st.divider()
st.subheader("Test a Transaction")

amount = st.number_input("Enter transaction amount", min_value=1, value=500)
card = st.text_input("Enter Card ID", "CARD007")

if st.button("Check Transaction"):
    if amount >= 5000:
        st.error("⚠️ Suspicious transaction detected!")
    else:
        st.success("✅ Transaction appears safe!")

st.caption("Academic demo using sample data. Not connected to the live Kafka, Spark or HBase pipeline.")
