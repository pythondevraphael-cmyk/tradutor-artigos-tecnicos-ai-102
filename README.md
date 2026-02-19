# Tradutor de Artigos Técnicos com Precisão Terminológica

![Python](https://img.shields.io/badge/Python-3.10+-blue?logo=python&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-App-red?logo=streamlit&logoColor=white)
![Azure](https://img.shields.io/badge/Azure-AI-lightblue?logo=microsoftazure&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-green)

**Projeto Final – Bootcamp Microsoft Certification Challenge AI-102 (DIO)**

## Objetivo do Desafio
Desenvolver uma solução de tradução automática de artigos técnicos utilizando Azure AI, com foco em garantir **precisão terminológica** e contexto específico do domínio técnico (ex: Inteligência Artificial, Machine Learning, Azure).

## Problema Enfrentado
Não foi possível criar o recurso Azure AI Translator devido à rejeição sistemática de cartões brasileiros no cadastro do Azure Free Tier (problema conhecido e confirmado pela equipe DIO – Beatriz/Support).

## Solução Alternativa Implementada
- **Interface**: Streamlit (aplicativo web simples e interativo)  
- **Tradução**: Biblioteca `deep-translator` (usa Google Translate de forma gratuita e ilimitada)  
- **Precisão terminológica**: Glossário customizado em Python com proteção robusta de termos (marcadores únicos sequenciais para evitar alterações indesejadas durante a tradução)  
- Preserva termos técnicos como: `machine learning`, `Azure AI`, `Custom Translator`, `prompt engineering`, `RAG`, `LLM`, etc.

## Como Executar Localmente

1. Clone o repositório:
   ```bash
   git clone https://github.com/SEU_USUARIO/tradutor-artigos-tecnicos-ai-102.git
   cd tradutor-artigos-tecnicos-ai-102

2. (Recomendado) Crie e ative um ambiente virtual:
    python -m venv venv
    venv\Scripts\activate   # No Windows
# ou
    source venv/bin/activate   # No Linux/Mac

3. Instale as dependências:
    python -m pip install streamlit deep-translator

4. Execute o aplicativo:
    streamlit run app.py

O app abrirá automaticamente no navegador (geralmente em http://localhost:8501).

## Como Usar
- Cole um texto técnico de exemplo
- Escolha um idioma
- Clique em traduzir e veja como os termos técnicos foram preservados

## Próximos Passos (se tivesse acesso ao Azure)
- Integrar o SDK oficial azure-ai-translation-text
- Usar o recurso Custom Translator com glossário oficial
- Fazer deploy no Azure App Service ou Azure Static Web Apps

Obrigado pela oportunidade no bootcamp!
Qualquer dúvida, é só chamar.
Raphael
Franca/SP – 2026


