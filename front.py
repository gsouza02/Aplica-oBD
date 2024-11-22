import streamlit as st
from conexao import Conexao
import scripts_sql as sql

jogo = Conexao('jogo')
desejos = Conexao('desejos')
tudo_jogo = Conexao('tudo_jogo')
# Função para a página 1
def pagina_1():
    # Conexões com os bancos de dados

    # Recuperando os DataFrames
    dfJogo = jogo.retorna_df()
    dfDesejos = desejos.retorna_df()
    dfTudoJogo = tudo_jogo.retorna_df()

    # Caixa para selecionar qual DataFrame exibir
    escolha = st.selectbox("Escolha a lista para exibir:", ['Jogos', 'Lista de Desejos'])

    # Mostrar o DataFrame selecionado
    if escolha == 'Jogos':
        st.dataframe(dfJogo, use_container_width=True)
    elif escolha == 'Lista de Desejos':
        if dfDesejos.empty:
            st.write("A lista de desejos está vazia. Adicione algum jogo.")
        else:
            st.dataframe(dfDesejos, use_container_width=True)

# Função para a página 2
def pagina_2():
    dfJogo = jogo.retorna_df()
    dfDesejos = desejos.retorna_df()
    dfTudoJogo = tudo_jogo.retorna_df()
    escolha = st.selectbox("Escolha em qual lista vai adicionar:", ['Jogos', 'Lista de Desejos'])
    st.dataframe(dfJogo, use_container_width=True)                    
    if escolha == 'Lista de Desejos':
        if dfDesejos.empty:
            st.write("A lista de jogos está vazia. Adicione um jogo.")
        else:
            st.write("Lista de desejos:")
            st.dataframe(dfDesejos, use_container_width=True)
        index_para_alterar = st.number_input("Digite o índice da linha do jogo que quer adicionar à lista de desejos:", min_value=0, max_value=len(dfJogo)-1, step=1)
        if st.button("Adicionar"):
            sql.insert_desejos(index_para_alterar)
            st.success("O jogo foi adicionado à lista de desejos.")
    else:
        titulo = st.text_input(f"Digite o título do jogo")
        ano = st.number_input(f"Digite o ano de lançamento do jogo", min_value=1950, max_value=2025, step=1)
        dev = st.text_input(f"Digite o nome do desenvolvedor do jogo")
        genero = st.text_input(f"Digite o gênero do jogo")
        if st.button("Adicionar"):
            sql.insert(titulo, ano, dev, genero)
            st.success("O jogo foi adicionado à lista.")
        

# Função para a página 3
def pagina_3():
    dfJogo = jogo.retorna_df()
    st.dataframe(dfJogo, use_container_width=True)
    escolha = st.selectbox("Escolha qual item será editado:", ['título', 'ano de lançamento'])
    index_para_alterar = st.number_input("Digite o índice da linha que deseja alterar:", min_value=0, max_value=len(dfJogo)-1, step=1)
    if escolha != 'ano de lançamento':
        novo_valor = st.text_input(f"Digite o novo valor para a linha")
    else:
        novo_valor = st.number_input(f"Digite o novo valor para a linha", min_value=1900, max_value=2025, step=1)
    if st.button("Editar"):
        sql.update(index_para_alterar, escolha, novo_valor)
        st.success("O jogo foi editado com sucesso.")
    
def pagina_4():
    dfJogo = jogo.retorna_df()
    dfDesejos = desejos.retorna_df()
    dfTudoJogo = tudo_jogo.retorna_df()

    # Caixa para selecionar qual DataFrame exibir
    escolha = st.selectbox("Escolha a lista para exibir:", ['Jogos', 'Lista de Desejos'])

    # Mostrar o DataFrame selecionado
    if escolha == 'Jogos':
        st.dataframe(dfJogo, use_container_width=True)
        index_para_alterar = st.number_input("Digite o índice do jogo que deseja deletar:", min_value=0, max_value=len(dfJogo)-1, step=1)
        if st.button("Deletar"):
            sql.delete(index_para_alterar, escolha)
            st.success("O jogo foi deletado com sucesso.")
    elif escolha == 'Lista de Desejos':
        if dfDesejos.empty:
            st.write("A lista de desejos está vazia. Adicione algum jogo.")
        else:
            st.dataframe(dfDesejos, use_container_width=True)
            index_para_alterar = st.number_input("Digite o índice do jogo que deseja deletar:", min_value=0, max_value=len(dfJogo)-1, step=1)
            if st.button("Deletar"):
                sql.delete(index_para_alterar, escolha)
                st.success("O jogo foi deletado com sucesso.")

# Usando radio na barra lateral para navegação
pagina = st.sidebar.radio('Escolha uma página:', ['Home', 'Adicionar', 'Editar', 'Deletar'])

# Carregar a página correspondente
if pagina == 'Home':
    pagina_1()
elif pagina == 'Adicionar':
    pagina_2()
elif pagina == 'Editar':
    pagina_3()
elif pagina == 'Deletar':
    pagina_4()
