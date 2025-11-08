import traceback
import sys
from PySide6.QtCore import QEventLoop
from PySide6.QtCore import QObject
from PySide6.QtCore import QTimer
from PySide6.QtCore import Slot
from PySide6.QtWidgets import QListWidgetItem
from PySide6.QtWidgets import QMessageBox
from PySide6.QtWidgets import QWidget
from anime_manager import AnimeManagerFragment
from database import Anime
from database import db_read_anime_list
from new_anime import NewAnimeFragment
from ui_anime_chooser import Ui_AnimeChooserFragment

class AnimeChooserFragment(QObject):
  def __init__(self, base: QWidget, anime_list_path: str):
    QObject.__init__(self)

    try:
      self._anime_table = db_read_anime_list(anime_list_path)
    except OSError as exc:
      traceback.print_exc()
      QMessageBox.critical(base, None, f'Unable to load anime list: {exc.strerror}')
      sys.exit(1)

    self._anime_list = list(self._anime_table.values())
    self._sort()

    self._new_anime_window = QWidget()
    self._new_anime_fragment = NewAnimeFragment(self._new_anime_window, self._anime_table, anime_list_path)

    self._base = base
    self._ui = Ui_AnimeChooserFragment()
    self._ui.setupUi(self._base)

    self._debounce_timer = QTimer()
    self._debounce_timer.setInterval(1000)
    self._debounce_timer.setSingleShot(True)
    self._debounce_timer.timeout.connect(self._do_upd_list)

    self._ui.lineEdit.setFocus()
    self._ui.lineEdit.textEdited.connect(self._sched_upd_list)
    self._ui.listWidget.itemDoubleClicked.connect(self._do_enter_manager)
    self._ui.pushButton_create.clicked.connect(self._do_new_anime)
    self._new_anime_fragment.creationComplete.connect(self._new_anime_cb)

    self._on_screen_list = []
    self._refresh_list()

  def _sort(self):
    self._anime_list.sort(key=lambda x: x.identifier)

  def _refresh_list(self):
    self._ui.listWidget.clear()
    self._on_screen_list.clear()

    query = self._ui.lineEdit.text()
    pretty_names = []

    for x in self._anime_list:
      if x.identifier.startswith(query):
        self._on_screen_list.append(x)
        pretty_names.append(x.display_name)

    self._ui.listWidget.addItems(pretty_names)

  @Slot()
  def _do_upd_list(self):
    self._refresh_list()

  @Slot(str)
  def _sched_upd_list(self, crap: str):
    self._debounce_timer.start()

  @Slot()
  def _do_new_anime(self):
    self._new_anime_fragment.setAnimeAbbreviation(self._ui.lineEdit.text())
    self._new_anime_window.show()
    self._base.close()

  @Slot(Anime)
  def _new_anime_cb(self, anime: Anime):
    # keep the contents inside lineEdit,
    # so the user won't have to type it again.

    self._base.show()

    self._anime_table[anime.identifier] = anime
    self._anime_list.append(anime)
    self._sort()

    self._refresh_list()

  @Slot(QListWidgetItem)
  def _do_enter_manager(self, item: QListWidgetItem):
    idx = self._ui.listWidget.indexFromItem(item).row()

    window = QWidget()
    x = AnimeManagerFragment(window, self._on_screen_list[idx])

    window.show()
    self._base.close()

    QEventLoop().exec()
