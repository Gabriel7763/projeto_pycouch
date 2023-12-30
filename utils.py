import socket
import couchdb


def conectar():
    """
    Função para conectar ao servidor
    """
    user = 'admin'
    password = 'admin'
    connection = couchdb.Server(f'http://{user}:{password}@localhost:5984')

    banco = 'pycouch'

    #se existir este banco na conexão, busque ele no banco e retorne
    if banco in connection:
        db = connection[banco]
        return db
    else:
        try:
            db = connection.create(banco)
            return db
        except socket.gaierror as e:
            print(f'Erro ao conectar ao servidor: {e}')
        except couchdb.http.Unauthorized as f:
            print(f'Você não tem permissão de acessor: {f}')
        except ConnectionRefusedError as g:
            print(f'Não foi possível conectar ao servidor: {g}')

def desconectar():
    """ 
    Função para desconectar do servidor.
    """
    print('Desconectando do servidor...')


def listar():
    """
    Função para listar os produtos
    """
    db = conectar()

    if db:
        if db.info()['doc_count'] > 0:
            print('Listando produtos...')
            print('--------------------')
            #para cada documento no banco de dados
            for doc in db:
                print(f"ID: {db[doc]['_id']}")
                print(f"Rev: {db[doc]['_rev']}")
                print(f"Produto: {db[doc]['nome']}")
                print(f"Preço: {db[doc]['preco']}")
                print(f"Estoque: {db[doc]['estoque']}")
                print('---------------------')
        else:
            print('Não existem produtos cadastrados')
    else:
        print('Não foi possível conectar com o sevidor')

def inserir():
    """
    Função para inserir um produto
    """  
    print('Inserindo produto...')

def atualizar():
    """
    Função para atualizar um produto
    """
    print('Atualizando produto...')

def deletar():
    """
    Função para deletar um produto
    """  
    print('Deletando produto...')

def menu():
    """
    Função para gerar o menu inicial
    """
    print('=========Gerenciamento de Produtos==============')
    print('Selecione uma opção: ')
    print('1 - Listar produtos.')
    print('2 - Inserir produtos.')
    print('3 - Atualizar produto.')
    print('4 - Deletar produto.')
    opcao = int(input())
    if opcao in [1, 2, 3, 4]:
        if opcao == 1:
            listar()
        elif opcao == 2:
            inserir()
        elif opcao == 3:
            atualizar()
        elif opcao == 4:
            deletar()
        else:
            print('Opção inválida')
    else:
        print('Opção inválida')
