import streamlit as st
from CODbot import CODSOFTBot

# Instantiate the CODSOFTBot
bot = CODSOFTBot()

# Define Streamlit app header
st.title("CODSOFT Chatbot")

# Greet the user and start chat
st.sidebar.subheader("Welcome to CODSOFT Chatbot")
name = st.text_input("Hello! Welcome to CODSOFT. May I have your name?")
if name:
    st.write(f"Hello {name}!")

    # Interaction loop
    will_help = input(f"Hi {name}, do you want to continue?\n")
    if will_help in bot.negative_responses:
        st.write("Have a great day!")
    else:
        bot.chat()

        # Chat loop
        while True:
            message = st.text_input("You:").strip().lower()
            if bot.make_exit(message):
                st.write("CODSOFT: Thank you for visiting CODSOFT. Have a wonderful day!")
                break
            reply = bot.match_rep(message)
            st.write(f"CODSOFT: {reply}")

# Footer
st.sidebar.text("© 2024 CODSOFT. All rights reserved.")

