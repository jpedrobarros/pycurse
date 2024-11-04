import os
import time
import random

from rich.style import Style
from rich import print
from console import console
from rich.color import Color

from backend import jogadores, linha, linha_vermemelha

# Textos fixos
subtitulo_inicial = ('SEJA BEM VINDO AO FUTURO!')
subtitulo_menu = ('MENU!')
subtitulo_decisao = 'EAE MEU CHAPA! QUER REPETIR OU VOLTAR??? - Sim(s) ou Não(n)??'
erro = 'VOLTA AE PAIZAO, NÃO ENTENDI'
finalizacao = 'ATÉ A PRÓXIMA E MUITO OBRIGADO!!!'
radonman = 'RANDON MODE!!!'

# Função para centralizar texto
def centralizar_texto(texto, largura=55):
    return texto.center(largura)
 
def jogador_randomico(jogadores):
    
    aleatorios = random.sample(jogadores, min(10, len(jogadores)))
    print(linha_vermemelha)
    console.print(f'! --- [🏆] [{centralizar_texto(radonman)}] [🏆] --- !', style='   bold black underline on white')
    print(linha_vermemelha)

    time.sleep(1)

    for jogador in aleatorios:      
        jogador_formatado = centralizar_texto(jogador)
        print(linha)
        print(f'! --- [⚽] [{jogador_formatado}] [⚽] --- !')
        print(linha)
        time.sleep(0.3)
        
    reapet = (obter_decisao(lambda: jogador_randomico(jogadores)))    

 # Função de listar os jogadores de forma padrão
def listar():
        # loop para montar tabelas com os jogadores
        for jogador in jogadores:  
            
            # centralizando texto dentro do espaço
            jogador_formatado = centralizar_texto(jogador)
            print(linha)
            print(f'! --- [⚽] [{jogador_formatado}] [⚽] --- !')
            print(linha)
            time.sleep(0.2)
            
        obter_decisao(lambda: listar(jogadores))    
            
def obter_decisao(reapet):
    continua = True
    
    while continua:     
        console.print(f'! --- [💬] [{centralizar_texto(subtitulo_decisao)}] [💬] --- !', style='blink bold black underline on white')
        
        print(linha_vermemelha)
        decisao_lista = input('! --- [💬]: ')
        print(linha_vermemelha)

        if decisao_lista == 's':
            reapet()
            
        elif decisao_lista != 'n':    
            print(f'! --- [❌] [{centralizar_texto(erro)}] [❌] --- !')
            print(linha)
            
        else:
            continua = False
            console.print(f'! --- [✅] [{centralizar_texto(finalizacao)}] [✅] --- !', style='blink bold black underline on white')
            print(linha_vermemelha)
            print('')

continua = True

while continua:
    
    os.system('clear') 

    console.print(f'! --- [🏆] [{centralizar_texto(subtitulo_inicial)}] [🏆] --- !', style='blink bold black underline on white')
    print(linha_vermemelha)
   
    # Logo
    os.system('figlet -c THE BEST!') 

    # Formatando o cabeçalho do programa
    print(linha_vermemelha)
    console.print(f'! --- [🏆] [{centralizar_texto(subtitulo_menu)}] [🏆] --- !', style='   bold black underline on white')
    print(linha_vermemelha)
    
    # Formatando o Menu
    print(linha_vermemelha)
    console.print('! --- [📟] [    (1) - LISTAR    ]     ❌     [     (2) - RANDON    ] [📄] --- !', style='bold')
    print(linha_vermemelha)
    console.print('! --- [📟] [    (3) - LISTAR    ]     ❌     [     (4) - EDITAR    ] [📄] --- !', style='bold')
    print(linha_vermemelha)
    
    
    decisao = input('! --- [💬] [    (')
    print(linha_vermemelha)

    if decisao == '1':
        listar()
            
    elif decisao == '2':    
        jogador_randomico()
                    
    else:
        continua = False
        console.print(f'! --- [✅] [{centralizar_texto(finalizacao)}] [✅] --- !', style='bold black underline on white')
        print(linha_vermemelha)
        print('')