from modelos.avaliacao import Avaliacao
from modelos.cardapio.item_cardapio import ItemCardapio

class Restaurante:
    """Representa um restaurante e suas características."""
    restaurantes = []

    def __init__(self, nome, categoria):
        """
        Inicializa uma instância de Restaurante.
        
        Parâmetros:
        - Nome (str): O nome do restaurante
        - Categoria (str): A categoria do restaurante
        """
        self._nome = nome.title()
        self._categoria = categoria
        self._ativo = False
        self._avaliacao = []
        self._cardapio = []
        Restaurante.restaurantes.append(self) # toda vez que um objeto é criado ele é armazenado dentro dessa lista (restaurante = [])
                                              # ou em outras palavras, adiciona automaticamente a instância atual da classe Restaurante à lista restaurantes
    
    def __str__(self):
        """Retorna uma representação em string do restaurante."""
        return '{} | {}'.format(self._nome, self._categoria)
    
    @classmethod
    def listar_restaurantes(cls):
        """Exibe uma lista formatada de todos os restaurantes."""
        for restaurante in cls.restaurantes:
            print('{} | {} | {} | {}'.format('Nome do Restaurante'.ljust(25), 'Categoria'.ljust(25), 'Avaliação'.ljust(25), 'Ativo'))
            print('{} | {} | {} | {}'.format(restaurante._nome.ljust(25), restaurante._categoria.ljust(25), str(restaurante.media_avaliacao).ljust(25), restaurante.ativo))

    @property
    def ativo(self):
        """Retorna um símbolo indicando o estado de atividade do restaurante."""        
        return '☑' if self._ativo else '☐'
    
    def alternar_estado(self):
        """Alterna o estado de atividade do restaurante."""
        self._ativo = not self._ativo

    def receber_avaliacao(self, cliente, nota):
        """
        Registra uma avaliação para o restaurante.
        
        Parâmetros:
        - Cliente (str): O nome do cliente que fez a avaliação
        - Nota (str): A nota atribuída ao restaurante (entre 1 e 5)"""
        if 0 < nota <= 5:
            avaliacao = Avaliacao(cliente, nota)
            self._avaliacao.append(avaliacao)

    @property
    def media_avaliacao(self):
        """Calcula e retorna a média das avaliações do restaurante"""
        if not self._avaliacao:
            return '-'
        soma_das_notas = sum(avaliacao._nota for avaliacao in self._avaliacao)
        quantidade_de_notas = len(self._avaliacao)
        media = round(soma_das_notas / quantidade_de_notas, 1)
        return media
    
    def adicionar_no_cardapio(self, item):
        """
        Adiciona um item ao cardápio do restaurante, se o item for uma instância de ItemCardapio.

        Parâmetros:
        - item (ItemCardapio): O item a ser adicionado ao cardápio.
        """
        if isinstance(item, ItemCardapio):
            self._cardapio.append(item)

    @property
    def exibir_cardapio(self):
        """
        Exibe o cardápio do restaurante, mostrando os detalhes de cada item, incluindo nome, preço e descrição (para pratos) ou tamanho (para bebidas).
        """
        print('Cardápio do restaurante {}\n'.format(self._nome))
        for i, item in enumerate(self._cardapio, start = 1):
            if hasattr(item, 'descricao'):        
                mensagem_prato = '{}. Nome: {} | Preço: R$ {} | Descrição: {}'.format(i, item._nome, item._preco, item._descricao)
                print(mensagem_prato)
            else:
                mensagem_bebida = '{}. Nome: {} | Preço: R$ {} | Tamanho: {}'.format(i, item._nome, item._preco, item._tamanho)
                print(mensagem_bebida)    
            
    
