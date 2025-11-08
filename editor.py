#!/usr/bin/env python
from argparse import ArgumentParser
import locale
from locale import LC_COLLATE
import sys
from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QApplication
from PySide6.QtWidgets import QWidget
from anime_chooser import AnimeChooserFragment
import res

def main() -> int:
  parser = ArgumentParser()

  parser.add_argument('-anime_list', help='specify path to animes.tsv to operate on', required=True)

  args = parser.parse_args()

  app = QApplication([])

  app.setApplicationName('animilk')
  app.setWindowIcon(QIcon(':/animilk/icon.png'))

  window = QWidget()
  x = AnimeChooserFragment(window, args.anime_list)
  window.show()

  return app.exec()

if __name__ == '__main__':
  locale.setlocale(LC_COLLATE, 'ja_JP.UTF-8')
  sys.exit(main())
