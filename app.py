import streamlit as st
from deep_translator import GoogleTranslator
import re

# Glossário técnico - termos que devem ser preservados exatamente
GLOSSARIO = {
    "machine learning": "machine learning",
    "deep learning": "deep learning",
    "neural network": "rede neural",
    "artificial intelligence": "inteligência artificial",
    "Azure AI": "Azure AI",
    "Azure Cognitive Services": "Azure Cognitive Services",
    "Translator": "Translator",
    "Custom Translator": "Custom Translator",
    "API": "API",
    "endpoint": "endpoint",
    "prompt engineering": "prompt engineering",
    "fine-tuning": "fine-tuning",
    "RAG": "RAG",
    "LLM": "LLM",
    "large language model": "large language model",
    # Adicione mais termos se quiser
}

def traduzir_tecnico(texto, idioma_destino="en"):
    if not texto.strip():
        return ""

    # Limpeza simples do texto de entrada
    texto = texto.strip()
    if not texto.endswith(('.', '!', '?')):
        texto += '.'  # ajuda o tradutor a entender melhor o fim da frase

    # Passo 1: Substituição case-insensitive dos termos do glossário
    mapa_restauracao = {}
    contador = 0

    for termo_original in list(GLOSSARIO.keys()):
        termo_protegido = f"__GLOSS_{contador}__"
        
        # Regex para substituição case-insensitive
        pattern = re.compile(re.escape(termo_original), re.IGNORECASE)
        texto = pattern.sub(termo_protegido, texto)
        
        mapa_restauracao[termo_protegido] = GLOSSARIO[termo_original]
        contador += 1

    # Passo 2: Tradução
    try:
        tradutor = GoogleTranslator(source="auto", target=idioma_destino)
        traducao = tradutor.translate(texto)
    except Exception as e:
        return f"Erro durante a tradução: {str(e)}. Tente novamente ou verifique sua conexão."

    # Passo 3: Restauração dos termos
    for protegido, termo_original in mapa_restauracao.items():
        traducao = traducao.replace(protegido, termo_original)

    return traducao

# Configuração da página
st.set_page_config(
    page_title="Tradutor Técnico Azure AI",
    page_icon="🌐",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Título e cabeçalho
st.title("🌐 Tradutor de Artigos Técnicos com Precisão Terminológica")
st.markdown("**Projeto Final – Bootcamp AI-102 | Microsoft Azure (DIO)**")
st.caption("Por Raphael | Alternativa aprovada pela DIO devido a limitações no Azure Free Tier (cartão rejeitado)")

# Layout principal em colunas
col1, col2 = st.columns([3, 3])

with col1:
    st.subheader("Texto Original")
    texto_original = st.text_area(
        "Cole o artigo técnico aqui (Português ou outro idioma):",
        height=400,
        placeholder="Exemplo:\nO machine learning e o deep learning utilizam neural network e prompt engineering para treinar large language model com Azure AI.",
        key="texto_original"
    )

with col2:
    st.subheader("Tradução")
    idioma_selecionado = st.selectbox(
        "Traduzir para:",
        [
            "Inglês (en)",
            "Espanhol (es)",
            "Francês (fr)",
            "Alemão (de)",
            "Italiano (it)"
        ],
        key="idioma"
    )
    codigo_idioma = idioma_selecionado.split("(")[1].strip(")")

    col_btn1, col_btn2 = st.columns([3, 1])
    with col_btn1:
        if st.button("🔄 Traduzir com Glossário Técnico", type="primary", use_container_width=True):
            if texto_original.strip():
                with st.spinner("Traduzindo e preservando termos técnicos..."):
                    resultado = traduzir_tecnico(texto_original, codigo_idioma)
                st.success("Tradução concluída!")
                st.text_area("Resultado:", resultado, height=400, key="resultado")
            else:
                st.warning("Por favor, cole algum texto para traduzir.")

    with col_btn2:
        if st.button("🧹 Limpar", use_container_width=True):
            st.session_state.texto_original = ""
            st.session_state.resultado = ""
            st.rerun()

# Rodapé com explicação
st.divider()
st.info("""
**Como o projeto atende o desafio?**  
- Simula o Azure AI Translator + Custom Translator  
- Glossário customizado garante **precisão terminológica** em domínio técnico (IA, Azure, ML)  
- Interface web prática com Streamlit  
- 100% gratuito e local (sem chave Azure necessária)
""")

st.caption("Desenvolvido para o Bootcamp AI-102 – DIO + Microsoft | Franca/SP – 2026")