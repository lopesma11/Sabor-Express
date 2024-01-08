# Sabor Express

O **Sabor Express** é um projeto de restaurante totalmente desenvolvido em Python. Este projeto permite a criação e gerenciamento de restaurantes, avaliações, cardápios e integração com uma API externa para obter dados de restaurantes.

## Estrutura de Diretórios

- **Modelos**: Contém as classes principais do projeto.
  - **Restaurante.py**: Define a classe `Restaurante` para representar um restaurante.
  - **avaliacao.py**: Define a classe `Avaliacao` para representar avaliações de restaurantes.

- **Modelos/Cardapio**: Subpasta que contém as classes relacionadas ao cardápio.
  - **bebida.py**: Define a classe `Bebida` para representar itens de bebidas no cardápio.
  - **prato.py**: Define a classe `Prato` para representar itens de pratos no cardápio.
  - **itemcardapio.py**: Define a classe abstrata `ItemCardapio` como base para itens no cardápio.

- **Scripts**: Contém scripts úteis para o projeto.
  - **app.py**: Script para interação com uma API externa e armazenamento dos dados em arquivos JSON.
  - **main.py**: Script principal para criar instâncias de restaurante, itens de cardápio e exibir o cardápio.

- **venv/Scripts**: Ambiente virtual Python.

- **app.py**: Outro script que utiliza as classes do modelo para criar instâncias de restaurante, bebida, e prato, aplicar descontos e exibir o cardápio.

- **requirements.txt**: Lista de dependências Python necessárias para o projeto.

## Como Executar

1. Clone este repositório.
2. Instale as dependências usando `pip install -r requirements.txt`.
3. Execute o script principal `main.py` para criar instâncias de restaurante, bebida e prato, aplicar descontos e exibir o cardápio.

## Funcionalidades Principais

- **Restaurante**: A classe principal que representa um restaurante com funcionalidades como ativar/desativar, receber avaliações e gerenciar o cardápio.

- **Avaliacao**: Classe para representar as avaliações de clientes sobre os restaurantes.

- **Cardápio**: Classes `Bebida` e `Prato` herdam da classe abstrata `ItemCardapio`. O cardápio pode ser exibido com detalhes de cada item.

- **API Integration (app.py)**: Demonstração de como integrar o projeto com uma API externa para obter dados de restaurantes.

## Contribuições

Contribuições são bem-vindas! Sinta-se à vontade para fazer melhorias, corrigir bugs ou adicionar novas funcionalidades. Abra uma issue para discussão antes de enviar um pull request.
