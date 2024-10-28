import os
from rich.console import Console
from rich import print
from rich.progress import track
from rich.panel import Panel


console = Console(record=True)
blue_console = Console(style="white on blue")

# declarando todas as funções de calculo
def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Erro: Divisão por zero"
    return x / y

# crio o fluxo de chamada dessa função
def calculadora():
    
    # atrelando as chamadas
    operacoes = { 
        '+': add,
        '-': subtract,
        '*': multiply,
        '/': divide
    } 
    
    # estrutura de repetição
    while True:
        os.system('cls' if os.name == 'nt' else 'clear') 
        try:
            print("|--------------------------------------------------------|")
            print("[🎩]                    CALCULATOR                    [🎩]")
            print("|--------------------------------------------------------|")
            print("[⏬]                  DIGITE UM NÚMERO                [⏬]")
            print("|--------------------------------------------------------|")   
            x = float(input("[🗣️  you: "))
            print("|--------------------------------------------------------|")
            print("[⏬]                 DIGITE OUTRO NÚMERO              [⏬]")
            print("|--------------------------------------------------------|")
            y = float(input("[🗣️  you: "))
            print("|--------------------------------------------------------|")
        
        # tratando se caso o input for inválido    
        except ValueError:
            print("|--------------------------------------------------------|")
            print("|          Esses não são os dróides que procura          |")
            print("|--------------------------------------------------------|")
            input("|❌ Erro404: Entrada inválida, insira números válidos.❌ |")
            print("|--------------------------------------------------------|")
            continue
        
        print("[🎩]                   OPERAÇÃO DESEJADA              [🎩]")
        print("|--------------------------------------------------------|")
        print("[⏬]                ('+', '-', '*', '/')              [⏬]")
        print("|--------------------------------------------------------|")
        operacao = input("[🗣️  you: ")
        print("|--------------------------------------------------------|")

        if operacao in operacoes:
            resultado = (operacoes[operacao](x, y)  )
            print("")
            print("Congrats, this is your calc stu:")
            print("|---------------------------------------------------------|")
            print("[✅]                        RESULTADO                  [✅]")
            print("|---------------------------------------------------------|")
            print(f"[✅] {resultado}")
            print("|---------------------------------------------------------|")

        else:
            print("|--------------------------------------------------------|")
            print("|          Esses não são os dróides que procura          |")
            print("|--------------------------------------------------------|")
            input("|❌ Erro404: Entrada inválida, insira números válidos.❌ |")
            print("|--------------------------------------------------------|")
                
        print("")
        print("|---------------------------------------------------------|")
        print("[🎩]           RESUMIR? Digite 'Resumir'               [🎩]")
        print("|---------------------------------------------------------|")        
        print("[⏬]        NOVA OPERAÇÃO - SIM OU NÃO? (s/n):         [⏬]")
        print("|---------------------------------------------------------|")
        continuar = input("[🗣️  you: ")
        print("|---------------------------------------------------------|")
        
        if continuar.lower() == 'n':    
            print("|---------------------------------------------------------|") 
            print("[🎩]                      ADIOS MI AMIGO               [🎩]")
            print("|---------------------------------------------------------|")
            break

# Executar a calculadora
calculadora()