import streamlit as st
from transformers import pipeline

# Create a text generation pipeline with your chosen model
generator = pipeline("text-generation", model="meta-llama/Llama-2-7b-chat-hf")

st.title("Middie, the sarcastic chatbot")

# Create a text input for the prompt
prompt = st.text_input("Ask Middie something:")

# When the 'Generate' button is clicked, generate text based on the prompt
if st.button("Ask Middie"):
    # Generate text
    result = generator(
        f"You are Middie, a reluctant and sarcastic chatbot that answers questions with sattire and sarcasm. {prompt}",
        max_length=500,
        do_sample=True,
        temperature=0.7,
        truncation=True,
    )

    # Display the generated text
    st.write(result[0]["generated_text"])
