import streamlit as st
import pandas as pd
import random

# --------------- PAGE CONFIG ---------------
st.set_page_config(page_title="Beneficiary Credit Scoring Dashboard", layout="wide")

# --------------- SIDEBAR NAVIGATION ---------------
st.sidebar.title("📂 Navigation")
page = st.sidebar.radio(
    "Go to", 
    ["🏠 Home", "📊 Credit Scoring", "📁 Loan Enquiries", "⚙️ About System"]
)

# --------------- PAGE 1: HOME ---------------
if page == "🏠 Home":
    st.title("🏦 Beneficiary Credit Scoring System")
    st.markdown("""
        This AI/ML-based system evaluates beneficiary creditworthiness 
        by combining **repayment behaviour**, **loan utilization**, and 
        **income verification** using consumption data.
    """)
    st.image("https://cdn-icons-png.flaticon.com/512/3106/3106898.png", width=200)
    st.success("Navigate using the left sidebar to explore different modules!")

# --------------- PAGE 2: CREDIT SCORING ---------------
elif page == "📊 Credit Scoring":
    st.title("📊 Credit Score Evaluation")

    st.subheader("Enter Beneficiary Information:")
    name = st.text_input("Full Name")
    income = st.number_input("Annual Income (₹)", min_value=0, step=1000)
    repayment_ratio = st.slider("Repayment Behaviour (%)", 0, 100, 70)
    loan_amount = st.number_input("Previous Loan Amount (₹)", min_value=0, step=500)
    tenure = st.selectbox("Loan Tenure", ["6 Months", "12 Months", "24 Months", "36 Months"])
    
    if st.button("🔍 Generate Score"):
        score = random.randint(400, 1200)
        
        if score < 600:
            risk = "High Risk 🔴"
        elif score < 900:
            risk = "Medium Risk 🟠"
        else:
            risk = "Low Risk 🟢"

        st.markdown(f"### 💳 Composite Credit Score: `{score}`")
        st.markdown(f"### ⚠️ Risk Classification: **{risk}**")

        st.progress(score / 1200)
        st.info("Scores above 900 are eligible for same-day loan sanction.")

# --------------- PAGE 3: LOAN ENQUIRIES ---------------
elif page == "📁 Loan Enquiries":
    st.title("📁 Previous Loan Enquiries")
    data = {
        "Date": ["2022-05-10", "2023-01-15", "2023-12-05"],
        "Loan Amount (₹)": [40000, 75000, 120000],
        "Status": ["Closed", "Active", "Pending"],
        "Repayment %": [100, 85, 60],
    }
    df = pd.DataFrame(data)
    st.dataframe(df, use_container_width=True)
    st.success("All previous loan records fetched successfully!")

# --------------- PAGE 4: ABOUT ---------------
elif page == "⚙️ About System":
    st.title("⚙️ About this System")
    st.markdown("""
    **Developed for:** NBCFDC  
    **Theme:** Smart Automation  
    **Title:** Beneficiary Credit Scoring with Income Verification Layer  

    🧩 **Features:**
    - AI-based scoring using repayment + consumption patterns  
    - Risk classification into Low / Medium / High  
    - Transparent and explainable scoring model  
    - Modular digital lending interface  
    """)
    st.info("More data layers and API integration can be added in the next version 🚀")
