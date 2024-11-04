import os
import time

from rich import print
from rich.color import Color
from rich.console import Console
from rich.style import Style

from backend import jogadores, linha, linha_vermemelha

console = Console()
base_style = Style.parse("cyan")

# Constantes
LARGURA_TEXTO = 59
ID_JOGADOR1 = 1
ID_JOGADOR2 = 2
PONTO = 1
PERGUNTAS: list = ['Drilhe?', 'Velocidade?', 'Chute?', 'Elasticidade?', 'Força?', 'Malandragem?']

# Textos
TITULO_JOGO = "FUTCOMPARE"
SUBTITULO_INICIAL = "DIGITE UM NOVO JOGADOR PARA A LISTA"
MENSAGEM_CONTINUAR = "EAE MEU CHAPA! QUER CONTINUAR POR AQUI - Sim(s) ou Não(n)?"
ERRO = "VOLTA AE PAIZAO, NÃO ENTENDI"
FINALIZACAO = "ATÉ A PRÓXIMA E MUITO OBRIGADO!!!"

def centralizar_texto(texto, largura=LARGURA_TEXTO):
    """Centraliza o texto em um determinado espaço."""
    return texto.center(largura)

def exibir_cabecalho():
    """Exibe o cabeçalho do jogo."""
    os.system('cls' if os.name == 'nt' else 'clear')
    print(linha_vermemelha)
    console.print(f"! --- [🏆] [{centralizar_texto(TITULO_JOGO)}] [🏆] --- !", style="bold black underline on blue")
    print(linha_vermemelha)
    os.system('figlet -c THE BEST!')
    print(linha_vermemelha)
    console.print(f"! --- [🏆] [{centralizar_texto(SUBTITULO_INICIAL)}] [🏆] --- !", style="bold black underline on blue")
    print(linha_vermemelha)

def listar_jogadores():
    """Lista os jogadores na tela."""
    for jogador in jogadores:
        jogador_formatado = centralizar_texto(jogador)
        print(linha)
        print(f"! --- [⚽] [{jogador_formatado}] [⚽] --- !")
        print(linha)
        time.sleep(0.5)

def obter_decisao():
    """Pergunta ao usuário se ele deseja continuar."""
    console.print(f"! --- [💬] [{centralizar_texto(MENSAGEM_CONTINUAR)}] [💬] --- !", style="blink bold black underline on white")
    print(linha_vermemelha)
    decisao = input("! --- [💬]: ")
    print(linha_vermemelha)
    return decisao

def main():
    """Função principal do jogo."""
    continuar = True
    while continuar:
        exibir_cabecalho()
        adicionar_jogador()  # Chama a função para adicionar jogador
        listar_jogadores()
        decisao = obter_decisao()

        if decisao == "s":
            os.system("cls" if os.name == "nt" else "clear")
        elif decisao != "n":
            print(f"! --- [❌] [{centralizar_texto(ERRO)}] [❌] --- !")
            print(linha)
        else:
            continuar = False
            console.print(f"! --- [✅] [{centralizar_texto(FINALIZACAO)}] [✅] --- !", style="blink bold black underline on white")
            print(linha_vermemelha)
            print("")

if __name__ == "__main__":
    main()