# Importando o módulo
from random import random

def joga_dado():
    # Laço
    while True:
        # Adicionando o valor pseudo-randômico na variável
        dado = int(random()*10)

        # Se o valor de dado for menor que 7 e não for igual a zero eu saio do loop
        if dado < 7 and dado != 0:
            break

    # Retorno o valor de "dado"
    return dado

# Função que valida a vitória ou derrota
def resultado(jogusus, resdado):
    # Ganhou
    if jogusus == resdado:
        print(f'Você ganhou! \nJogou: {jogusus}\nDado: {resdado}\n\n')
    
    # Perdeu
    else:
        print(f'Você Perdeu! \nJogou: {jogusus}\nDado: {resdado}\n\n')
    

#imprimindo na tela
while True:
    # O usuário digita um valor de 0 a 6
    jogada = int(input('Qual o valor que vai cair do dado? '))

    # Variável recebe a jogada do dado chamando a função joga_dado
    j_dado = joga_dado()

    # Chamo a função que valida a vitória depois de escolher minha jogada e lançar o dado
    resultado(jogada, j_dado)




