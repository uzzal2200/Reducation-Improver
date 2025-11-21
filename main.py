import streamlit as st
from langchain_core.prompts import PromptTemplate
from langchain_groq import ChatGroq

# ---------------------------
# Prompt Template
# ---------------------------
template = """
Below is a draft text. Your job is to:
- Rewrite the text
- Apply the desired tone
- Convert to the desired English dialect
- Start with a warm introduction

DRAFT: {draft}
TONE: {tone}
DIALECT: {dialect}

YOUR {dialect} RESPONSE:
"""

prompt = PromptTemplate(
    input_variables=["draft", "tone", "dialect"],
    template=template,
)

# ---------------------------
# Streamlit App UI
# ---------------------------
st.set_page_config(page_title="Re-write your text")
st.header("Re-write your text")

st.markdown("Rewrite your text in different styles – by **MD Uzzal Mia**")

# API Key input
st.markdown("## Enter Your Groq API Key")
groq_api_key = st.text_input("Groq API Key", type="password")

# Model input
model_input = st.text_input(
    "Groq Model (optional)",
    placeholder="mixtral-8x7b-32768"
)

# Draft text
st.markdown("## Enter the text you want to re-write")
draft_input = st.text_area("", placeholder="Your text...")

if len(draft_input.split()) > 700:
    st.error("Maximum length is 700 words.")
    st.stop()

# Tone + Dialect
col1, col2 = st.columns(2)
with col1:
    option_tone = st.selectbox("Tone", ["formal", "informal"])
with col2:
    option_dialect = st.selectbox("Dialect", ["American", "British"])

# Output title
st.markdown("### Your Re-written Text:")

# ---------------------------
# Generate Output
# ---------------------------
if draft_input:
    if not groq_api_key:
        st.warning("Please enter your Groq API key.")
        st.stop()

    model_name = model_input if model_input else "mixtral-8x7b-32768"

    # Load LLM
    try:
        llm = ChatGroq(
            groq_api_key=groq_api_key,
            model=model_name,
            temperature=0.7
        )
    except Exception as e:
        st.error("Could not load the model. Check your API key or model name.")
        st.exception(e)
        st.stop()

    # Build prompt
    final_prompt = prompt.format(
        draft=draft_input,
        tone=option_tone,
        dialect=option_dialect
    )

    # Call Groq LLM
    try:
        response = llm.invoke(final_prompt)

        # Extract pure text only
        if hasattr(response, "content"):
            st.write(response.content)
        else:
            st.write(str(response))

    except Exception as e:
        st.error("Model call failed.")
        st.exception(e)
