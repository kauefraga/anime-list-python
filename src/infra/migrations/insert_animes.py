from datetime import datetime
from infra.db import Anime

def insert_animes():
  Anime.create(
    title='Mirai Nikki',
    url='https://betteranime.net/anime/legendado/mirai-nikki',
    created_at=datetime.now()
  )
  Anime.create(
    title='Beast Tamer',
    url='https://betteranime.net/anime/legendado/yuusha-party-wo-tsuihou-sareta-beast-tamer-saikyoushu-no-nekomimi-shoujo-to-deau',
    created_at=datetime.now()
  )
  Anime.create(
    title='Rakudai Kishi',
    url='https://betteranime.net/anime/legendado/rakudai-kishi-no-cavalry',
    created_at=datetime.now()
  )
  Anime.create(
    title='Bocchi The Rock',
    url='https://betteranime.net/anime/legendado/bocchi-the-rock',
    created_at=datetime.now()
  )
  Anime.create(
    title='Akashic Records',
    url='https://betteranime.net/anime/legendado/rokudenashi-majutsu-koushi-to-akashic-records',
    created_at=datetime.now()
  )

if __name__ == '__main__':
  insert_animes()
