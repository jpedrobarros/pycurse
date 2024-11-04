from rich.console import Console

jogadores = [
    'Neymar', 'Ganso', 'Pelé', 
    'Garrincha', 'Ronaldo Fenômeno', 'Romário',
    'Zico', 'Rivelino', 'Sócrates', 'Ronaldinho Gaúcho',
    'Cafu', 'Roberto Carlos', 'Nilton Santos', 'Jairzinho',
    'Tostão', 'Falcão', 'Zizinho', 'Ademir da Guia',
    'Leônidas da Silva', 'Didi', 'Gérson', 'Júnior',
    'Dunga', 'Bebeto', 'Rivaldo', 'Kaká', 
    'Taffarel', 'Djalma Santos', 'Gilmar', 'Carlos Alberto Torres',
    'Zagallo', 'Vavá', 'Amarildo', 'Branco',
    'Careca', 'Arthur Friedenreich',  'Domingos da Guia',
    'Manga',  'Heleno de Freitas', 'Clodoaldo', 'Emerson Leão' 
]

linha_vermemelha = ('[bold red]!-----------------------------------------------------------------------------![/bold red]')
linha = ('[bold red]![/bold red]-----------------------------------------------------------------------------[bold red]![/bold red]')

console = Console()

def centralizar_texto(texto, largura=55):
    return texto.center(largura)

linha_vermemelha = '!' + '-' * 77 + '!'

# Textos fixos
subtitulo_inicial = 'SEJA BEM VINDO AO FUTURO!'
subtitulo_menu = 'MENU!'
subtitulo_decisao = 'EAE MEU CHAPA! QUER REPETIR OU VOLTAR??? - Sim(s) ou Não(n)??'
erro = 'VOLTA AE PAIZAO, NÃO ENTENDI'
finalizacao = 'ATÉ A PRÓXIMA E MUITO OBRIGADO!!!'
radonman = 'RANDON MODE!!!'

def title():
    console.print(f'! --- [🏆] [{centralizar_texto(subtitulo_menu)}] [🏆] --- !', style='bold black underline on white')
    print(linha_vermemelha)
    print('')