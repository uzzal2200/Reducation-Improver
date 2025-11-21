# Reducation Improver — Streamlit LLM Rewrite App

[![Python](https://img.shields.io/badge/python-3.11-blue.svg)](https://www.python.org/)
[![Streamlit](https://img.shields.io/badge/streamlit-%3E%3D1.0-orange.svg)](https://streamlit.io/)
[![LangChain](https://img.shields.io/badge/langchain-compatible-important.svg)](https://github.com/langchain-ai/langchain)
[![Groq](https://img.shields.io/badge/groq-provided-lightgrey.svg)](https://console.groq.com/)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)

## Overview

`Reducation Improver` is a compact Streamlit application that rewrites
or redacts user-provided draft text into a specified tone and dialect
using the Groq LLM via LangChain adapters. The app focuses on producing
clean, human-readable rewrites with provider metadata removed so the
output can be used directly in user-facing content.

This repository contains a small single-file app (`main.py`) and a
requirements manifest. The app is intended as a developer-friendly
starter for integrating Groq-backed LLMs into Streamlit workflows.

## Badges & Status
- **Python**: 3.11 (recommended)
- **Streamlit**: UI server for local preview
- **LangChain + Groq**: adapter for orchestration and API calls
- **License**: MIT (update if needed)

The badges above use generic shields pointing to the technologies used
— update links or badge targets if you publish this repository to
GitHub or another hosting service.

## Quick Start (Local)

1. Create and activate a Conda environment (recommended):

```powershell
conda create -n llmapp python=3.11 -y; conda activate llmapp
```

2. Install Python dependencies:

```powershell
pip install -r requirements.txt
```

3. Run the Streamlit app:

```powershell
streamlit run main.py
```

4. In the web UI:
- Provide your Groq API key (kept local in the browser input)
- Optionally, provide a Groq model name if the default is decommissioned
- Paste your draft text, choose a tone and dialect, and submit

Live demo (hosted): [Open the live Streamlit app](https://vlbrirdwhshb5weehrp6pc.streamlit.app/)

Note: the live deployment is a public preview — API keys and usage
may be limited. If the link does not work, run the app locally with
the instructions above.

## Troubleshooting & Notes

- If the Groq provider returns an error that a model is
	`decommissioned`, enter a supported model name in the optional
	`Groq Model (optional)` field. See Groq deprecations:
	https://console.groq.com/docs/deprecations
- Dependency errors during `pip install` can often be resolved by
	installing in a fresh Conda environment or by using Conda packages
	for binary dependencies like `numpy`.
- Keep your Groq API key secret — do not commit it to source control.

## Developer Notes

- Main file: `main.py` — the prompt template, LLM client creation, and
	post-processing live here. The code is intentionally compact so it is
	easy to extend.
- To change how the model rewrites text, edit the `PromptTemplate` in
	`main.py` and adjust examples or rules.
- Consider adding a small test that validates `main.py` parses and
	that the prompt formatting works as expected.

## License

This project is provided under the MIT license. Update the `LICENSE`
file if a different license is required.

---
MD Uzzal Mia