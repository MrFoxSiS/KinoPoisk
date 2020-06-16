# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'DOC.ui'
#
# Created by: PyQt5 UI code generator 5.13.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form2(object):
    def setupUi(self, Form2):
        Form2.setObjectName("Form2")
        Form2.setFixedSize(401, 300)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("vopinc.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Form2.setWindowIcon(icon)
        self.textEdit = QtWidgets.QTextEdit(Form2)
        self.textEdit.setEnabled(True)
        self.textEdit.setGeometry(QtCore.QRect(10, 10, 381, 281))
        self.textEdit.setFocusPolicy(QtCore.Qt.WheelFocus)
        self.textEdit.setReadOnly(True)
        self.textEdit.setObjectName("textEdit")

        self.retranslateUi(Form2)
        QtCore.QMetaObject.connectSlotsByName(Form2)

    def retranslateUi(self, Form2):
        _translate = QtCore.QCoreApplication.translate
        Form2.setWindowTitle(_translate("Form2", "Help"))
        self.textEdit.setHtml(_translate("Form2", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Tahoma\'; font-size:14pt; font-weight:600; color:#383838; background-color:#ffffff;\">Стартовое окно:</span><span style=\" font-family:\'Tahoma\'; font-size:14pt; font-weight:600; color:#383838;\"> </span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Tahoma\'; font-size:10pt; font-weight:600; color:#383838; background-color:#ffffff;\">1) Название фильмов:</span><span style=\" font-family:\'Tahoma\'; font-size:10pt; font-weight:600; color:#383838;\"> </span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Tahoma\'; font-size:8pt; color:#383838; background-color:#ffffff;\">Поле предназначенное для ввода названий фильмов.</span><span style=\" font-family:\'Tahoma\'; font-size:8pt; color:#383838;\"> </span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Tahoma\'; font-size:8pt; color:#383838; background-color:#ffffff;\">Если вводится несколько фильмов, то названия отделяются Enter или,</span><span style=\" font-family:\'Tahoma\'; font-size:8pt; color:#383838;\"> </span><span style=\" font-family:\'Tahoma\'; font-size:8pt; color:#383838; background-color:#ffffff;\">зависит от настроек.</span><span style=\" font-family:\'Tahoma\'; font-size:8pt; color:#383838;\"> </span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Tahoma\'; font-size:10pt; font-weight:600; color:#383838; background-color:#ffffff;\">2) Информация о фильмах:</span><span style=\" font-family:\'Tahoma\'; font-size:8pt; font-weight:600; color:#383838;\"> </span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Tahoma\'; font-size:8pt; color:#383838; background-color:#ffffff;\">Поле куда выводится информация о фильмах в виде списка.</span><span style=\" font-family:\'Tahoma\'; font-size:8pt; color:#383838;\"> </span><span style=\" font-family:\'Tahoma\'; font-size:8pt; color:#383838; background-color:#ffffff;\">Фильмы берутся из поля &quot;Название фильмов:&quot;.</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Tahoma\'; font-size:8pt; color:#383838; background-color:#ffffff;\">Выводимую информацию о фильмах можно настроить в окне &quot;Settings&quot;.</span><span style=\" font-family:\'Tahoma\'; font-size:8pt; color:#383838;\"> </span></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Tahoma\'; font-size:14pt; font-weight:600; color:#383838; background-color:#ffffff;\">Settings:</span><span style=\" font-family:\'Tahoma\'; font-size:14pt; font-weight:600; color:#383838;\"> </span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Tahoma\'; font-size:8pt; color:#383838; background-color:#ffffff;\">окно с настройками приложения.</span><span style=\" font-family:\'Tahoma\'; font-size:8pt; color:#383838;\"> </span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Tahoma\'; font-size:10pt; font-weight:600; color:#383838; background-color:#ffffff;\">1)Разделитель фильмов:</span><span style=\" font-family:\'Tahoma\'; font-size:10pt; font-weight:600; color:#383838;\"> </span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Tahoma\'; font-size:8pt; color:#383838; background-color:#ffffff;\">Выпадающий список позволяющий выбрать способ разделения названий фильмов</span><span style=\" font-family:\'Tahoma\'; font-size:8pt; color:#383838;\"> </span><span style=\" font-family:\'Tahoma\'; font-size:8pt; color:#383838; background-color:#ffffff;\">в поле &quot;Названия фильмов:&quot; .</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Tahoma\'; font-size:10pt; font-weight:600; color:#383838; background-color:#ffffff;\">2)Кол фильмов:</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Tahoma\'; font-size:8pt; color:#383838; background-color:#ffffff;\">Параметр позволяющий указать количество фильмов в примере ниже.<br />Фильмы в примере ниже случайные и не настраиваются.</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Tahoma\'; font-size:10pt; font-weight:600; color:#383838; background-color:#ffffff;\">3)Данные о фильме:</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Tahoma\'; font-size:8pt; color:#383838; background-color:#ffffff;\">Это группа настроек при помощи которых можно контролировать выводимую информацию о фильмах.</span></p></body></html>"))
