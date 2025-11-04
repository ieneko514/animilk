#!/usr/bin/env python
from argparse import ArgumentParser
import sys
from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QApplication
from PySide6.QtWidgets import QWidget
import res

def main() -> int:
  parser = ArgumentParser()


  args = parser.parse_args()

  app = QApplication([])

  app.setApplicationName('animilk')
  app.setWindowIcon(QIcon(':/animilk/icon.png'))

  window = QWidget()
  window.show()

  return app.exec()

if __name__ == '__main__':
  sys.exit(main())
