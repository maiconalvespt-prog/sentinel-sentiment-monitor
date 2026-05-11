# Interface visual (usando o Streamlit)

import streamlit as st
import pandas as pd
from processor.scraper import NewsFetcher
from processor.analyzer import SentimentAnalyzer
from utils.helpers import clean_text, truncate_text

# 1. Configuração da Página
st.set_page_config(
    page_title="Sentinel Monitor",
    page_icon="🛡️",
    layout="wide"
)

# Estilização customizada para parecer um Dashboard Executivo
st.markdown("""
    <style>
    .main { background-color: #f5f7f9; }
    .stMetric { background-color: #ffffff; padding: 15px; border-radius: 10px; box-shadow: 0 2px 4px rgba(0,0,0,0.05); }
    </style>
    """, unsafe_allow_html=True)

# 2. Inicialização dos Objetos (Singletons de facto)
fetcher_tool = None
analyzer_tool = SentimentAnalyzer()

# 3. Interface Lateral (Sidebar)
with st.sidebar:
    st.image("https://cdn-icons-png.flaticon.com/512/2092/2092663.png", width=80)
    st.title("Sentinel Core")
    st.info("Monitoramento de reputação via NLP")
    
    tema = st.text_input("Tema para monitorar:", placeholder="Ex: Nvidia, Bitcoin, Governo...")
    qtd_noticias = st.slider("Volume de dados:", 5, 30, 10)
    
    executar = st.button("🚀 Iniciar Varredura", use_container_width=True)

# 4. Lógica Principal
st.title("🛡️ Painel de Análise de Sentimento")

if executar and tema:
    with st.spinner(f"Varrendo notícias sobre '{tema}'..."):
        # Coleta
        fetcher_tool = NewsFetcher(tema)
        dados_brutos = fetcher_tool.collect_news(limit=qtd_noticias)
        
        if not dados_brutos:
            st.error("Nenhum dado encontrado para este tema.")
        else:
            resultados = []
            
            # Processamento
            for noticia in dados_brutos:
                titulo_limpo = clean_text(noticia['title'])
                analise = analyzer_tool.analyze(titulo_limpo)
                
                resultados.append({
                    "Fonte": noticia['source'],
                    "Título": truncate_text(titulo_limpo, 80),
                    "Sentimento": analise['label'],
                    "Score": analise['score'],
                    "Link": noticia['link']
                })
            
            df = pd.DataFrame(resultados)

            # 5. Visualização de Métricas
            col1, col2, col3 = st.columns(3)
            with col1:
                st.metric("Total Analisado", len(df))
            with col2:
                pos_pct = len(df[df['Sentimento'] == 'Positivo'])
                st.metric("Menções Positivas", f"{pos_pct}")
            with col3:
                score_medio = df['Score'].mean()
                st.metric("Índice de Humor", f"{score_medio:.2f}")

            st.divider()

            # 6. Exibição dos Cards
            st.subheader("Últimas Menções Identificadas")
            
            for index, row in df.iterrows():
                with st.expander(f"{row['Sentimento']} | {row['Título']}"):
                    st.write(f"**Fonte:** {row['Fonte']}")
                    st.write(f"**Score de Polaridade:** {row['Score']}")
                    st.markdown(f"[Acessar fonte original]({row['Link']})")

elif not tema and executar:
    st.warning("Por favor, digite um tema na barra lateral.")
else:
    st.info("Aguardando comando... Defina um tema na lateral e clique em 'Iniciar Varredura'.")