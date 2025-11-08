import csv
import dataclasses
from dataclasses import dataclass
from typing import Self
from typing import Sequence

class DatabaseError(Exception):
  pass

@dataclass
class Anime:
  """hold some basic information"""

  # short name
  identifier: str

  # full title in Japanese
  display_name: str

  def to_csv_row(self) -> Sequence[str]:
    return dataclasses.astuple(self)

  @classmethod
  def from_csv_row(cls, row: Sequence[str]) -> Self:
    try:
      return cls(*row)
    except TypeError as exc:
      raise DatabaseError('Malformed anime entry') from exc

def db_read_anime_list(path: str) -> dict[str, Anime]:
  """offer an index by anime ID"""

  animes = {}

  with open(path, 'r', newline='', encoding='utf-8') as f:
    for row in csv.reader(f, csv.excel_tab):
      anime = Anime.from_csv_row(row)
      animes[anime.identifier] = anime

  return animes

def db_write_new_anime(path: str, anime: Anime):
  """insert a new record into the list file on disk"""

  with open(path, 'a', newline='', encoding='utf-8') as f:
    csv.writer(f, csv.excel_tab).writerow(anime.to_csv_row())
