import re
import streamlit as st

st.set_page_config(
    page_title="Password Strength Checker By Muniba Fatima", 
    page_icon="👁️‍🗨️", 
    layout="centered"
)

# Custom CSS
st.markdown("""
<style>
    .main {text-align: center;}
    .stTextInput {width: 60% !important; margin: auto;} 
    .stButton button {width: 50%; background-color: blue; color: white; font-size: 18px;} 
    .stButton button:hover {background-color: red; color: white;}
</style>
""", unsafe_allow_html=True)

# Page title and description
st.title("🔐 Password Strength Checker")
st.write("Enter your password below to check its security level. 🏓")

# Function to check password strength
def check_password_strength(password):
    score = 0
    feedback = []

    # Check password length
    if len(password) >= 8:
        score += 1
    else:
        feedback.append("❌ Password should be **at least 8 characters long**.")

    # Check uppercase & lowercase
    if re.search(r"[A-Z]", password) and re.search(r"[a-z]", password):
        score += 1
    else:
        feedback.append("❌ Password should include **both uppercase (A-Z) and lowercase (a-z) letters**.")

    # Check for numbers
    if re.search(r"\d", password):
        score += 1
    else:
        feedback.append("❌ Password should include **at least one number (0-9)**.") 

    # Check for special characters
    if re.search(r"[!@#$%^&*]", password):
        score += 1
    else:
        feedback.append("❌ Include **at least one special character (!@#$%^&*)**.") 

    # Display password results
    if score == 4:
        st.success("✅ **Strong Password** - Your password is secure.")
    elif score == 3:
        st.info("⚠️ **Moderate Password** - Consider improving security by adding more complexity.")
    elif score == 2:
        st.warning("⚠️ **Weak Password** - Follow the suggestions below to strengthen it.")
    else:
        st.error("❌ **Very Weak Password** - It is highly recommended to improve your password.")

    # Feedback section
    if feedback:
        with st.expander("🏓 Improve Your Password"):
            for item in feedback:
                st.write(item)

# Input field for password
password = st.text_input("Enter your password:", type="password", help="Ensure your password is strong 🔐")

# Button to check strength
if st.button("Check Strength"):
    if password:
        check_password_strength(password)
    else:
        st.warning("⚠️ Please enter a password first!")  # Show warning if password is empty
