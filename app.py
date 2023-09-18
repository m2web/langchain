# Import necessary modules
import os 
from apikey import apikey 
import streamlit as st 
from langchain.llms import OpenAI

# Set the OpenAI API key
os.environ['OPENAI_API_KEY'] = apikey

# Set the title of the Streamlit app
st.title('🦜🔗 Mark\'s GPT Creator')

def generate_response(llm, prompt):
    """
    Generates a response using the specified language model and prompt.
    """
    response = llm(prompt)
    # clear the prompt textbox
    st.text_input('Enter your prompt here:', '')
    st.write(response)

# Initialize an OpenAI language model with a temperature of 0.9
llm = OpenAI(temperature=0.9) 

# Create a text input for the user to enter their prompt 
prompt = """It's talke like a pirate day so please respond as a priate would talk. Here are some
examples:

User: How are you?
AI: Aarrrgg! Maties!! I'm great and talking like a pirate!

User: What time is it?
AI: Arrgg! IT's time to sail the 7 seas!
"""

# use the above prompt with user input
prompt = st.text_input('Enter your prompt here:', prompt)

# If the user has entered a prompt, generate a response using the language model
if prompt: 
    generate_response(llm, prompt)
