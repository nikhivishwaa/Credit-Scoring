import streamlit as st
import random
import pandas as pd

# ----- PAGE CONFIG -----
st.set_page_config(page_title="Beneficiary Credit Scoring", page_icon="💳", layout="centered")

# ----- TITLE & HEADER -----
st.markdown("""
<style>
body {
    background: linear-gradient(120deg, #0f2027, #203a43, #2c5364);
    color: white;
}
.block-container {
    background: rgba(255, 255, 255, 0.08);
    padding: 2rem;
    border-radius: 15px;
    box-shadow: 0 0 20px rgba(255,255,255,0.1);
}
h1, h2, h3 {
    text-align: center;
}
</style>
""", unsafe_allow_html=True)

st.title("💳 Beneficiary Credit Scoring Dashboard")
st.markdown("""
This prototype simulates the AI/ML credit scoring process for NBCFDC beneficiaries.  
Enter loan and repayment details to generate a **Composite Credit Score (400–1200)**.
""")

# ----- USER INPUTS -----
st.subheader("📋 Beneficiary Information")

col1, col2 = st.columns(2)
with col1:
    name = st.text_input("Beneficiary Name")
    age = st.number_input("Age", min_value=18, max_value=80, value=30)
    income = st.number_input("Approx Monthly Income (₹)", min_value=0, value=10000)
    business_type = st.selectbox("Business Activity Type", ["Retail", "Manufacturing", "Service", "Agriculture", "Other"])

with col2:
    loan_amount = st.number_input("Previous Loan Amount (₹)", min_value=0, value=50000)
    tenure = st.number_input("Loan Tenure (months)", min_value=1, value=12)
    repayment_status = st.selectbox("Repayment Status", ["On-Time", "Delayed", "Defaulted"])
    repeat_borrower = st.selectbox("Is Repeat Borrower?", ["Yes", "No"])

st.subheader("📊 Consumption Details (Optional)")
energy = st.slider("Average Monthly Electricity Usage (kWh)", 0, 500, 150)
mobile_recharge = st.slider("Monthly Mobile Recharge (₹)", 0, 1000, 300)
utility_bills = st.slider("Average Monthly Utility Bills (₹)", 0, 5000, 1200)

# ----- SCORE GENERATION -----
if st.button("🔍 Generate Credit Score"):
    score = random.randint(400, 1200)

    # Determine risk band
    if score >= 900:
        risk_band = "🟢 Low Risk"
        color = "green"
    elif score >= 700:
        risk_band = "🟡 Moderate Risk"
        color = "yellow"
    else:
        risk_band = "🔴 High Risk"
        color = "red"

    # Show results
    st.markdown(f"""
        <div style='text-align:center; font-size:22px;'>
            <b>Composite Credit Score:</b> <span style='color:{color}; font-size:30px;'>{score}</span><br>
            <b>Risk Band:</b> {risk_band}
        </div>
    """, unsafe_allow_html=True)

    # Display summary table
    summary = {
        "Name": [name],
        "Monthly Income (₹)": [income],
        "Loan Amount (₹)": [loan_amount],
        "Repayment Status": [repayment_status],
        "Energy Usage (kWh)": [energy],
        "Credit Score": [score],
        "Risk Band": [risk_band]
    }

    df = pd.DataFrame(summary)
    st.dataframe(df, use_container_width=True)

    st.caption("You can modify inputs and click again to simulate re-scoring.")

st.markdown("---")
st.caption("Prototype developed for SIH 2025 | PSID: 25150 | Theme: Smart Automation")
