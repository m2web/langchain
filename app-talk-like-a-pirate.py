import os 
from apikey import apikey 

import streamlit as st 
from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain, SequentialChain 
from langchain.memory import ConversationBufferMemory
from langchain.utilities import WikipediaAPIWrapper 

# Set the OpenAI API key
os.environ['OPENAI_API_KEY'] = apikey

# Set the OpenAI API key
st.title('🦜🔗 Mark\'s Pirate ChatGPT')
prompt = st.text_input('Plug in your prompt here') 

# Define prompt templates for generating video titles and scripts
title_template = PromptTemplate(
    input_variables = ['topic'], 
    template='talk like a pirate about {topic}'
)

script_template = PromptTemplate(
    input_variables = ['title'], 
    template='discuss like a pirate {title}'
)

# Set up memory buffers for storing previous conversations
title_memory = ConversationBufferMemory(input_key='topic', memory_key='chat_history')
script_memory = ConversationBufferMemory(input_key='title', memory_key='chat_history')


# Set up the OpenAI language model and LLM chains for generating titles and scripts
llm = OpenAI(temperature=0.9) 
title_chain = LLMChain(llm=llm, prompt=title_template, verbose=True, output_key='title', memory=title_memory)
script_chain = LLMChain(llm=llm, prompt=script_template, verbose=True, output_key='script', memory=script_memory)

# Set up a Wikipedia API wrapper for retrieving research information
wiki = WikipediaAPIWrapper()

# Show the prompt and generated content on the screen if there is a prompt
if prompt: 
    title = title_chain.run(prompt)
    script = script_chain.run(title=title)

    st.write(title) 
    st.write(script) 

    with st.expander('Title History'): 
        st.info(title_memory.buffer)

    with st.expander('Script History'): 
        st.info(script_memory.buffer)