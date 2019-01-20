import sqlite3


class BancoDeDados:
    """Classe que representa o banco de dados da aplicação"""
    def __init__(self, nome='bancodb'):
        self.nome, self.conexao = nome, None

    def conecta(self):
        """Conecta ao arquivo do banco de dados nome.sqlite3"""
        self.conexao = sqlite3.connect(self.nome)

    def desconecta(self):
        """Encerra a conexão com o banco sqlite3"""
        try:
            self.conexao.close()
        except AttributeError:
            pass

    def criar_tabelas(self):
        """Cria as tabelas do banco"""
        """Ordem dos dados: 'Nome do fornecedor, Descrição da compra, Valor, data, numero parcelas"""
        try:
            cursor = self.conexao.cursor()
            cursor.execute("""
            CREATE TABLE IF NOT EXISTS Compras (
            id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
            nome_fornecedor VARCHAR(50) NOT NULL,
            descricao_compra TEXT NOT NULL,
            valor_compra DECIMAL(8, 2) NOT NULL,
            data_compra DATE NOT NULL,
            n_parcelas_compra INTEGER NOT NULL);
            """)

            cursor.execute("""
                        CREATE TABLE IF NOT EXISTS Vendas (
                        id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                        nome_cliente VARCHAR(50) NOT NULL,
                        descricao_venda TEXT NOT NULL,
                        valor_venda DECIMAL(8, 2) NOT NULL,
                        data_venda DATE NOT NULL,
                        n_parcelas_venda INTEGER NOT NULL);
                        """)
        except AttributeError:
            print('banco de dados não conectado')

    def inserir_compra(self, nome_fornecedor, descricao_compra, valor_compra, data_compra, n_parcelas_compra):
        """Insere linhas com as novas compras na tabela"""
        try:
            cursor = self.conexao.cursor()
            cursor.execute(f"""
            INSERT INTO Compras (nome_fornecedor, descricao_compra, valor_compra, data_compra, n_parcelas_compra)
            VALUES (?,?,?,?,?)""", (nome_fornecedor, descricao_compra, valor_compra, data_compra, n_parcelas_compra))
            self.conexao.commit()
        except AttributeError:
            print('Não foi possivel adicionar a compra.')

    def inserir_venda(self, nome_cliente, descricao_venda, valor_venda, data_venda, n_parcelas_venda):
        """Insere linhas com as novas compras na tabela"""
        try:
            cursor = self.conexao.cursor()
            cursor.execute(f"""
            INSERT INTO Vendas (nome_cliente, descricao_venda, valor_venda, data_venda, n_parcelas_venda)
            VALUES (?,?,?,?,?)""", (nome_cliente, descricao_venda, valor_venda, data_venda, n_parcelas_venda))
            self.conexao.commit()
        except AttributeError:
            print('Não foi possivel adicionar a compra.')

    def buscar_compras(self):
        cursor = self.conexao.cursor()
        compras = cursor.execute('SELECT nome_fornecedor, descricao_compra, valor_compra, data_compra, '
                                 'n_parcelas_compra FROM Compras WHERE id >= 0;').fetchall()
        return compras

    def buscar_vendas(self):
        cursor = self.conexao.cursor()
        vendas = cursor.execute('SELECT nome_cliente, descricao_venda, valor_venda, data_venda, n_parcelas_venda '
                                'FROM Vendas WHERE id >= 0;').fetchall()
        return vendas


if __name__ == '__main__':
    banco = BancoDeDados('BancoTeste')
    banco.conecta()

    print(banco.buscar_compras())

    banco.desconecta()
