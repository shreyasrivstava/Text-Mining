# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'New_Window4.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5 import QtCore, QtGui, QtWidgets
from New_Window5 import Ui_New_Window5
import sys
import numpy as np
import pandas as pd
import itertools
import operator
import nltk
from nltk.tokenize import word_tokenize
from nltk.tokenize import RegexpTokenizer
from nltk.stem import WordNetLemmatizer
from nltk.stem.porter import PorterStemmer
from nltk.corpus import wordnet

class Stream(QtCore.QObject):
    newText = QtCore.pyqtSignal(str)

    def write(self, text):
        self.newText.emit(str(text))


class Ui_New_Window4(object):
    def openWindow(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_New_Window5()
        self.ui.setupUi(self.window)
        self.window.show()

    def openWindow_2(self):
        f1=open('filename_3.txt','r')
        f2=open('filename.txt','w')
        f3=f1.read()
        f2.write(f3)
        from New_Window_2 import Ui_New_Window_2
        self.window = QtWidgets.QMainWindow()
        #self.window.termination()
        self.ui = Ui_New_Window_2()
        self.ui.setupUi(self.window)

    def setupUi(self, New_Window4):
        New_Window4.setObjectName("New_Window4")
        New_Window4.showMaximized()
        New_Window4.setStyleSheet("background-color: black;")
        sys.stdout = Stream(newText=self.onUpdateText)
        self.centralwidget = QtWidgets.QWidget(New_Window4)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(160, 20, 1020, 61))
        font = QtGui.QFont()
        font.setFamily("Cambria")
        font.setPointSize(20)
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        font.setItalic(True)
        self.label.setFont(font)
        self.label.setStyleSheet("color: white;")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setWordWrap(True)
        self.label.setObjectName("label")
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(170, 190, 900, 400))
        self.textEdit.setStyleSheet("background-color: white;")
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setFamily("Cambria")
        self.textEdit.setFont(font)
        self.textEdit.setObjectName("textEdit")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(1100, 350, 170, 41))
        self.lineEdit.setStyleSheet("background-color: white;")
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        font.setPointSize(10)
        font.setFamily("Cambria")
        self.lineEdit.setFont(font)
        self.lineEdit.setObjectName("lineEdit")
        self.CalculateInfoGain = QtWidgets.QPushButton(self.centralwidget)
        self.CalculateInfoGain.setGeometry(QtCore.QRect(1100, 540, 170, 41))
        self.CalculateInfoGain.setStyleSheet("QPushButton""{""background-color : white;""}""QPushButton::pressed""{""background-color : aqua;""}")
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        font.setPointSize(10)
        font.setFamily("Cambria")
        self.CalculateInfoGain.setFont(font)
        self.CalculateInfoGain.setObjectName("CalculateInfoGain")
        self.load = QtWidgets.QPushButton(self.centralwidget)
        self.load.setGeometry(QtCore.QRect(170, 130, 110, 41))
        self.load.setStyleSheet("QPushButton""{""background-color : white;""}""QPushButton::pressed""{""background-color : aqua;""}")
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        font.setPointSize(10)
        font.setFamily("Cambria")
        self.load.setFont(font)
        self.load.setObjectName("load")
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
        New_Window4.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(New_Window4)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        New_Window4.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(New_Window4)
        self.statusbar.setObjectName("statusbar")
        New_Window4.setStatusBar(self.statusbar)
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(1095, 300,170, 41))
        font = QtGui.QFont()
        font.setFamily("Cambria")
        font.setPointSize(13)
        font.setBold(True)
        
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("color: white;")
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")

        self.CalculateInfoGain.clicked.connect(self.sort)
        self.load.clicked.connect(self.loadfile)
        self.lineEdit.returnPressed.connect(self.returnum)
        self.Next.clicked.connect(self.openWindow)
        self.Previous.clicked.connect(self.openWindow_2)

        self.retranslateUi(New_Window4)
        QtCore.QMetaObject.connectSlotsByName(New_Window4)

    def retranslateUi(self, New_Window4):
        _translate = QtCore.QCoreApplication.translate
        New_Window4.setWindowTitle(_translate("New_Window4", "MainWindow"))
        self.label.setText(_translate("New_Window4", "Pre-Processing->Tokenization->Stopword Removal-> Stemming/Lemmatization->InfoGain"))
        self.CalculateInfoGain.setText(_translate("New_Window4", "Calculate InfoGain"))
        self.load.setText(_translate("New_Window4", "Previous Data"))
        self.Next.setText(_translate("New_Window4", "Next>>"))
        self.Previous.setText(_translate("New_Window4", "<<Previous"))
        self.label_3.setText(_translate("New_Window4", "Enter value of n here:"))


    def onUpdateText(self, text):
        cursor = self.textEdit.textCursor()
        cursor.movePosition(QtGui.QTextCursor.End)
        cursor.insertText(text)
        self.textEdit.setTextCursor(cursor)
        self.textEdit.ensureCursorVisible()

    def loadfile(self):
        file = open(r"filename.txt")
        self.text = file.read()
        print(self.text)
        print()
        print("Alert : ENTER THE VALUE OF N, YOU WANT TO CALCULATE InfoGain FOR AND THEN PRESS THE BUTTON!!!")
        print()
        file.close()
     
    def sort(self):
     
        dic = {}
        data = pd.read_excel('f3.xlsx')
        m=len(data.axes[0])
        pd.options.display.max_rows = 999
        an = data['Y']
        dna_sequence = an
        value = self.gain(m, dna_sequence)
        file = open(r"filename.txt")
        stext = file.read()
        key = word_tokenize(stext)
        for k,v in zip(key,value):
            dic.setdefault(k,[]).append(v)   
        no = self.returnum()
        N = int(no)
        sd = dict(sorted([(i,list(set(j))) for i, j in dic.items()], key=operator.itemgetter(1), reverse=True))
        output = dict(itertools.islice(sd.items(), N))
        print("Information Gain of top ",N," words are:", "\n")
        print(output)
        with open('n.txt', 'w') as f:
            f.writelines("%s" % N)
        
        
    def gain(self, m, dna_sequence):
        lists = []
        twl=[]
        fm=0
        data = pd.read_excel('f3.xlsx')
        df = pd.DataFrame(data, columns = ['X'])
        file = open(r"filename.txt")
        st = file.read()
        length = len(st)
        liststem = word_tokenize(st)
        for j,y in zip(liststem,range(length)):
            for i in range(m):
                d1 = df.iloc[i][0]
                tokenizer = RegexpTokenizer(r'\w+')
                data1 = tokenizer.tokenize(d1)
                for k in data1:
                    ps = WordNetLemmatizer()
                    hl = ps.lemmatize(k, self.get_wordnet_pos(k))
                    h = hl.lower()
                    po = PorterStemmer()
                    stt = po.stem(k)
                    st = stt.lower()
                    if ((j==h) or (j==st)) :
                        a = 1
                        break
                    else:
                        a = 0

                lists.append(a)
            twl.append(lists)
            lists= []
        fm= (np.transpose(twl))
        d={}
        info = []
        Weighted_Entropy = 0
        total_entropy =self.Entropy(dna_sequence)
        for u,i in zip(range (length),liststem):
            res = [sub[u] for sub in fm]
            vals,counts= np.unique(res,return_counts=True)
            for k,v in zip(res,dna_sequence):
                d.setdefault(k,[]).append(v)
            for v in range(len(vals)):
                for key in d.keys():
                    if(vals[v]== key):
                        Weighted_Entropy += (counts[v]/np.sum(counts))*(self.Entropy(d[key]))

            Information_Gain = total_entropy - Weighted_Entropy
            info.append(Information_Gain)
            d = {}
            Weighted_Entropy = 0
        return info

    def Entropy(self, dna_sequence):
        elements,counts = np.unique(dna_sequence,return_counts = True)
        entropy = np.sum([(-counts[i]/np.sum(counts))*np.log2(counts[i]/np.sum(counts)) for i in range(len(elements))])
        return entropy
        
    def returnum(self):
        num = self.lineEdit.text()
        return num

    def get_wordnet_pos(self, word):
        tag = nltk.pos_tag([word])[0][1][0].upper()
        tag_dict = {"J": wordnet.ADJ,
                    "N": wordnet.NOUN,
                    "V": wordnet.VERB,
                    "R": wordnet.ADV}
        
        return tag_dict.get(tag, wordnet.NOUN)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    New_Window4 = QtWidgets.QMainWindow()
    ui = Ui_New_Window4()
    ui.setupUi(New_Window4)
    New_Window4.show()
    sys.exit(app.exec_())

