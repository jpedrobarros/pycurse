from console import console

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

linha_vermemelha = ('[bold red]!---------------------------------------------------------------------------------![/bold red]')
linha = ('[bold red]![/bold red]---------------------------------------------------------------------------------[bold red]![/bold red]')
linha_icons = ('! --- [😝] [ ')

tamanho_linha: int = len(linha)
tamanho_linha_icons: int = len(linha_icons)

tamanho_espaco = (tamanho_linha - (tamanho_linha_icons * 2))
