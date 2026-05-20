import streamlit as st
import math

# Page Config
st.set_page_config(
    page_title="Scientific Calculator",
    page_icon="🧮",
    layout="centered"
)

# Dark Mode Styling
st.markdown("""
    <style>
    .stApp {
        background-color: #0E1117;
        color: white;
    }

    h1, h2, h3, p, label {
        color: white;
    }

    .stButton>button {
        background-color: #262730;
        color: white;
        border-radius: 10px;
        height: 3em;
        width: 100%;
    }

    .stTextInput>div>div>input {
        background-color: #262730;
        color: white;
    }
    </style>
""", unsafe_allow_html=True)

st.title("🧮 Scientific Calculator")

# History Storage
if "history" not in st.session_state:
    st.session_state.history = []

# Inputs
num1 = st.number_input("Enter First Number", value=0.0)
num2 = st.number_input("Enter Second Number", value=0.0)

# Operations
operation = st.selectbox(
    "Choose Operation",
    [
        "Addition",
        "Subtraction",
        "Multiplication",
        "Division",
        "Power",
        "Square Root",
        "Sin",
        "Cos",
        "Tan",
        "Log"
    ]
)

# Calculation
if st.button("Calculate"):

    try:

        if operation == "Addition":
            result = num1 + num2
            expression = f"{num1} + {num2}"

        elif operation == "Subtraction":
            result = num1 - num2
            expression = f"{num1} - {num2}"

        elif operation == "Multiplication":
            result = num1 * num2
            expression = f"{num1} × {num2}"

        elif operation == "Division":
            result = num1 / num2
            expression = f"{num1} ÷ {num2}"

        elif operation == "Power":
            result = num1 ** num2
            expression = f"{num1}^{num2}"

        elif operation == "Square Root":
            result = math.sqrt(num1)
            expression = f"√{num1}"

        elif operation == "Sin":
            result = math.sin(math.radians(num1))
            expression = f"sin({num1})"

        elif operation == "Cos":
            result = math.cos(math.radians(num1))
            expression = f"cos({num1})"

        elif operation == "Tan":
            result = math.tan(math.radians(num1))
            expression = f"tan({num1})"

        elif operation == "Log":
            result = math.log10(num1)
            expression = f"log({num1})"

        st.success(f"Result: {result}")

        # Save History
        st.session_state.history.append(
            f"{expression} = {result}"
        )

    except Exception as e:
        st.error(f"Error: {e}")

# History Section
st.subheader("🕘 Calculation History")

if st.session_state.history:
    for item in reversed(st.session_state.history):
        st.write(item)
else:
    st.write("No calculations yet.")

# Clear History
if st.button("Clear History"):
    st.session_state.history = []
    st.success("History Cleared")

