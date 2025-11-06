from PySide6.QtCore import QObject
from PySide6.QtCore import Slot
from PySide6.QtWidgets import QWidget
from ui_new_anime import Ui_NewAnimeFragment

class NewAnimeFragment(QObject):
  def __init__(self, base: QWidget):
    QObject.__init__(self)

    self._base = base
    self._ui = Ui_NewAnimeFragment()
    self._ui.setupUi(self._base)

    for x in (self._ui.lineEdit_name, self._ui.lineEdit_abbr):
      x.textEdited.connect(self._chk_input)

  def setAnimeAbbreviation(self, val: str):
    self._ui.lineEdit_abbr.setText(val)

  @Slot(str)
  def _chk_input(self, crap: str):
    self._ui.pushButton_confirm.setEnabled(all(x.text() != '' for x in (self._ui.lineEdit_name, self._ui.lineEdit_abbr)))
