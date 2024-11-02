import os
import time
from rich.style import Style
from rich import print
from console import console
from rich.color import Color
from rich.style import Style
from rich import print
from backend import jogadores, linha, linha_vermemelha

base_style = Style.parse("cyan")

# textos fixos
subtitulo_inicial = ('DIGITE UM NOVO JOGADOR PARA A LISTA')
subtitulo_decisao = 'EAE MEU CHAPA! QUER CONTINUAR POR AQUI - Sim(s) ou Não(n)??'
erro = 'VOLTA AE PAIZAO, NÃO ENTENDI'
finalizacao = 'ATÉ A PRÓXIMA E MUITO OBRIGADO!!!'

# Função para centralizar texto
def centralizar_texto(texto, largura=59):
    return texto.center(largura)

continua = True

while continua:

    os.system('cls' if os.name == 'nt' else 'clear')  
    print(linha_vermemelha)
    
    console.print(f'! --- [🏆] [{centralizar_texto(subtitulo_inicial)}] [🏆] --- !', style='bold black underline on blue')
    print(linha_vermemelha)
    
    os.system('figlet -c THE BEST!') 

    # formatando o subtitulo inicial que será a base superior do loop
    print(linha_vermemelha)
    console.print(f'! --- [🏆] [{centralizar_texto(subtitulo_inicial)}] [🏆] --- !', style='bold black underline on blue')
    print(linha_vermemelha)
    
       
    # loop para montar tabelas com os jogadores
    for jogador in jogadores:  
        
        # centralizando texto dentro do espaço
        jogador_formatado = centralizar_texto(jogador)
        print(linha)
        print(f'! --- [⚽] [{jogador_formatado}] [⚽] --- !')
        print(linha)
        time.sleep(0.5)
        
    console.print(f'! --- [💬] [{centralizar_texto(subtitulo_decisao)}] [💬] --- !', style='blink bold black underline on white')
    
    print(linha_vermemelha)
    decisao = input('! --- [💬]: ')
    print(linha_vermemelha)


    if decisao == 's':
        os.system('cls' if os.name == 'nt' else 'clear')
        
    elif decisao != 'n':    
        print(f'! --- [❌] [{centralizar_texto(erro)}] [❌] --- !')
        print(linha)
        
    else:
        continua = False
        console.print(f'! --- [✅] [{centralizar_texto(finalizacao)}] [✅] --- !', style='blink bold black underline on white')
        print(linha_vermemelha)
        print('')





