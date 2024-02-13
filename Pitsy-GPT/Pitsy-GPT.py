import openai
import streamlit as st

class PitsyAutomationGPT:
    def __init__(self):
        # Directly setting the API key - not recommended for production
        self.api_key = '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'
        openai.api_key = self.api_key
        self.conversation_history = []

    def get_response(self, user_input):
        self.conversation_history.append({"role": "user", "content": user_input})
        try:
            response = openai.ChatCompletion.create(
              model="gpt-3.5-turbo",
              messages=self.conversation_history
            )
            assistant_response = response['choices'][0]['message']['content']
            self.conversation_history.append({"role": "assistant", "content": assistant_response})
            return assistant_response
        except Exception as e:
            return f"An error occurred: {str(e)}"

# Instantiate PitsyAutomationGPT
pitsy = PitsyAutomationGPT()

# Streamlit UI setup
st.title("🤖 Pitsy Automation GPT Interface 🚀")

st.header("💬 Let's Chat!")
user_input = st.text_input("📝 Type your message here:")
if st.button("🔍 Get Response"):
    response = pitsy.get_response(user_input)
    if response:
        st.success(f"🤖 AI Response: {response}")
    else:
        st.error("Failed to get a response. Please check your API key and internet connection.")
