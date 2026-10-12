import streamlit as st
import joblib

# Page configuration
st.set_page_config(
    page_title="SME Credit Risk Intelligence",
    page_icon="💼",
    layout="centered",
    initial_sidebar_state="expanded"
)

# Custom CSS for Clean & Premium Look (Fixed Theme Contrast)
st.markdown("""
    <style>
    .stButton>button {
        width: 100%;
        background: linear-gradient(135deg, #3b82f6 0%, #1d4ed8 100%);
        color: white;
        font-weight: 600;
        padding: 0.75rem;
        border-radius: 8px;
        border: none;
        box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1);
        transition: all 0.3s ease;
    }
    .stButton>button:hover {
        background: linear-gradient(135deg, #2563eb 0%, #1e40af 100%);
        box-shadow: 0 10px 15px -3px rgba(59, 130, 246, 0.3);
    }
    </style>
""", unsafe_allow_html=True)


# Load Model safely
@st.cache_resource
def load_model():
    return joblib.load('model.pkl')


model = load_model()

# Header Section
st.title("🛡️ SME Credit Risk & Intelligence Portal")
st.markdown("---")
st.markdown(
    "Advanced machine learning system designed to evaluate business creditworthiness and financial distress risk instantly.")

# Sidebar for Navigation / Info
with st.sidebar:
    st.header("📊 System Metrics")
    st.info("Model: Random Forest Classifier\nStatus: Online & Active\nAccuracy: Optimized")
    st.markdown("---")
    st.markdown("### Instructions")
    st.write("Enter the required business parameters carefully to get an accurate credit risk assessment.")

# Main Form Container
with st.container():
    st.subheader("📝 Enter Business Parameters")

    col1, col2 = st.columns(2)

    with col1:
        age = st.number_input("SME Age (Years)", min_value=0.0, value=5.0, step=1.0,
                              help="Total operating years of the business.")
        revenue_cat = st.number_input("Annual Revenue Category", min_value=0.0, value=2.0, step=1.0,
                                      help="Categorical scale of yearly revenue.")

    with col2:
        liquidity = st.number_input("Liquidity Stability", min_value=0.0, value=5.0, step=1.0,
                                    help="Score measuring cash flow stability.")
        risk = st.number_input("Risk Awareness", min_value=0.0, value=5.0, step=1.0,
                               help="Management risk awareness index.")

    st.markdown("<br>", unsafe_allow_html=True)

    # Prediction Trigger
    if st.button("Evaluate Credit Risk"):
        with st.spinner("Analyzing financial health and transaction patterns..."):
            # Prediction
            prediction = model.predict([[age, revenue_cat, liquidity, risk]])

            st.markdown("---")
            st.subheader("🎯 Assessment Result")

            if prediction[0] == 0:
                st.success("### Low Risk: Loan Approved ✅")
                st.write(
                    "The business displays stable financial indicators and healthy liquidity parameters. Recommended for credit disbursement.")
            else:
                st.error("### High Risk: Loan Rejected ❌")
                st.write(
                    "The evaluated parameters indicate elevated vulnerability to financial distress. Additional collateral or manual audit is recommended.")