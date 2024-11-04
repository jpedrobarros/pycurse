import os
import time
import random

from rich.style import Style
from rich import print
from console import console
from rich.color import Color

from shared import jogadores, linha, linha_vermemelha

# Textos fixos
subtitulo_inicial = ('SEJA BEM VINDO AO FUTURO!')
subtitulo_menu = ('MENU!')
subtitulo_decisao = 'EAE MEU CHAPA! REPETIR OU VOLTAR? - Sim(s) ou Não(n)??'
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

    time.sleep(0.8)

    for jogador in aleatorios:
        jogador_formatado = centralizar_texto(jogador)
        print(linha)
        print(f'! --- [⚽] [{jogador_formatado}] [⚽] --- !')
        print(linha)
        time.sleep(0.2)
        
    obter_decisao(lambda: jogador_randomico(jogadores))

# Função de listar os jogadores de forma padrão
def listar(jogadores):
    # loop para montar tabelas com os jogadores
    title()
    time.sleep(0.8)

    for jogador in jogadores:
        # centralizando texto dentro do espaço
        jogador_formatado = centralizar_texto(jogador)
        print(linha)
        print(f'! --- [⚽] [{jogador_formatado}] [⚽] --- !')
        print(linha)
        time.sleep(0.1)
        
    obter_decisao(lambda: listar(jogadores))

def obter_decisao(reapet):
    continua = True
    
    while continua:
        console.print(f'! --- [🏆] [{centralizar_texto(subtitulo_decisao)}] [🏆] --- !', style='   bold black underline on white')
        
        print(linha_vermemelha)
        decisao_lista = input('! --- [💬]: ')
        print(linha_vermemelha)

        if decisao_lista == 's':
            os.system('clear')
            title()
            reapet()
            
        elif decisao_lista == 'n':
            main()
            
        else:
            continua = False
            console.print(f'! --- [✅] [{centralizar_texto(finalizacao)}] [✅] --- !', style='blink bold black underline on white')
            print(linha_vermemelha)
            print('')

def title():
    os.system('clear')

    console.print(f'! --- [🏆] [{centralizar_texto(subtitulo_inicial)}] [🏆] --- !', style='blink bold black underline on white')
    print(linha_vermemelha)
   
    # Logo
    os.system('figlet -c THE BEST!')

    # Formatando o cabeçalho do programa
    print(linha_vermemelha)
    console.print(f'! --- [🏆] [{centralizar_texto(subtitulo_menu)}] [🏆] --- !', style='   bold black underline on white')
    print(linha_vermemelha)
    
    
def main():
    continua = True

    
    while continua:
        title()
        # Formatando o Menu
        print(linha_vermemelha)
        console.print('! --- [📟] [    (1) - LISTAR    ]     ❌     [     (2) - RANDON    ] [📄] --- !', style='bold')
        print(linha_vermemelha)
        console.print('! --- [📟] [    (3) - SAIR      ]     ❌     [     (4) - XX         ] [📄] --- !', style='bold')
        print(linha_vermemelha)
        
        decisao = input('! --- [💬] [    (')
        print(linha_vermemelha)

        if decisao == '1':
            listar(jogadores)
                
        elif decisao == '2':
            jogador_randomico(jogadores)
                        
        else:
            continua = False
            console.print(f'! --- [✅] [{centralizar_texto(finalizacao)}] [✅] --- !', style='blink bold black underline on white')
            print(linha_vermemelha)
            print('')
            
main()