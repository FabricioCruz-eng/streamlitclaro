import streamlit as st
import pandas as pd

st.set_page_config(page_title="Pesquisa de Rotas", layout="wide")
st.markdown("""
    <h1 style="font-size: 24px; color: #BCCBD8;">🛣️ Trecho Claro Cedente</h1>
""", unsafe_allow_html=True)

# Upload do arquivo
dados = None
arquivo = st.sidebar.file_uploader("Carregue o arquivo de dados (.xlsx, .xls, .csv)", type=["xlsx", "xls", "csv"])

if arquivo:
    if arquivo.name.endswith(".csv"):
        dados = pd.read_csv(arquivo, sep=None, engine='python')
    else:
        dados = pd.read_excel(arquivo)

    # Normalizar nomes das colunas (remover espaços extras)
    dados.columns = [col.strip() for col in dados.columns]

    # Filtros na sidebar
    operadoras = sorted(dados["Operadora"].dropna().unique())
    uf1s = sorted(dados["UF1"].dropna().unique())
    uf2s = sorted(dados["UF2"].dropna().unique())

    operadora_sel = st.sidebar.multiselect("Operadora", operadoras)
    uf1_sel = st.sidebar.multiselect("UF1", uf1s)
    uf2_sel = st.sidebar.multiselect("UF2", uf2s)

    # Aplicar filtros
    df_filtrado = dados.copy()
    if operadora_sel:
        df_filtrado = df_filtrado[df_filtrado["Operadora"].isin(operadora_sel)]
    if uf1_sel:
        df_filtrado = df_filtrado[df_filtrado["UF1"].isin(uf1_sel)]
    if uf2_sel:
        df_filtrado = df_filtrado[df_filtrado["UF2"].isin(uf2_sel)]

    st.dataframe(df_filtrado, use_container_width=True)
else:
    st.info("Por favor, carregue um arquivo de dados para começar.")

st.markdown("""---""")
st.markdown("""
        

Ferramenta desenvolvida e mantida por fabricio.cruz@claro.com.br
            
### Dados Utilizados
Os arquivos utilizados na análise estão disponíveis em:
1. 🗃️ Repositório de Dados do Portal Roma 
2. 🔓 Trechos Cedidos""")

# Adicionando rodapé com informações de direitos autorais
st.markdown("---")
st.markdown(
    """
    <div style="text-align: center; color: white; background-color: #262730; padding: 10px;">
        Copyright © 2025 Todos os direitos reservados - Claro Brasil
    </div>
    """, 
    unsafe_allow_html=True
) 
