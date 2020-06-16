import sys
from random import randint
from kinopoisk.movie import Movie
from PyQt5 import QtWidgets
from INT import Ui_MainWindow
from PyQt5.QtGui import QIcon
from SET import Ui_MainWindow2
from PyQt5.QtCore import Qt, QSettings
from DOC import Ui_Form2
from PyQt5 import Qt as gi
from time import sleep
# список фильмов для пимера
lis = ("Джокер", "лило и стич", "Рик и морти", "Игра пристолов", "Люди в черном", "Трансформеры",
       "призрак в доспехах", "1+1", "движение вверх", "как приучить дракона", "человек из стали", "Бэтмен")


class Log(gi.QThread):
    load_finished = gi.pyqtSignal(object)
    gif = 0

    def __init__(self, lines):
        super().__init__()
        Log.gif += 1
        self.lines = lines

    def run(self):
        for film in self.lines:
            self.xxx = []
            movie = Movie.objects.search(film)
            dxd = []
            if len(movie) > 0:
                if Win.tit == 1:
                    t1 = movie[0].title
                    if len(t1) >= 14:
                        dxd.append(t1)
                    elif len(t1) <= 13:
                        dxd.append(t1 + "\t")
                if Win.yea == 1:
                    dxd.append(str(movie[0].year))
                if Win.rat == 1:
                    dxd.append(str(movie[0].rating))
                if Win.ra == 1:
                    dxd.append(str(movie[0].runtime))
            elif len(movie) == 0:
                Win.nofilm += 1
                Win.film -= 1
                self.dxd3 = []
                if Win.tit == 1:
                    dxd.append("фильм не найден")
                    self.dxd3.append("фильм не найден")
                if Win.yea == 1:
                    dxd.append("нету")
                    self.dxd3.append("нету")
                if Win.rat == 1:
                    dxd.append("нету")
                    self.dxd3.append("нету")
                if Win.ra == 1:
                    dxd.append("нету")
                    self.dxd3.append("нету")
            if dxd not in self.xxx:
                self.xxx.append(dxd)
            elif dxd == self.dxd3:
                self.xxx.append(dxd)
            self.load_finished.emit(self.xxx)
            sleep(randint(1, 5))
        Log.gif = 0


# Основное окно
class Win(QtWidgets.QMainWindow, Ui_MainWindow):
    # Переменнные настроек
    ror = '\n'
    tit = 1
    yea = 1
    rat = 1
    ra = 1
    isp = 0
    film = 0
    nofilm = 0
    stat = 0

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowIcon(QIcon('icon.png'))
        self.statusBar()
        self.btnBrowse.clicked.connect(self.browse_folder)
        self.statusBar().showMessage("Ввод: 0 б     Вывод: 0 Ф")
        self.toolButton.clicked.connect(self.open)
        self.load_settings()
        Win.stat += 1

# Функция поиска фильма
    def browse_folder(self):
        if Log.gif == 0:
            self.grid = 0
            Win.isp += 1
            self.textEdit.clear()
            self.films_file = self.textEdit_2.toPlainText()
            self.fi = len(self.textEdit_2.toPlainText())
            self.jojo = []
            if Win.tit == 1:
                self.jojo.append("Название:\t")
            if Win.yea == 1:
                self.jojo.append("Год:")
            if Win.rat == 1:
                self.jojo.append("Рэйтинг:")
            if Win.ra == 1:
                self.jojo.append("Длительность(Мин):")
            self.textEdit.append("\t".join(self.jojo))
            if self.fi == 0:
                self.textEdit_2.setText("Введите название фильма")
            else:
                self.lines = self.films_file.split(Win.ror)
                self.progressBar.setMaximum(len(self.lines))
                self.thread = Log(self.lines)
                self.thread.load_finished.connect(self.vil)
                self.thread.finished.connect(self.thread.deleteLater)
                self.thread.start()
            self.statusBar().showMessage("Ввод: " + str(self.fi) + " б     Вывод: " + str(len(self.lines)) + " Ф")
            Win.film += len(self.lines)

    def vil(self, xxx):
        self.grid += 1
        if len(xxx) > 0:
            for v in xxx:
                self.textEdit.append("\t".join(v))
        self.progressBar.setProperty("value", self.grid)

# Открытие окна настроек
    def open(self):
        self.window2 = Win2()
        self.window2.show()

# Сохранение данных при выходе
    def closeEvent(self, e):
        settings = QSettings('config.ini', QSettings.IniFormat)
        settings.setValue('te1', self.textEdit_2.toPlainText())
        settings.setValue('te2', self.textEdit.toPlainText())
        settings.setValue('Geometry', self.saveGeometry())
        settings.setValue('ror', Win.ror)
        settings.setValue('tit', Win.tit)
        settings.setValue('yea', Win.yea)
        settings.setValue('rat', Win.rat)
        settings.setValue('ra', Win.ra)
        settings.setValue('isp', Win.isp)
        settings.setValue('film', Win.film)
        settings.setValue('stat', Win.stat)
        settings.setValue('nofilm', Win.nofilm)
        super().closeEvent(e)

    def load_settings(self):
        settings = QSettings('config.ini', QSettings.IniFormat)
        geometry = settings.value('Geometry')
        if geometry:
            self.restoreGeometry(geometry)
        self.textEdit_2.setText(settings.value('te1'))
        self.textEdit.setText(settings.value('te2'))
        Win.ror = settings.value('ror', '\n')
        Win.tit = int(settings.value('tit', 1))
        Win.yea = int(settings.value('yea', 1))
        Win.rat = int(settings.value('rat', 1))
        Win.ra = int(settings.value('ra', 1))
        Win.isp = int(settings.value('isp', 0))
        Win.film = int(settings.value('film', 0))
        Win.stat = int(settings.value('stat', 0))
        Win.nofilm = int(settings.value('nofilm', 0))


# Окно настроек
class Win2(QtWidgets.QMainWindow, Ui_MainWindow2):

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.comboBox.addItem("Enter")
        self.comboBox.addItem(",")
        self.comboBox.activated[int].connect(self.lol1)
        self.checkBox.stateChanged.connect(self.title)
        self.checkBox_2.stateChanged.connect(self.year)
        self.checkBox_3.stateChanged.connect(self.rating)
        self.pushButton.clicked.connect(self.open2)
        self.pushButton_2.clicked.connect(self.text)
        self.checkBox_4.stateChanged.connect(self.runtime)
        self.load_settings()
        self.text()
        self.label_12.setText(str(Win.isp))
        self.label_11.setText(str(Win.film))
        if Win.stat == 1:
            self.label_7.setText(str(Win.stat) + " раз")
        if Win.stat >= 5:
            self.label_7.setText(str(Win.stat)+" раз")
        elif Win.stat > 1 and Win.stat < 5:
            self.label_7.setText(str(Win.stat) + " раза")
        self.label_13.setText(str(Win.nofilm))

    # Сохранение данных при выходе
    def closeEvent(self, e):
        settings = QSettings('config.ini', QSettings.IniFormat)
        settings.setValue('Geometry2', self.saveGeometry())
        settings.setValue('tit', int(self.checkBox.isChecked()))
        settings.setValue('yea', int(self.checkBox_2.isChecked()))
        settings.setValue('rat', int(self.checkBox_3.isChecked()))
        settings.setValue('ra', int(self.checkBox_4.isChecked()))
        settings.setValue('ras', int(self.comboBox.currentIndex()))
        settings.setValue('prim', int(self.spinBox.text()))
        super().closeEvent(e)

    def load_settings(self):
        settings = QSettings('config.ini', QSettings.IniFormat)
        geometry = settings.value('Geometry2')
        if geometry:
            self.restoreGeometry(geometry)
        self.checkBox.setChecked(bool(int(settings.value('tit', 1))))
        self.checkBox_2.setChecked(bool(int(settings.value('yea', 1))))
        self.checkBox_3.setChecked(bool(int(settings.value('rat', 1))))
        self.checkBox_4.setChecked(bool(int(settings.value('ra', 1))))
        self.comboBox.setCurrentIndex(int(settings.value('ras', 0)))
        self.spinBox.setValue(int(settings.value('prim', 1)))

# Загруска примера
    def text(self):
        self.textEdit.clear()
        self.xxx2 = []
        self.fif = int(self.spinBox.text())
        self.jojo = []
        if Win.tit == 1:
            self.jojo.append("Название:\t")
        if Win.yea == 1:
            self.jojo.append("Год:")
        if Win.rat == 1:
            self.jojo.append("Рэйтинг:")
        if Win.ra == 1:
            self.jojo.append("Длительность(Мин):")
        self.xxx2.append(self.jojo)
        for x in range(self.fif):
            self.ran = randint(0, 11)
            self.movie = Movie.objects.search(lis[self.ran])
            self.dxd2 = []
            if Win.tit == 1:
                self.t1 = self.movie[0].title
                if len(self.t1) >= 14:
                    self.dxd2.append(self.t1)
                elif len(self.t1) <= 13:
                    self.dxd2.append(self.t1 + "\t")
            if Win.yea == 1:
                self.y1 = self.movie[0].year
                self.dxd2.append(str(self.y1))
            if Win.rat == 1:
                self.r1 = self.movie[0].rating
                self.dxd2.append(str(self.r1))
            if Win.ra == 1:
                self.ra1 = self.movie[0].runtime
                self.dxd2.append(str(self.ra1))
            self.xxx2.append(self.dxd2)
        for v in self.xxx2:
            self.textEdit.append("\t".join(v))

# Настройки параметров
    def lol1(self, int):
        if int == 0:
            Win.ror = '\n'
        elif int == 1:
            Win.ror = ','

    def title(self, state1):

        if state1 == Qt.Checked:
            Win.tit = 1
        else:
            Win.tit = 0

    def year(self, state2):

        if state2 == Qt.Checked:
            Win.yea = 1
        else:
            Win.yea = 0

    def rating(self, state3):

        if state3 == Qt.Checked:
            Win.rat = 1
        else:
            Win.rat = 0

    def runtime(self, state4):

        if state4 == Qt.Checked:
            Win.ra = 1
        else:
            Win.ra = 0

    # Открытие окна документаии
    def open2(self):
        self.doc = Doc()
        self.doc.show()


# Документация
class Doc(QtWidgets.QMainWindow, Ui_Form2):

    def __init__(self):
        super().__init__()
        self.setupUi(self)


# Запуск приложния
if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = Win()
    window.show()
    app.exec_()
