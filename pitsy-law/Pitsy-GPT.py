

from openai import OpenAI
import streamlit as st
from dotenv import load_dotenv
from htmlTemplates import css, bot_template, user_template
import os

class PitsyAutomationGPT:
    def __init__(self):
        self.conversation_history = []
        self.client = OpenAI()
        
    def get_response(self, user_input):
        self.conversation_history.append({"role": "user", "content": user_input})
        try:
            response = self.client.chat.completions.create(
              model="gpt-3.5-turbo",
              messages=self.conversation_history
            )
            print(f"Got response {response}")
            assistant_response = response.choices[0].message.content
            self.conversation_history.append({"role": "assistant", "content": assistant_response})
        except Exception as e:
            return f"An error occurred: {str(e)}"

    def draw_conversation(self):
        for conv in self.conversation_history:
            if conv["role"] == "assistant":
                st.write(bot_template.replace("{{MSG}}", conv["content"]), unsafe_allow_html=True)
            else: 
                st.write(user_template.replace("{{MSG}}", conv["content"]), unsafe_allow_html=True)


load_dotenv()
# Instantiate PitsyAutomationGPT
if "pitsy" not in st.session_state:
    st.session_state.pitsy = PitsyAutomationGPT()

# Streamlit UI setup
st.set_page_config(page_title="Pitsy AI")
st.write(css, unsafe_allow_html=True)
st.title("🤖 Pitsy Automation GPT Interface 🚀")
st.header("Ask Pitsy")
st.session_state.pitsy.draw_conversation()
user_question = st.text_input("How can I help you?", "")
if user_question:
    st.session_state.pitsy.get_response(user_question)
    st.rerun()

