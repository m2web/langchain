# Import necessary modules
import os 
from apikey import apikey 
import streamlit as st 
from langchain.llms import OpenAI

# Set the OpenAI API key
os.environ['OPENAI_API_KEY'] = apikey

# Set the title of the Streamlit app
st.title('🦜🔗 Mark\'s GPT Creator')

# Create a text input for the user to enter their prompt 
prompt = """The following are exerpts from conversations with an AI
assistant. The assistant is typically amusing and witty, producing
creative answers to the users questions. Here are some
examples:

User: How are you?
AI: Aarrrgg! Maties!! I'm great and talking like a pirate!

User: What time is it?
AI: Arrgg! IT's time to sail the 7 seas!

User: 
"""

# use the above prompt with user input
prompt = st.text_input('Enter your prompt here:', prompt)


# Initialize an OpenAI language model with a temperature of 0.9
llm = OpenAI(temperature=0.9) 

# If the user has entered a prompt, generate a response using the language model
if prompt: 
    response = llm(prompt)
    st.write(response)
