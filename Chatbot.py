import openai
import streamlit as st

# insert an image

st.image("./ucf_logo.jpg", width=700)

with st.sidebar:
    openai_api_key = st.text_input(
        "OpenAI API Key", key="chatbot_api_key", type="password"
    )
    "[Get an OpenAI API key](https://platform.openai.com/account/api-keys)"


st.title("Learn Simulation with ChatGPT")
# st.caption("🚀 A streamlit chatbot powered by OpenAI LLM")

# radio
st.subheader("Select a topic to learn")
topic = st.radio(
    "",
    (
        "Input analysis",
        "Simulation model building",
        "Output analysis",
        "Verification and validation",
        "Design of simulation experiments",
    ),
)

# slide bar for temperature
st.subheader("Select a temperature")
temperature = st.slider("", 0.0, 1.0, 0.5, 0.1)

if "messages" not in st.session_state:
    st.session_state["messages"] = [
        {"role": "assistant", "content": "How can I help you?"}
    ]

for msg in st.session_state.messages:
    st.chat_message(msg["role"]).write(msg["content"])

if prompt := st.chat_input():
    if not openai_api_key:
        st.info("Please add your OpenAI API key to continue.")
        st.stop()

    openai.api_key = openai_api_key
    st.session_state.messages.append({"role": "user", "content": prompt})
    st.chat_message("user").write(prompt)
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo", messages=st.session_state.messages
    )
    msg = response.choices[0].message
    st.session_state.messages.append(msg)
    st.chat_message("assistant").write(msg.content)
