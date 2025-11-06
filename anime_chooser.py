from PySide6.QtCore import QObject
from PySide6.QtWidgets import QWidget
from ui_anime_chooser import Ui_AnimeChooserFragment

class AnimeChooserFragment(QObject):
  def __init__(self, base: QWidget):
    QObject.__init__(self)

    self._base = base
    self._ui = Ui_AnimeChooserFragment()
    self._ui.setupUi(self._base)

    self._ui.lineEdit.setFocus()
