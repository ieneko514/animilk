import traceback
from PySide6.QtCore import QObject
from PySide6.QtCore import Signal
from PySide6.QtCore import Slot
from PySide6.QtWidgets import QMessageBox
from PySide6.QtWidgets import QWidget
from database import Anime
from database import db_write_new_anime
from ui_new_anime import Ui_NewAnimeFragment

class NewAnimeFragment(QObject):
  creationComplete = Signal(Anime)

  def __init__(self, base: QWidget, animes: dict[str, Anime], anime_list_path: str):
    QObject.__init__(self)

    self._base = base
    self._animes = animes
    self._anime_list_path = anime_list_path

    self._ui = Ui_NewAnimeFragment()
    self._ui.setupUi(self._base)

    for x in (self._ui.lineEdit_name, self._ui.lineEdit_abbr):
      x.textEdited.connect(self._chk_input)

    self._ui.pushButton_confirm.clicked.connect(self._do_creation)

  def setAnimeAbbreviation(self, val: str):
    self._ui.lineEdit_abbr.setText(val)

  @Slot(str)
  def _chk_input(self, crap: str):
    self._ui.pushButton_confirm.setEnabled(all(x.text() != '' for x in (self._ui.lineEdit_name, self._ui.lineEdit_abbr)))

  @Slot()
  def _do_creation(self):
    if (identifier := self._ui.lineEdit_abbr.text()) in self._animes.keys():
      QMessageBox.warning(self._base, 'Unable to create anime entry', 'An entry with this abbreviation already exists.')
      return

    try:
      db_write_new_anime(self._anime_list_path, anime := Anime(identifier, self._ui.lineEdit_name.text()))
    except OSError as exc:
      traceback.print_exc()
      QMessageBox.warning(self._base, None, f'Unable to write anime entry: {exc.strerror}')
      return

    QMessageBox.information(self._base, None, 'New anime entry created.')
    self.creationComplete.emit(anime)

    for x in (self._ui.lineEdit_name, self._ui.lineEdit_abbr):
      x.clear()

    self._ui.pushButton_confirm.setEnabled(False)

    self._base.close()
