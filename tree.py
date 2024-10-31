import random

def obter_resposta(pergunta):
    
    while True:
        try: 
            resposta = int(input(f'{pergunta} ESCOLHA O JOGADOR E DIGITE O NÚMERO: '))
            if resposta in (idJogador1, idJogador2):
                return resposta  
            else:
                print('Resposta errada irmão')   
                         
        except ValueError:
            print('COLOCO O NÚMERO CERTO POHA')

def define_campeao(pontos_jogador_1, pontos_jogador_2):
    
    if  pontos_jogador_1 > pontos_jogador_2 :
        print('SIIIIU! CR7 é o BRABO!')

    elif pontos_jogador_2 == pontos_jogador_1:
        print('O dois é a mema fita')

    elif pontos_jogador_2 > pontos_jogador_1:
        print('PARAAADO NO BAILÃO - Aqui é aduto NEY poha!')
    else:
        print('ERRO 404')

def random_mode(jogadores):
    jogadores_aleatorios = random.sample(jogadores, 2)
    for jogador in jogadores_aleatorios:
        numero = jogadores[jogador]
        print(f'JOGADOR: {jogador} - {numero}')
    
random_mode(jogadores)              

pontos_jogador_1 = 0 
pontos_jogador_2 = 0
ponto = 1
idJogador1 = 1
idJogador2 = 2

perguntas : list = ['Drilhe?', 'Velocidade?', 'Chute?', 'Elasticidade?', 'Força?', 'Malandragem?']

jogadores = [('CR7', 1), ('VINI', 2), ('RODRIGO', 3), ('MESSI?', 4), ('NEYMAR', 5), ('SAVINHO?', 6)]


print("|--------------------------------------------------------|")
print("[🎩]                    FUTCOMPARE                    [🎩]")
print("|--------------------------------------------------------|")
print("[⏬]                  DIGITE YES                      [⏬]")
print("|--------------------------------------------------------|")   

while continuar:
    os.system('cls' if os.name == 'nt' else 'clear')

    random_mode(jogadores)
    
    resposta = input("Deseja selecionar jogadores novamente? (s/n): ")
    if resposta.lower() != 's':
        continuar = False
        
    for pergunta in perguntas:
        resposta = obter_resposta(pergunta)
        if resposta == idJogador1:
            pontos_jogador_1 += ponto
        else:
            pontos_jogador_2 += ponto        

define_campeao(pontos_jogador_1, pontos_jogador_2)
continuar = True
