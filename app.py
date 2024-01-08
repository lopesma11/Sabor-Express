from modelos.restaurante import Restaurante
from modelos.cardapio.bebida import Bebida
from modelos.cardapio.prato import Prato

restaurante_pizza = Restaurante('Pizza Hut', 'Italiana')
bebida_suco = Bebida('Suco de Melancia', 5.00, 'Grande')
bebida_suco.aplicar_desconto()
prato_paozinho = Prato('Paozinho', 2.00, 'O melhor pão da cidade')
prato_paozinho.aplicar_desconto()
restaurante_pizza.adicionar_no_cardapio(bebida_suco)
restaurante_pizza.adicionar_no_cardapio(prato_paozinho)

def main():
    restaurante_pizza.exibir_cardapio

if __name__ == '__main__':
    main()