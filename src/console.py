from rich.console import Console
from rich.style import Style
from rich.theme import Theme
from rich.progress import track

console = Console()

console.print(style="red on white")
style = Style(color="magenta", bgcolor="yellow", italic=True)