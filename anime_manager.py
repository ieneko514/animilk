from PySide6.QtCore import QObject
from PySide6.QtWidgets import QWidget
from database import Anime
from ui_anime_manager import Ui_AnimeManagerFragment

class AnimeManagerFragment(QObject):
  def __init__(self, base: QWidget, anime: Anime):
    QObject.__init__(self)

    self._base = base
    self._anime = anime

    self._ui = Ui_AnimeManagerFragment()
    self._ui.setupUi(self._base)

    self._ui.label_title.setText(anime.display_name)
