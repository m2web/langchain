# How to Build an AutoGPT App 🦜🔗

Here are my steps in learning how to build an AutoGPT app with this forked repository. Thanks to [https://github.com/nicknochnack/Langchain-Crash-Course](https://github.com/nicknochnack/Langchain-Crash-Course).

## Forking the Repository and then removing the .git folder

I forked the repository and then removed the .git folder so that I could start fresh with my own repository.

## Adding More Detailed Comments

Then, I got Copilot Chat to assist me with more detailed comments the app.py file. Now that I have more explicit comments I created a new branch to add the comments:

```bash
git checkout -b add-comments-to-app.py
```

## Adding Dependencies

Then, per the video on YouTube I added the code's dependencies via pip:

```python
pip install streamlit langchain openai wikipedia chromadb tiktoken
```

## Readme.md

Next, I created a new branch off the main branch for this readme file

```bash
git checkout -b add-readme
```

And, no surprise, I added this readme.md to the branch and committed it and switched back to the main branch, and merged the add-readme branch into the main branch:

```bash
git merge add-readme
```

I then merged the add-comments-to-app.py branch into the main branch:

```bash
git merge add-comments-to-app.py
```

# add apikey.py file
Next, I added an apikey.py file to the main branch and added the following:

```python
apikey = 'your apikey here'
```

Of course, I replaced the 'your apikey here' with my actual OpenAI API key.

## Add a .gitignore file

I added a .gitignore file to the main branch and added the following to it:

```bash
apikeys.py
```

This way, my apikeys.py file will not be uploaded to GitHub since it contains my OpenAI API key. The file has only one line in it:

```python
apikey = 'your apikey here'
```

## Minimal app.py file

Here is a minimal app.py file I created:

```python
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
prompt = st.text_input('Plug in your prompt here') 

# Initialize an OpenAI language model with a temperature of 0.9
llm = OpenAI(temperature=0.9) 

# If the user has entered a prompt, generate a response using the language model
if prompt: 
    response = llm(prompt)
    st.write(response)
```
