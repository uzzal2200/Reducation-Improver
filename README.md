# Redaction & Rewrite — Streamlit LLM Rewrite App

[![Python](https://img.shields.io/badge/python-3.11-blue.svg)](https://www.python.org/)
[![Streamlit](https://img.shields.io/badge/streamlit-%3E%3D1.0-orange.svg)](https://streamlit.io/)
[![LangChain](https://img.shields.io/badge/langchain-compatible-important.svg)](https://github.com/langchain-ai/langchain)
[![Groq](https://img.shields.io/badge/groq-provided-lightgrey.svg)](https://console.groq.com/)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)

Professional, minimal Streamlit app that rewrites or redacts draft text
into a chosen tone and dialect using a Groq LLM via LangChain. The
output is cleaned of provider metadata and returned as plain, human
readable text suitable for direct use in user-facing content.

This README provides concise setup steps, architecture details, and
troubleshooting guidance for local development and evaluation.

## Quick Start

1. Create and activate a Conda environment (recommended):

```powershell
conda create -n llmapp python=3.11 -y; conda activate llmapp
```

2. Install dependencies:

```powershell
pip install -r requirements.txt
```

3. Run locally:

```powershell
streamlit run main.py
```

4. In the UI provide:
- your Groq API key (never commit it)
- an optional Groq model name if the default is decommissioned
- the draft text, tone, and dialect

## Architecture & Visual Diagram

The application follows a small, clear pipeline: prompt construction →
LLM request → generation extraction → post-processing → UI output.

If the diagram below does not render in your viewer, open
`assets/architecture.svg` directly in your browser or click the image.

<p align="center">
	<a href="./assets/architecture.svg" target="_blank">
		<img src="assets/architecture.svg" alt="Architecture diagram" style="max-width:100%;height:auto;"/>
	</a>
</p>

Mermaid flowchart (for renderers that support it):

```mermaid
flowchart LR
	U[User Browser / Streamlit UI]
	U -->|enter draft, tone, dialect, API key| S[Streamlit App (`main.py`)]
	S --> P[PromptTemplate]
	P --> R[Formatted Prompt]
	R --> L[LangChain: ChatGroq Client]
	L --> G[Groq API / Model]
	G --> M[Model Response (may include metadata)]
	M --> X[Post-process: Extract & Clean]
	X --> O[UI Output: Clean rewritten text]
```

Text (linear):

```
[User] -> [Streamlit App (main.py)] -> [PromptTemplate] -> [ChatGroq client] -> [Groq Model] -> [Extract & Clean] -> [UI Output]
```

## How it works (technical)

- The `PromptTemplate` in `main.py` injects the draft plus tone/dialect
	examples into a structured prompt.
- The app uses `langchain_groq.ChatGroq` to create a client and sends a
	single chat-style message as a plain dict: `{ "role": "user",
	"content": <prompt> }` for broad compatibility.
- The top generation is read from `resp.generations[0][0]`. The code
	prefers `generation.message.content` then `generation.text` before
	falling back to `str(gen)`.
- A small extractor strips provider metadata such as
	`content='...' response_metadata=...` so the UI shows only human
	readable text.

## Troubleshooting

- If you receive a `model_decommissioned` error, enter a supported
	model name in the "Groq Model (optional)" field or consult:
	https://console.groq.com/docs/deprecations
- If `pip install` fails on binary packages (e.g. `numpy`), prefer a
	fresh Conda env or install the heavy packages via Conda.
- Ensure your editor/IDE uses the same Python environment you run
	Streamlit from to avoid import errors (e.g. `langchain_core`).

## Developer notes

- Main file: `main.py` — prompt, LLM client, extraction, and UI logic.
- To adjust rewrite behavior, edit the `PromptTemplate` examples in
	`main.py`.
- Consider adding a lightweight test that validates prompt formatting
	and that `main.py` compiles.

## License

MIT — update `LICENSE` if you choose a different license.

---
MD Uzzal Mia