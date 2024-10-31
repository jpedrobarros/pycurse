import random

jogadores = [('CR7', 1), ('VINI', 2), ('RODRIGO', 3), ('MESSI?', 4), ('NEYMAR', 5), ('SAVINHO?', 6)]

for nome, numero in jogadores:
    print(f'{nome} - {numero}')

jogadore_randomico1 = random.sample(list(jogadores.keys()), 2)   


for jogador in jogadore_randomico1:
        numero = jogadores[jogador]
        print(f'{jogador} - {numero}')

