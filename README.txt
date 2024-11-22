Para rodar o código é necessário instalar as bibliotecas abaixo listadas.

na linha 9 do conexao.py, pode ser necessário alterar a url de conexão com o banco de dados, dependendo de onde o servidor estiver localizado.

É recomendado, também, a utilização de ambiente local para instalar as bibliotecas, porém o global também irá funcionar.


python -m venv venv. Para criar o ambiente.
venv\Scripts\activate. Para ativar o ambiente.

Se tiver feito os passos anteriores ou não o primeiro passo para rodar o programa é executar o comando a baixo.

pip install pandas sqlalchemy pymysql streamlit

Após criar os dados do arquivo scripts.sql. Basta executar o comando

streamlit run front.py