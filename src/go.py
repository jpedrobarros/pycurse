import random
import os


def obter_resposta(pergunta, idJogada1, idJogada2):
    """Obtém a resposta do usuário e valida a entrada."""
    while True:
        try:
            print("|------------------------------------------|")
            resposta = int(input(f'QUEM É MELHOR EM:   {pergunta}??'))
            if resposta in (idJogada1, idJogada2):
                return resposta
            else:
                print('Resposta inválida. Digite 1 ou 2.')
        except ValueError:
            print('Entrada inválida. Digite um número.')

def define_campeao(pontos_jogador_1, pontos_jogador_2):
    """Determina e imprime o vencedor com base nos pontos."""
    if pontos_jogador_1 > pontos_jogador_2:
        print("Jogador 1 é o campeão!")
    elif pontos_jogador_2 > pontos_jogador_1:
        print("Jogador 2 é o campeão!")
    else:
        print("Empate!")

def random_mode(jogadores):
    """Seleciona e imprime dois jogadores aleatórios."""
    if not jogadores:
        print("Erro: Nenhum jogador disponível.")
        return
    jogadores_list = list(jogadores.keys())
    jogadores_aleatorios = random.sample(jogadores_list, 2)
    for jogador in jogadores_aleatorios:
        numero = jogadores[jogador] 
        print(f"[🔥]{jogador} - {numero}[🔥]")
        
def jogar(jogadores, perguntas, idJogada1, idJogada2, ponto):
    """Executa uma rodada do jogo."""
    pontos_jogador_1 = 0
    pontos_jogador_2 = 0
    random_mode(jogadores)

    for pergunta in perguntas:
        resposta = obter_resposta(pergunta, idJogada1, idJogada2)
        if resposta == idJogada1:
            pontos_jogador_1 += ponto
        else:
            pontos_jogador_2 += ponto

    define_campeao(pontos_jogador_1, pontos_jogador_2)

# Variáveis
idJogada1 = 1
idJogada2 = 2
ponto = 1
perguntas: list = ['Drilhe?', 'Velocidade?', 'Chute?', 'Elasticidade?', 'Força?', 'Malandragem?']
jogadores = {'CR7': 1, 'VINI': 2, 'RODRIGO': 3, 'MESSI?': 4, 'NEYMAR': 5, 'SAVINHO?': 6}

# Cabeçalho do jogo
os.system('cls' if os.name == 'nt' else 'clear')
print("|-------------------------------------------------------|")
print("[🎩]                    FUTCOMPARE                   [🎩]")
print("|-------------------------------------------------------|")
print("[🔥]                 MODO ALEATÓRIO                  [🔥]")
print("|-------------------------------------------------------|")   

continuar = True

while continuar:
    jogar(jogadores, perguntas, idJogada1, idJogada2, ponto)
    resposta = input("Jogar novamente? (s/n): ")
    if resposta.lower() != 's':
        continuar = False