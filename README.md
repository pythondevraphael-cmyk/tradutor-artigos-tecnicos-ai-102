[![Status](https://img.shields.io/badge/Status-MVP%20Concluído-brightgreen)](https://github.com/raphaelmendes-dev/Technical-Article-Translator)
[![Python](https://img.shields.io/badge/Python-3.12+-blue?logo=python&logoColor=white)](https://www.python.org/)
[![Streamlit](https://img.shields.io/badge/Streamlit-Web%20App-FF4B4B?logo=streamlit&logoColor=white)](https://streamlit.io/)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

<div align="center">
  <h1>Technical-Article-Translator</h1>
  <p><strong>Tradutor de Artigos Técnicos com Preservação Terminológica Determinística</strong></p>
  <p>Tradução precisa de textos de IA/ML/Azure mantendo termos técnicos intactos – 100% local e gratuito.</p>

  <p>
    <a href="https://github.com/raphaelmendes-dev"><strong>Meu GitHub</strong></a> •
    <a href="https://www.linkedin.com/in/raphaelmendes-dev/">LinkedIn</a> •
    <a href="mailto:python.dev.raphael@gmail.com">Contato</a>
  </p>

  <p><em>README em <a href="README.en.md">English</a></em></p>
</div>

## 🎯 Visão Geral

Solução de tradução automática para artigos técnicos que garante **precisão terminológica** em domínios como IA, ML e Azure.  

- Usa **glossário determinístico** com proteção robusta (substituição sequencial + restauração pós-tradução)
- Evita alterações indesejadas em termos chave: LLM, RAG, prompt engineering, Azure AI, etc.
- Interface Streamlit simples e interativa

Inspirado no Azure AI Translator + Custom Translator, implementado localmente sem dependências de nuvem.

## ✨ Funcionalidades

- Cole texto técnico (qualquer idioma de origem)
- Tradução para inglês, espanhol, francês, alemão, italiano
- Glossário customizado preserva termos exatos (case-insensitive)
- Interface com duas colunas (original vs traduzido)
- Botão limpar e feedback de processamento

Fluxo: Texto → Proteção determinística → Tradução → Restauração → Resultado seguro.

## 🛠️ Stack Técnica

- Backend → Python 3.12+
- UI → Streamlit
- Tradução → deep-translator (Google Translate gratuito)
- Glossário/Proteção → re (regex), dicionário customizado

## 🚀 Como Rodar

- CloneBashgit clone https://github.com/raphaelmendes-dev/Technical-Article-Translator.git
- cd Technical-Article-Translator
- Ambiente virtualBashpython -m venv venv
- venv\Scripts\activate  # Windows
- ou source venv/bin/activate  # Linux/Mac
- DependênciasBashpip install streamlit deep-translator
- ExecuteBashstreamlit run app.py

Acesse: http://localhost:8501

## 💡 Como Usar

- nCole artigo técnico (ex.: texto sobre LLM, Azure AI)
- Escolha idioma alvo
- Clique em "Traduzir" → veja termos preservados

## 📊 Resultados & Diferenciais

- 100% determinístico na preservação de terminologia (sem alucinações)
- Alta precisão em textos de IA/ML/Azure
- Solução gratuita e local (sem chave API)
- Escalável: pode integrar Azure AI Translator real ou Ollama local no futuro

## 🤝 Contribua
Contribuições bem-vindas! Fork → branch → PR.
A
Tradutores customizados, processamento de texto técnico, arquiteturas híbridas (determinístico + IA), Azure AI, Streamlit, FastAPI.
Projetos funcionais entregues.

Contato: raphaelmendes-dev | python.dev.raphael@gmail.com | LinkedIn

## ⭐ Dê uma estrela se ajudou!


Última atualização: Março 2026
