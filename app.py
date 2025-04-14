import pickle
import streamlit as st

# Load the trained Decision Tree model and vectorizer
with open('dt_model_sql_injection.pkl', 'rb') as model_file:
    dt_model = pickle.load(model_file)

with open('vectorizer_sql_injection.pkl', 'rb') as vectorizer_file:
    vectorizer = pickle.load(vectorizer_file)

# Streamlit app title and description
st.markdown(
    """
    <style>
    .main-title {
            text-align: center;
            font-size: 40px;
            background: linear-gradient(90deg, #ff7f50, #1e90ff);
            -webkit-background-clip: text;
            color: transparent;
            font-weight: bold;
        }
    .footer {
        position: fixed;
        bottom: 0;
        left: 0;
        width: 100%;
        background-color: #F4F6F7;
        color: #2E86C1;
        text-align: center;
        padding: 10px 0;
        font-size: 16px;
    }
    .submit-button {
        text-align: center;
    }
    </style>
    <div class="main-title">SQL Injection Detection</div>
    """,
    unsafe_allow_html=True,
)

# Input box for user to enter a SQL query or text to be tested
user_input = st.text_area(
    "Enter text or SQL query to check for SQL Injection:",
    placeholder="Type your text or SQL query here...",
    height=150,
)

# Button to check for SQL Injection
if st.button("Check for SQL Injection"):
    if user_input.strip():
        try:
            # Transform the user input using the loaded vectorizer
            transformed_input = vectorizer.transform([user_input])
            
            # Predict using the loaded Decision Tree model
            prediction = dt_model.predict(transformed_input)
            
            # Display the result with styling
            if prediction == 1:
                st.error("🚨 This input is likely to contain SQL Injection!")
            else:
                st.success("✅ This input seems safe from SQL Injection.")
        except Exception as e:
            st.error(f"Error in processing: {e}")
    else:
        st.warning("⚠️ Please enter some text or SQL query.")

# Footer
st.markdown(
    """
    <div class="footer">
        Developed by <b>Prince Kuriya</b> | © 2024
    </div>
    """,
    unsafe_allow_html=True,
)
