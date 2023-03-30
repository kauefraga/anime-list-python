import click
from rich import print

from components.icons import Icon


SITES = [
  f'{Icon.PLUS.value} https://animesonlinex.cx - https://animesgratis.org',
  f'{Icon.PLUS.value} https://animestc.net',
  f'{Icon.PLUS.value} https://animeszone.net',
  f'{Icon.PLUS.value} https://www.anroll.net',
  f'{Icon.MINUS.value} https://betteranime.net',
  f'{Icon.MINUS.value} https://puray.moe',
  f'{Icon.MINUS.value} https://animesonline.cc',
]

@click.command()
def status():
  """List the available and unavailable websites for watching anime"""
  for i in range(len(SITES)):
    print(SITES[i])
