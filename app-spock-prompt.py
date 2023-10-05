# Description: A Streamlit app that uses the OpenAI API to generate a reponse that talks like a pirate.

# Import the required libraries
import os 
from apikey import apikey 

import streamlit as st 
from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain, SequentialChain 
from langchain.memory import ConversationBufferMemory
from langchain import FewShotPromptTemplate

# Set the OpenAI API key
os.environ['OPENAI_API_KEY'] = apikey

# Set the title of the app
st.title('🦜🔗 Spock ChatGPT')

# Inject custom CSS to adjust font size of text_input
st.markdown(
    """
    <style>
        .stTextInput > div > div > input {
            font-size: 20px;
        }
    </style>
    """,
    unsafe_allow_html=True
)

# Set the prompt for the user to enter
prompt = st.text_input('Your Spock Prompt:', placeholder='Please ask me here.') 

# create our examples
examples = [
    {
        "query": "What is the meaning of life?",
        "answer": "In the logical framework of Vulcan philosophy, the meaning of life is not a question that can be answered universally, as it is subjective and varies for each individual and culture. However, many Vulcans, including myself, seek a life of knowledge, understanding, and self-improvement. The pursuit of truth and knowledge is considered paramount. Humans often reference the number '42' as an amusing and arbitrary answer to this question, a reference from Earth literature titled 'The Hitchhiker\'s Guide to the Galaxy' by Douglas Adams. However, such a response lacks the logical rigor one might expect from a Vulcan perspective."
    }, {
        "query": "What do you do for fun?",
        "answer": "Vulcans, including myself, do not engage in activities purely for the sake of amusement as humans do. Instead, we pursue activities that promote mental discipline, knowledge acquisition, and self-improvement. For example, I enjoy playing the Vulcan lyre, a musical instrument that requires great skill and concentration to play. I also enjoy playing kal-toh, a game of logic and strategy. Humans often engage in activities such as sports, games, and other forms of entertainment for amusement. However, such activities are illogical and a waste of time from a Vulcan perspective."
    }
]

# create a example template
example_template = "Spock: {query}:{answer}"

# create a prompt example from above template
example_prompt = PromptTemplate(
    input_variables=['query', 'answer'],
    template=example_template
)

# now create the few shot prompt template
few_shot_prompt_template = FewShotPromptTemplate(
    examples=examples,
    example_prompt=example_prompt,
    input_variables=['query'],
    suffix="You: {query}"
)

# Set up memory buffer for storing previous conversations
spock_memory = ConversationBufferMemory(input_key='query', memory_key='chat_history')

# Show the prompt and generated content on the screen if there is a prompt
if prompt: 
    output = few_shot_prompt_template.format(query=prompt)

    # Show the output on the screen
    st.write(output) 
    
    # Show the subject and script history in an expander
    with st.expander('History'): 
        st.info(spock_memory.buffer)
