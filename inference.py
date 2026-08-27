import json

import requests
import streamlit as st

OLLAMA_URL = "http://localhost:11434/api/chat"
MODEL = "tinyllama"

st.set_page_config(page_title="TinyLlama Chat", page_icon="💬")
st.title("💬 TinyLlama Chat")

# Keep chat history across reruns
if "messages" not in st.session_state:
    st.session_state.messages = []

# Render previous messages
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])


def stream_ollama(messages):
    """Stream tokens from Ollama's chat endpoint."""
    payload = {"model": MODEL, "messages": messages, "stream": True}
    with requests.post(OLLAMA_URL, json=payload, stream=True, timeout=300) as r:
        r.raise_for_status()
        for line in r.iter_lines():
            if not line:
                continue
            chunk = json.loads(line)
            token = chunk.get("message", {}).get("content", "")
            if token:
                yield token
            if chunk.get("done"):
                break


# Chat input — Streamlit waits here for every new question
if prompt := st.chat_input("Ask me anything..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        try:
            response = st.write_stream(stream_ollama(st.session_state.messages))
        except requests.exceptions.ConnectionError:
            st.error("Cannot reach Ollama at localhost:11434. Is `ollama serve` running?")
            st.stop()
        except requests.exceptions.HTTPError as e:
            st.error(f"Ollama error: {e}. Did you pull the model? Try: ollama pull tinyllama")
            st.stop()

    st.session_state.messages.append({"role": "assistant", "content": response})
