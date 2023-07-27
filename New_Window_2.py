# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'New_Window_2.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import sys
from New_Window4 import Ui_New_Window4
class Stream(QtCore.QObject):
    newText = QtCore.pyqtSignal(str)

    def write(self, text):
        self.newText.emit(str(text))


class Ui_New_Window_2(QtCore.QObject):
    def openWindow(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_New_Window4()
        self.ui.setupUi(self.window)
        self.window.show()

    def openWindow_2(self):
        f1=open('filename_2.txt','r')
        f2=open('filename.txt','w')
        f3=f1.read()
        f2.write(f3)
        from New_Window_3 import Ui_Main_Window_3
        self.window = QtWidgets.QMainWindow()
        #self.window.termination()
        self.ui = Ui_Main_Window_3()
        self.ui.setupUi(self.window)
        #refreshAll()
        

    def setupUi(self, New_Window_2):
        New_Window_2.setObjectName("New_Window_2")
        New_Window_2.showMaximized()
        New_Window_2.setStyleSheet("background-color: black;")
        sys.stdout = Stream(newText=self.onUpdateText)
        self.centralwidget = QtWidgets.QWidget(New_Window_2)
        self.centralwidget.setObjectName("centralwidget")
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(170, 180, 900, 400))
        self.textEdit.setStyleSheet("background-color: white;")
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setFamily("Cambria")
        self.textEdit.setFont(font)
        self.textEdit.setObjectName("textEdit")
        self.Stemming = QtWidgets.QRadioButton(self.centralwidget)
        self.Stemming.setGeometry(QtCore.QRect(1100, 300, 120, 41))
        self.Lemmatization = QtWidgets.QRadioButton(self.centralwidget)
        self.Lemmatization.setGeometry(QtCore.QRect(1100, 450, 140, 41))
        self.LOAD = QtWidgets.QPushButton(self.centralwidget)
        self.LOAD.setGeometry(QtCore.QRect(170, 122, 110, 41))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        font.setFamily("Cambria")
        font.setPointSize(12)
        self.Stemming.setFont(font)
        self.Stemming.setStyleSheet("color: white;")
        self.Stemming.setObjectName("Stemming")
        self.Lemmatization.setFont(font)
        self.Lemmatization.setStyleSheet("color: white;")
        self.Lemmatization.setObjectName("Lemmatization")
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        font.setFamily("Cambria")
        font.setPointSize(10)
        self.LOAD.setFont(font)
        self.LOAD.setStyleSheet("QPushButton""{""background-color : white;""}""QPushButton::pressed""{""background-color : aqua;""}")        
        self.LOAD.setFont(font)
        self.LOAD.setObjectName("LOAD")
        self.Next = QtWidgets.QPushButton(self.centralwidget)
        self.Next.setGeometry(QtCore.QRect(675, 680, 150, 41))
        self.Next.setStyleSheet("QPushButton""{""background-color : white;""}""QPushButton::pressed""{""background-color : aqua;""}")        
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        font.setPointSize(10)
        font.setFamily("Cambria")
        self.Next.setFont(font)
        self.Next.setObjectName("Next")
        self.Previous = QtWidgets.QPushButton(self.centralwidget)
        self.Previous.setGeometry(QtCore.QRect(440, 680, 150, 41))
        self.Previous.setStyleSheet("QPushButton""{""background-color : white;""}""QPushButton::pressed""{""background-color : aqua;""}")
        self.Previous.setFont(font)
        self.Previous.setObjectName("Previous")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(270, 30, 791, 61))
        font = QtGui.QFont()
        font.setFamily("Cambria")
        font.setPointSize(20)
        font.setBold(True)
        font.setItalic(True)
        font.setUnderline(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setWordWrap(True)
        self.label.setStyleSheet("color: white;")
        self.label.setObjectName("label")
        font = QtGui.QFont()
        font.setFamily("Cambria")
        font.setPointSize(16)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        New_Window_2.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(New_Window_2)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        New_Window_2.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(New_Window_2)
        self.statusbar.setObjectName("statusbar")
        New_Window_2.setStatusBar(self.statusbar)
        self.Stemming.toggled.connect(self.Stemming_p)
        self.Lemmatization.toggled.connect(self.lemmatize)
        self.LOAD.clicked.connect(self.load)
        self.Next.clicked.connect(self.openWindow)
        self.Previous.clicked.connect(self.openWindow_2)


        self.retranslateUi(New_Window_2)
        QtCore.QMetaObject.connectSlotsByName(New_Window_2)

    def retranslateUi(self, New_Window_2):
        _translate = QtCore.QCoreApplication.translate
        New_Window_2.setWindowTitle(_translate("New_Window_2", "MainWindow"))
        self.Stemming.setText(_translate("New_Window_2", "Stemming"))
        self.Lemmatization.setText(_translate("New_Window_2", "Lemmatization"))
        self.LOAD.setText(_translate("New_Window_2", "Previous data"))
        self.Next.setText(_translate("New_Window_2", "Next>>"))
        self.Previous.setText(_translate("New_Window_2", "<<Previous"))
        self.label.setText(_translate("New_Window_2", "Pre-Processing->Tokenization->Stop-Word-Removal->Stemming"))

    def onUpdateText(self, text):
        cursor = self.textEdit.textCursor()
        cursor.movePosition(QtGui.QTextCursor.End)
        cursor.insertText(text)
        self.textEdit.setTextCursor(cursor)
        self.textEdit.ensureCursorVisible()


    def Stemming_p(self) :
        from nltk.stem.porter import PorterStemmer
        file = open(r"filename.txt")
        text = file.read()
        file.close()
        from nltk.tokenize import word_tokenize
        tokens = word_tokenize(text)

        porter = PorterStemmer() 
        stemmed = [porter.stem(w) for w in tokens]
        stemmed = " ".join(stemmed)
        #for word in text
        print()
        print('_Stemmed Data_')
        print()
        print(stemmed)
        with open('filename.txt', 'w') as f:
            sys.stdout = f # Change the standard output to the file we created.
            print("Stemmed Data")
            print()
            print(stemmed)
        with open('filename_4.txt', 'w') as f:
            sys.stdout = f # Change the standard output to the file we created.
            print("Stemmed Data")
            print()
            print(stemmed)
            #sys.stdout = sys.stdout 
    
    def lemmatize(self) :
        from nltk.stem import WordNetLemmatizer
        file = open(r"filename.txt")
        text = file.read()
        file.close()
        from nltk.tokenize import word_tokenize
        tokens = word_tokenize(text)

        wordnet_lemmatizer = WordNetLemmatizer()
        lemmatized = [wordnet_lemmatizer.lemmatize(word) for word in tokens]
        lemmatized = " ".join(lemmatized)
        print()
        print('_Lemmatized data_')
        print()
        print(lemmatized)
        with open('filename.txt', 'w') as f:
            sys.stdout = f # Change the standard output to the file we created.
            print("Lemmatized Data")
            print()
            print(lemmatized)
            sys.stdout = sys.stdout
        with open('filename_4.txt', 'w') as f:
            sys.stdout = f # Change the standard output to the file we created.
            print("Lemmatized Data")
            print()
            print(lemmatized)


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
    New_Window_2 = QtWidgets.QMainWindow()
    ui = Ui_New_Window_2()
    ui.setupUi(New_Window_2)
    New_Window_2.show()
    sys.exit(app.exec_())

