import os
import textwrap
from rich.console import Console

console = Console(record=True)
blue_console = Console(style="white on blue")

jogadores = ['Neymar', 'Ganso', 'Pele']

linha = '! ---------------------------------------------------------------- !'


continuar = True

os.system('clear')    
os.system('figlet THE BEST LIST')    


console.rule('[bold red]Chapter 2', 'max_width: int = 80')
    
while continuar:  
    
    for jogador in jogadores: 
        jogador_lista = jogador.center(42)
        print('! ---------------------------------------------------------- !')
        print('! --- [😝] ESCOLHA UM NOVO JOGADOR PRA NOSSA LISTA  [😝] --- !')
        print('! ---------------------------------------------------------- !')
        print(f'! --- [⚽] LISTA: {jogadores                       }[😝] --- !')
        print('! ---------------------------------------------------------- !')
        print('! --- [⚽] NOVO JOGADOR OU APENAS (n) PARA SAIR     [⚽] --- !')
        print('!------------------------------------------------------------!')
        
        novo_jogador = input('Digite um novo Jogador ou (n) para sair:  ')
        
        if novo_jogador != jogadores and novo_jogador not in jogadores:
            jogadores.append(novo_jogador)
        
        elif novo_jogador in (jogadores):
            print('ESSE JOGADOR JÁ PERTENCE A LISTA !!!')
            
        else:
            print('TMJ PAIZAO, MEMA FITA!')   
            continuar = False
            
        