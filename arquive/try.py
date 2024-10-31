import random

def obter_resposta(pergunta):
    """Obtém a resposta do usuário e valida a entrada."""
    while True:
        try:
            resposta = int(input(f'{pergunta} ESCOLHA O JOGADOR E DIGITE O NÚMERO: '))
            if resposta in (id_jogador_1, id_jogador_2):
                return resposta
            else:
                print('Resposta inválida. Digite 1 para CR7 ou 2 para Neymar.')
        except ValueError:
            print('Entrada inválida. Digite 1 para CR7 ou 2 para Neymar.')

def determinar_vencedor(pontos_jogador_1, pontos_jogador_2):
    """Determina e imprime o vencedor com base nos pontos."""
    if pontos_jogador_1 > pontos_jogador_2:
        print('SIIIIU! CR7 é o BRABO!')
    elif pontos_jogador_2 > pontos_jogador_1:
        print('PARAAADO NO BAILÃO - Aqui é aduto NEY poha!')
    else:
        print('O dois é a mema fita')

# Inicializa os IDs dos jogadores
id_jogador_1 = 1
id_jogador_2 = 2

# Inicializa os pontos dos jogadores
pontos_jogador_1 = 0
pontos_jogador_2 = 0

# Define o valor de cada ponto
ponto = 1

# Cria uma lista com as perguntas
perguntas: list = ['Drible?', 'Velocidade?', 'Chute?']

print('CR7 OU NEY?')
print('CR7 (1) ')
print('NEY (2) ')

# Embaralha as perguntas para aleatoriedade
random.shuffle(perguntas)

for pergunta in perguntas:
    resposta = obter_resposta(pergunta)
    if resposta == id_jogador_1:
        pontos_jogador_1 += ponto
    else:
        pontos_jogador_2 += ponto

determinar_vencedor(pontos_jogador_1, pontos_jogador_2)