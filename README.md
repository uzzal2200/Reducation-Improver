<!--
	Professional README written for developer consumption. Keep this
	concise and focused: setup, architecture, usage, troubleshooting.
-->

# Redaction & Rewrite — Streamlit LLM Rewrite App

[![Python](https://img.shields.io/badge/python-3.11-blue.svg)](https://www.python.org/)
[![Streamlit](https://img.shields.io/badge/streamlit-%3E%3D1.0-orange.svg)](https://streamlit.io/)
[![LangChain](https://img.shields.io/badge/langchain-compatible-important.svg)](https://github.com/langchain-ai/langchain)
[![Groq](https://img.shields.io/badge/groq-provided-lightgrey.svg)](https://console.groq.com/)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)

Short description
-----------------

Redaction & Rewrite is a focused Streamlit prototype that rewrites or
redacts user-provided draft text into a chosen tone and dialect using
Groq models orchestrated via LangChain. The app cleans provider
metadata and returns plain, human-readable text suitable for
copy/paste into customer-facing interfaces.

When to use this repo
----------------------
- Rapid prototyping of text rewrite/redaction flows with Groq LLMs.
- Reference implementation for integrating `langchain_groq` into a
	Streamlit UI.

Quick setup (developer)
------------------------
1. Create a Conda environment (recommended):

```powershell
conda create -n llmapp python=3.11 -y
conda activate llmapp
```

2. Install runtime dependencies:

```powershell
pip install -r requirements.txt
```

3. Run locally:

```powershell
streamlit run main.py
```

4. In the UI provide:
- Groq API key (never commit; enter into the secure input field)
- Optional Groq model name (if the default model is decommissioned)
- Draft text, tone, and dialect

Architecture 
---------------------

The runtime flow is intentionally minimal and robust: prompt
construction → LLM call → generation extraction → post-processing →
UI output.

If your viewer does not render diagrams, open `assets/architecture.svg`.

<p align="center">
	<a href="./assets/architecture.svg" target="_blank">
		<img src="assets/architecture.svg" alt="Architecture diagram" style="max-width:100%;height:auto;border:1px solid #ddd;padding:6px;"/>
	</a>
</p>

Core pipeline (text):

```
[User] -> [Streamlit App (`main.py`)] -> [PromptTemplate] -> [LangChain ChatGroq client] -> [Groq model] -> [Extractor & Cleaner] -> [UI Output]
```

How it works (details)
----------------------
- Prompt assembly: `main.py` defines a `PromptTemplate` that combines
	tone and dialect examples with the user's draft.
- LLM call: the app creates a `langchain_groq.ChatGroq` client and
	sends a single chat-style message (as a plain dict) for compatibility
	across LangChain versions.
- Extraction: the app reads the top generation (`resp.generations[0][0]`)
	and prefers `generation.message.content` then `generation.text`.
- Cleaning: provider metadata is removed by a small extractor so the
	UI shows only the rewritten text.

Configuration
-------------
- `Groq API Key`: provided at runtime in the UI. Keep it secret.
- `Groq Model`: optional override for situations where the default is
	decommissioned.

Troubleshooting
---------------
- model_decommissioned: supply a supported model name or check
	Groq deprecations: https://console.groq.com/docs/deprecations
- installation issues: prefer a fresh Conda env and install binary
	packages (numpy) via Conda if pip wheels fail
- import errors in editors: ensure the IDE uses the same Python
	interpreter/environment you use to run Streamlit

Developer notes
---------------
- Primary file: `main.py` — prompt, client creation, extraction,
	post-processing, and Streamlit UI.
- Prompt tuning: edit the `PromptTemplate` examples in `main.py` to
	change redaction rules, tone guidance, or dialect vocabulary.
- Tests & CI: consider adding a quick syntax test (`python -m
	py_compile main.py`) and a lightweight CI workflow to validate the
	app starts cleanly.

Contributing
------------
- Fork and open a PR. Keep changes small and focused (prompt text,
	docs, tests). Add unit tests for any non-trivial extraction logic.

License
-------
MIT — see the `LICENSE` file.

Contact
-------
Maintainer: MD Uzzal Mia — update contact details as needed.

---
MD Uzzal Mia