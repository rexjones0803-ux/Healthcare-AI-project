import streamlit as st
import json

st.title("Health Insurance Question & Answer Tool")
st.write("Ask basic questions about your UnitedHealthcare insurance plan.")

with open("insurance_data.json", "r") as file:
    insurance_data = json.load(file)

text = insurance_data["pdf_text"]

question = st.text_input("Ask a question about your insurance plan:")

if question:
    words = question.lower().replace("?", "").split()

    words = [
        word for word in words
        if word not in ["what", "is", "my", "does", "insurance",
                        "cover", "the", "a", "an", "how", "much"]
    ]

    if "emergency" in question.lower():
        words = ["emergency room"]

    matches = [
        line for line in text.splitlines()
        if all(word in line.lower() for word in words if len(word) > 3)
    ]

    if matches:
        answer = next((line for line in matches if "$" in line), matches[0])
        st.write("ANSWER:", answer)
    else:
        st.write("Sorry, I couldn't find an answer.")