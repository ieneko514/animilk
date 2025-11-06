from PySide6.QtCore import QObject
from PySide6.QtCore import Slot
from PySide6.QtWidgets import QWidget
from new_anime import NewAnimeFragment
from ui_anime_chooser import Ui_AnimeChooserFragment

class AnimeChooserFragment(QObject):
  def __init__(self, base: QWidget):
    QObject.__init__(self)

    self._new_anime_window = QWidget()
    self._new_anime_fragment = NewAnimeFragment(self._new_anime_window)

    self._base = base
    self._ui = Ui_AnimeChooserFragment()
    self._ui.setupUi(self._base)

    self._ui.lineEdit.setFocus()
    self._ui.pushButton_create.clicked.connect(self._do_new_anime)

  @Slot()
  def _do_new_anime(self):
    self._new_anime_fragment.setAnimeAbbreviation(self._ui.lineEdit.text())
    self._new_anime_window.show()
    self._base.close()
