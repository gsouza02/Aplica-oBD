from sqlalchemy import create_engine
import pandas as pd


class Conexao:

    def __init__(self, tipo):
        self.tabela = tipo
        db_url = 'mysql+pymysql://root:root@localhost:3306' # porta e nome padrão do MySQL, se necessário mudar aqui
        try:
            self.engine = create_engine(db_url)



        except:
            print('Erro ao conectar ao banco de dados')

        
    def retorna_df(self):
        if self.tabela == 'jogo':
            sql_query = """
            SELECT j.titulo AS título, j.ano_lancamento AS 'ano de lançamento', d.nome AS desenvolvedor, g.nome AS genêro
            FROM catalogo_jogos.jogo AS j
            LEFT JOIN catalogo_jogos.desenvolvedor AS d 
            ON j.id_desenvolvedor = d.id
            LEFT JOIN catalogo_jogos.genero AS g
            ON j.id_genero = g.id
            """
        elif self.tabela == 'desejos':
            sql_query = """
            SELECT j.titulo AS título, j.ano_lancamento AS 'ano de lançamento', d.nome AS desenvolvedor, g.nome AS genêro, ld.data_adicao AS 'data de adição'
            FROM catalogo_jogos.jogo AS j
            LEFT JOIN catalogo_jogos.desenvolvedor AS d 
            ON j.id_desenvolvedor = d.id
            LEFT JOIN catalogo_jogos.genero AS g
            ON j.id_genero = g.id
            INNER JOIN catalogo_jogos.lista_desejos AS ld
            on ld.id_jogo = j.id
            """
        elif self.tabela == 'tudo_jogo':
            sql_query = """
            SELECT * FROM catalogo_jogos.jogo
            """
        df = pd.read_sql(sql_query, self.engine)
        return df


    def retorna_engine(self):
        return self.engine