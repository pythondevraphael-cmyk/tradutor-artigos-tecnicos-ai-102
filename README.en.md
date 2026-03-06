[![Status](https://img.shields.io/badge/Status-MVP%20Completed-brightgreen)](https://github.com/raphaelmendes-dev/Technical-Article-Translator)
[![Python](https://img.shields.io/badge/Python-3.12+-blue?logo=python&logoColor=white)](https://www.python.org/)
[![Streamlit](https://img.shields.io/badge/Streamlit-Web%20App-FF4B4B?logo=streamlit&logoColor=white)](https://streamlit.io/)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

<div align="center">
  <h1>Technical Article Translator</h1>
  <p><strong>Technical Article Translator with Deterministic Terminology Preservation</strong></p>
  <p>Accurate translation of AI/ML/Azure texts keeping key terms intact – fully local & free.</p>

  <p>
    <a href="https://github.com/raphaelmendes-dev"><strong>My GitHub</strong></a> •
    <a href="https://www.linkedin.com/in/raphaelmendes-dev/">LinkedIn</a> •
    <a href="mailto:python.dev.raphael@gmail.com">Contact</a>
  </p>

  <p><em>README in <a href="README.md">Português</a></em></p>
</div>

## 🎯 Overview

Automatic translation tool for technical articles ensuring **terminology precision** in AI, ML, and Azure domains.

- Deterministic glossary protection (sequential markers + post-translation restoration)
- Prevents unwanted changes to key terms: LLM, RAG, prompt engineering, Azure AI, etc.
- Simple and interactive Streamlit interface

Azure AI Translator + Custom Translator inspired, implemented locally without cloud dependencies.

## ✨ Features

- Paste technical text (any source language)
- Translation to English, Spanish, French, German, Italian
- Custom glossary preserves exact terms (case-insensitive)
- Side-by-side view (original vs translated)
- Clear button and processing feedback

Flow: Text → Deterministic protection → Translation → Restoration → Secure result.

## 🛠️ Tech Stack

- Backend → Python 3.12+
- UI → Streamlit
- Translation → deep-translator (free Google Translate)
- Glossary/Protection → re (regex), custom dictionary

## 🚀 Quick Start

- CloneBashgit clone https://github.com/raphaelmendes-dev/Technical-Article-Translator.git
- cd Technical-Article-Translator
- Virtual envBashpython -m venv venv
- venv\Scripts\activate  # Windows
- or source venv/bin/activate
- InstallBashpip install streamlit deep-translator
- RunBashstreamlit run app.py

Access: http://localhost:8501

## 💡 How to Use

- Paste technical article (e.g., text about LLM, Azure AI)
- Select target language
- Click "Translate" → see preserved terms

## 📊 Results & Differentiators

- 100% deterministic terminology preservation (no hallucinations)
- High accuracy on AI/ML/Azure texts
- Free and local solution (no API key needed)
- Scalable: future Azure AI Translator or local Ollama integration

## 🤝 Contribute or Freelance
Contributions welcome! Fork → branch → PR.

Custom translators, technical text processing, hybrid architectures, Azure AI, Streamlit, FastAPI.
Delivered functional projects.

Contact: raphaelmendes-dev | python.dev.raphael@gmail.com | LinkedIn


## ⭐ Star if you like it!


Last update: March 2026
