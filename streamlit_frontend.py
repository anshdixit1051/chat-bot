import uuid
import streamlit as st
from langgraph_backend import chatbot
from langchain_core.messages import HumanMessage

# ---------- session setup ----------
if 'thread_id' not in st.session_state:
    st.session_state['thread_id'] = str(uuid.uuid4())

if 'message_history' not in st.session_state:
    st.session_state['message_history'] = []

CONFIG = {'configurable': {'thread_id': st.session_state['thread_id']}}

# ---------- sidebar ----------
with st.sidebar:
    if st.button('New chat'):
        st.session_state['thread_id'] = str(uuid.uuid4())
        st.session_state['message_history'] = []
        st.rerun()

# ---------- show previous messages ----------
for message in st.session_state['message_history']:
    with st.chat_message(message['role']):
        st.markdown(message['content'])

# ---------- handle new input ----------
user_input = st.chat_input('Type here')

if user_input:
    st.session_state['message_history'].append({'role': 'user', 'content': user_input})
    with st.chat_message('user'):
        st.markdown(user_input)

    with st.chat_message('assistant'):
        try:
            with st.spinner('Thinking...'):
                response = chatbot.invoke(
                    {'messages': [HumanMessage(content=user_input)]},
                    config=CONFIG,
                )
            ai_message = response['messages'][-1].content
            st.markdown(ai_message)
            st.session_state['message_history'].append(
                {'role': 'assistant', 'content': ai_message}
            )
        except Exception as e:
            st.error(f'Something went wrong: {e}')