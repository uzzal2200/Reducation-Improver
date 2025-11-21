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

## Architecture & How It Works

At a high level the app follows a simple pipeline:

1. **Prompt construction** — `main.py` defines a `PromptTemplate`
	 that includes examples for tone and dialect and injects the user
	 draft text.
2. **LLM invocation** — the app creates a `ChatGroq` client (from
	 `langchain_groq`) using the provided API key. A single chat-style
	 request is sent as a plain dict message: `{ "role": "user",
	 "content": <prompt> }`.
3. **Generation extraction** — the code reads the top generation from
	 `resp.generations[0][0]`. It prefers `generation.message.content`
	 when available, or falls back to `generation.text` or `str(gen)`.
4. **Post-processing** — because some provider responses include
	 metadata (for example `content='...' response_metadata=...`), the
	 app runs a small extraction routine that strips provider metadata
	 and returns only the human-readable rewritten text.
5. **Display** — the cleaned rewrite is shown in the Streamlit UI.

This architecture intentionally uses a minimal, robust call pattern
that avoids importing provider-specific message classes. Using a dict
message improves compatibility across LangChain and provider adapter
versions.

Detailed architecture

Rendered diagram (SVG):

![Architecture diagram](assets/architecture.svg)

Mermaid (flowchart):

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
  style U fill:#f9f,stroke:#333,stroke-width:1px
  style S fill:#cff,stroke:#333,stroke-width:1px
  style G fill:#fee,stroke:#333,stroke-width:1px
  style X fill:#efe,stroke:#333,stroke-width:1px
```

ASCII fallback (linear):

```
[User Browser / Streamlit UI]
	|
	v
[Streamlit App (`main.py`)]
	|
	v
[PromptTemplate] -> [Formatted Prompt]
	|
	v
[LangChain ChatGroq Client]
	|
	v
[Groq API / Model]
	|
	v
[Model Response (possible metadata)]
	|
	v
[Extractor & Cleaner] -> [Clean human-readable rewrite]
	|
	v
[UI Output]
```

The diagram shows the runtime flow: the Streamlit UI collects the
inputs, `main.py` formats the prompt, sends it via the LangChain
`ChatGroq` adapter to the Groq model, then extracts and cleans the
response before rendering it back in the UI.

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