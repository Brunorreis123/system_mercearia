from Models import Categoria, Estoque, Pessoa, Produtos, Funcionario, Venda, Fornecedor
from Dao import DaoVenda, DaoCategoria, DaoPessoa, DaoEstoque, DaoFornecedor, DaoFuncionario
from datetime import datetime


class ControllerCategoria:

    def cadastrarCategoria(self, novaCategoria):
        existe = False
        x = DaoCategoria.ler()
        for i in x:
            if i.categoria == novaCategoria:
                existe = True

        if not existe:
            DaoCategoria.salvar(novaCategoria)
            print('Categoria cadastrada com sucesso!')
        else:
            print('A categoria que deseja cadastrar já existe!')

a = ControllerCategoria()
a.cadastrarCategoria('Frios')