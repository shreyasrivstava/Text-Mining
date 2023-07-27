# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'New_Window_3.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5 import *
from PyQt5.QtCore import *
from New_Window_2 import Ui_New_Window_2
import sys
class Stream(QtCore.QObject):
    newText = QtCore.pyqtSignal(str)

    def write(self, text):
        self.newText.emit(str(text))

class Ui_Main_Window_3(QObject):
    def openWindow(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_New_Window_2()
        self.ui.setupUi(self.window)
        self.window.show()


    def openWindow_2(self):
        
        from New_Window import Ui_New_Window
        self.window = QtWidgets.QMainWindow()
        #self.window.termination()
        self.ui = Ui_New_Window()
        self.ui.setupUi(self.window)
        #refreshAll()

    def setupUi(self, Main_Window_3):
        Main_Window_3.setObjectName("Main_Window_3")
        Main_Window_3.showMaximized()
        Main_Window_3.setStyleSheet("background-color: black;")
        sys.stdout = Stream(newText=self.onUpdateText)
        self.centralwidget = QtWidgets.QWidget(Main_Window_3)
        self.centralwidget.setObjectName("centralwidget")
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(170, 160, 900, 400))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setFamily("Cambria")
        self.textEdit.setFont(font)
        self.textEdit.setStyleSheet("background-color: white;")
        self.textEdit.setObjectName("textEdit")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(300, 20, 671, 51))
        font = QtGui.QFont()
        font.setFamily("Cambria")
        font.setPointSize(20)
        font.setBold(True)
        font.setItalic(True)
        font.setUnderline(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setWordWrap(False)
        self.label.setStyleSheet("color: white;")
        self.label.setObjectName("label")
        self.LOAD = QtWidgets.QPushButton(self.centralwidget)
        self.LOAD.setGeometry(QtCore.QRect(170, 100, 135, 41))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        font.setPointSize(10)
        font.setFamily("Cambria")
        self.LOAD.setFont(font)
        self.LOAD.setStyleSheet("QPushButton""{""background-color : white;""}""QPushButton::pressed""{""background-color : aqua;""}")
        self.LOAD.setObjectName("LOAD")
        self.SWR = QtWidgets.QPushButton(self.centralwidget)
        self.SWR.setGeometry(QtCore.QRect(1110, 510, 150, 41))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        font.setPointSize(10)
        font.setFamily("Cambria")
        self.SWR.setFont(font)
        self.SWR.setStyleSheet("QPushButton""{""background-color : white;""}""QPushButton::pressed""{""background-color : aqua;""}")
        self.SWR.setObjectName("SWR")
        self.Next = QtWidgets.QPushButton(self.centralwidget)
        self.Next.setGeometry(QtCore.QRect(675, 680, 150, 41))
        font = QtGui.QFont()
        font.setBold(True)
        font.setPointSize(10)
        font.setFamily("Cambria")
        self.Next.setFont(font)
        self.Next.setStyleSheet("QPushButton""{""background-color : white;""}""QPushButton::pressed""{""background-color : aqua;""}")
        self.Next.setObjectName("Next")
        self.Previous = QtWidgets.QPushButton(self.centralwidget)
        self.Previous.setGeometry(QtCore.QRect(440, 680, 150, 41))
        self.Previous.setStyleSheet("QPushButton""{""background-color : white;""}""QPushButton::pressed""{""background-color : aqua;""}")
        self.Previous.setFont(font)
        self.Previous.setObjectName("Previous")
        Main_Window_3.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(Main_Window_3)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        Main_Window_3.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(Main_Window_3)
        self.statusbar.setObjectName("statusbar")
        Main_Window_3.setStatusBar(self.statusbar)

        self.retranslateUi(Main_Window_3)
        QtCore.QMetaObject.connectSlotsByName(Main_Window_3)
        self.Next.clicked.connect(self.openWindow)
        self.Previous.clicked.connect(self.openWindow_2)
        self.SWR.clicked.connect(self.swr)
        self.LOAD.clicked.connect(self.load)

    def retranslateUi(self, Main_Window_3):
        _translate = QtCore.QCoreApplication.translate
        Main_Window_3.setWindowTitle(_translate("Main_Window_3", "MainWindow"))
        self.label.setText(_translate("Main_Window_3", "Pre-Processing->Tokenization->Stop-Word-Removal"))
        self.LOAD.setText(_translate("Main_Window_3", "Load Previous Data"))
        self.SWR.setText(_translate("Main_Window_3", "Remove Stop Words"))
        self.Next.setText(_translate("Main_Window_3", "Next>>"))
        self.Previous.setText(_translate("Main_Window_3", "<<Previous"))


    def onUpdateText(self, text):
        cursor = self.textEdit.textCursor()
        cursor.movePosition(QtGui.QTextCursor.End)
        cursor.insertText(text)
        self.textEdit.setTextCursor(cursor)
        self.textEdit.ensureCursorVisible()


    def swr(self) :
        #from gensim.parsing.preprocessing import remove_stopwords
        #[w for w in self.words if not w in stop_words]
        import nltk
        from nltk.corpus import stopwords
        from nltk.tokenize import word_tokenize
        stop_words = nltk.corpus.stopwords.words('english')
        #self.word = [w for w in self.w if not w in stop_words]
        file = open(r"filename.txt")
        text = file.read()
        file.close()
        text_tokens = word_tokenize(text)
        newStopWords = ['shall','should','could','could not','should not','would','would not']
        stop_words.extend( newStopWords)
        tokens_without_sw = [word for word in text_tokens if not word in stop_words]
        tokens_without_sw = " ".join(tokens_without_sw)
        print()
        print("_Stop Words Removed_")
        print()
        print(tokens_without_sw)
        with open('filename.txt', 'w') as f:
            sys.stdout = f # Change the standard output to the file we created.
            print(tokens_without_sw)
            sys.stdout = sys.stdout 
        with open('filename_3.txt', 'w') as f:
            sys.stdout = f # Change the standard output to the file we created.
            print(tokens_without_sw)
            sys.stdout = sys.stdout 
        
    def load(self) :
        print('Current State of data')
        print()
        file = open(r"filename.txt")
        text = file.read()
        file.close()
        print(text)  
        


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Main_Window_3 = QtWidgets.QMainWindow()
    ui = Ui_Main_Window_3()
    ui.setupUi(Main_Window_3)
    Main_Window_3.show()
    sys.exit(app.exec_())

