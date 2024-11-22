from conexao import Conexao
from sqlalchemy import text

tabelaJogo = Conexao('jogo')
tabelaDesejos = Conexao('desejos')
tabaelaTudoJogo = Conexao('tudo_jogo')

df_jogos = tabelaJogo.retorna_df()
df_desejos = tabelaDesejos.retorna_df()
df_tudo_jogo = tabaelaTudoJogo.retorna_df()

engine = Conexao('jogo').retorna_engine()


def insert(nome, ano, dev, genero):
    print(nome, ano, dev, genero)   

def insert_desejos(linha):
    
    sql_query = f"""
INSERT INTO catalogo_jogos.lista_desejos VALUES({linha + 1}, CURRENT_DATE);
    """
    with engine.begin() as connection:
        connection.execute(text(sql_query))
    
def update(linha, coluna, novo_valor):
    if coluna == 'ano de lançamento':
        coluna = 'ano_lancamento'
        sql_query = f"""
    UPDATE catalogo_jogos.jogo SET {coluna} = {novo_valor} WHERE id = {linha + 1}; 
    """
    if coluna == 'título':
        coluna = 'titulo'
        sql_query = f"""
    UPDATE catalogo_jogos.jogo SET {coluna} = '{novo_valor}' WHERE id = {linha + 1}; 
    """
    id = df_tudo_jogo.loc[linha, 'titulo']
    with engine.begin() as connection:
        connection.execute(text(sql_query))
        
def delete(linha, tabela):
    if tabela == 'Lista de Desejos':
        nome = df_desejos.loc[linha, 'título']
        sql_query = f"""
    DELETE FROM catalogo_jogos.lista_desejos WHERE id_jogo = (SELECT id FROM catalogo_jogos.jogo WHERE titulo = '{nome}');
    """
        with engine.begin() as connection:
            connection.execute(text (sql_query))
    else :
        tabela = 'jogo'
        sql_query = f"""
    DELETE FROM catalogo_jogos.{tabela} WHERE id = {linha + 1};
    """
    with engine.begin() as connection:
        connection.execute(text (sql_query))