import os
import time
import random

from rich import print
from console import console

from shared import jogadores, linha, linha_vermemelha

# Constantes
LARGURA_TEXTO = 55

# Textos
TITULO_JOGO = "FUTCOMPARE"
SUBTITULO_MENU = "MENU!"
SUBTITULO_LISTA = "LISTA COMPLETA DE JOGADORES"
SUBTITULO_ALEATORIO = "LISTA DE JOGADORES ALEATÓRIA"
MENSAGEM_REPETIR = "REPETIR OU VOLTAR? - Sim(s) ou Não(n)?"
ERRO = "VOLTA AE PAIZAO, NÃO ENTENDI"
FINALIZACAO = "ATÉ A PRÓXIMA E MUITO OBRIGADO!!!"

def centralizar_texto(texto, largura=LARGURA_TEXTO):
    """Centraliza o texto em um determinado espaço."""
    return texto.center(largura)

def exibir_lista_aleatoria(jogadores):
    """Exibe uma lista aleatória de 10 jogadores."""
    if not jogadores:
        print("Erro: Nenhum jogador disponível.")
        return
    
    aleatorios = random.sample(jogadores, min(10, len(jogadores)))
    print(linha_vermemelha)
    console.print(f'! --- [🏆] [{centralizar_texto(SUBTITULO_ALEATORIO)}] [🏆] --- !', style='bold black underline on white')
    print(linha_vermemelha)

    time.sleep(0.8)

    for jogador in aleatorios:
        jogador_formatado = centralizar_texto(jogador)
        print(linha)
        print(f'! --- [⚽] [{jogador_formatado}] [⚽] --- !')
        print(linha)
        time.sleep(0.2)
        
    obter_decisao(lambda: exibir_lista_aleatoria(jogadores))

def listar(jogadores):
    """Lista os jogadores de forma padrão."""
    title()
    time.sleep(0.8)

    for jogador in jogadores:
        jogador_formatado = centralizar_texto(jogador)
        print(linha)
        print(f'! --- [⚽] [{jogador_formatado}] [⚽] --- !')
        print(linha)
        time.sleep(0.1)
        
    obter_decisao(lambda: listar(jogadores))

def obter_decisao(reapet):
    """Pergunta ao usuário se ele deseja repetir a ação ou voltar ao menu."""
    continua = True
    while continua:
        console.print(f'! --- [🏆] [{centralizar_texto(MENSAGEM_REPETIR)}] [🏆] --- !', style='bold black underline on white')
        print(linha_vermemelha)
        decisao_lista = input('! --- [💬]: ')
        print(linha_vermemelha)

        if decisao_lista == 's':
            os.system('clear')
            reapet()
            continua = False  # Sai do loop após executar a ação
        elif decisao_lista == 'n':
            main()
            continua = False  # Sai do loop após voltar ao menu
        else:
            print(f'! --- [❌] [{centralizar_texto(ERRO)}] [❌] --- !')
            print(linha)

def title():
    """Exibe o cabeçalho do programa."""
    os.system('clear')
    console.print(f'! --- [🏆] [{centralizar_texto(SUBTITULO_MENU)}] [🏆] --- !', style='blink bold black underline on white')
    print(linha_vermemelha)
    os.system('figlet -c THE BEST!')
    print(linha_vermemelha)
    console.print(f'! --- [🏆] [{centralizar_texto(SUBTITULO_MENU)}] [🏆] --- !', style='bold black underline on white')
    print(linha_vermemelha)

def exibir_menu():
    """Exibe o menu de opções."""
    print(linha_vermemelha)
    console.print('! --- [📟] [  (1) - LISTAR COMPLETA  ]     ❌     [  (2) - LISTA ALEATÓRIA  ] [📄] --- !', style='bold')
    print(linha_vermemelha)
    console.print('! --- [📟] [  (0) - SAIR            ]     ❌     [  (4) - XX               ] [📄] --- !', style='bold')
    print(linha_vermemelha)

def main():
    """Função principal do programa."""
    continua = True
    while continua:
        title()
        exibir_menu()
        
        opcao_menu = input('! --- [💬] [    (')
        print(linha_vermemelha)

        if opcao_menu == '1':
            listar(jogadores)
        elif opcao_menu == '2':
            exibir_lista_aleatoria(jogadores)
        elif opcao_menu == '0':
            console.print(f'! --- [✅] [{centralizar_texto(FINALIZACAO)}] [✅] --- !', style='bold black underline on white')
            print(linha_vermemelha)
            print('')
            continua = False  # Sai do loop principal
        else:
            print(f"! --- [❌] [{centralizar_texto(ERRO)}] [❌] --- !")
            print(linha)

if __name__ == "__main__":
    main()