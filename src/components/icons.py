from enum import Enum

# Needs rich module
class Icon(Enum):
  """The implemented symbols are: [+], [-] and [?]"""
  PLUS = '[green][[/green]+[green]][/green]'
  MINUS = '[red][[/red]-[red]][/red]'
  INTERROGATIVE = '[yellow][[/yellow]?[yellow]][/yellow]'
