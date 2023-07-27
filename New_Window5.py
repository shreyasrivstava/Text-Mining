# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'New_Window3.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import sys
import pandas as pd
import math
import nltk
import numpy as np
import operator
import itertools
from nltk.tokenize import RegexpTokenizer
from nltk.corpus import wordnet
from nltk.stem.porter import PorterStemmer
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
class Stream(QtCore.QObject):
    newText = QtCore.pyqtSignal(str)

    def write(self, text):
        self.newText.emit(str(text))

class Ui_New_Window5(QtCore.QObject):
   
    def openWindow_2(self):
        f1=open('filename_4.txt','r')
        f2=open('filename.txt','w')
        f3=f1.read()
        f2.write(f3)
        from New_Window_4 import Ui_New_Window_4
        self.window = QtWidgets.QMainWindow()
        #self.window.termination()
        self.ui = Ui_New_Window_4()
        self.ui.setupUi(self.window)


    def setupUi(self, New_Window5):
        New_Window5.setObjectName("New_Window5")
        New_Window5.showMaximized()
        New_Window5.setStyleSheet("background-color: black;")
        sys.stdout = Stream(newText=self.onUpdateText)
        self.centralwidget = QtWidgets.QWidget(New_Window5)
        self.centralwidget.setObjectName("centralwidget")
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(70, 120, 1050, 450))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setFamily("Cambria")
        self.textEdit.setFont(font)
        self.textEdit.setStyleSheet("background-color: white;")
        self.textEdit.setObjectName("textEdit")
        self.after = QtWidgets.QPushButton(self.centralwidget)
        self.after.setGeometry(QtCore.QRect(1130, 350, 130, 41))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        font.setPointSize(10)
        font.setFamily("Cambria")
        self.after.setFont(font)
        self.after.setStyleSheet("QPushButton""{""background-color : white;""}""QPushButton::pressed""{""background-color : aqua;""};")
        self.after.setObjectName("After")
        self.kill = QtWidgets.QPushButton(self.centralwidget)
        self.kill.setGeometry(QtCore.QRect(675, 680, 150, 41))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        font.setPointSize(10)
        font.setFamily("Cambria")
        self.kill.setFont(font)
        self.kill.setStyleSheet("QPushButton""{""background-color : white;""border- 2px solid black;""}""QPushButton::pressed""{""background-color : aqua;""};")
        self.kill.setObjectName("Close")
        self.Previous = QtWidgets.QPushButton(self.centralwidget)
        self.Previous.setGeometry(QtCore.QRect(440, 680, 150, 41))
        self.Previous.setStyleSheet("QPushButton""{""background-color : white;""}""QPushButton::pressed""{""background-color : aqua;""}")
        self.Previous.setFont(font)
        self.Previous.setObjectName("Previous")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(250, 30, 800, 71))
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
        
        New_Window5.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(New_Window5)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        New_Window5.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(New_Window5)
        self.statusbar.setObjectName("statusbar")
        New_Window5.setStatusBar(self.statusbar)
        self.after.clicked.connect(self.loadfile)
        self.kill.clicked.connect(self.Close_program)
        self.Previous.clicked.connect(self.openWindow_2)
        self.retranslateUi(New_Window5)
        QtCore.QMetaObject.connectSlotsByName(New_Window5)

    def retranslateUi(self, New_Window5):
        _translate = QtCore.QCoreApplication.translate
        New_Window5.setWindowTitle(_translate("New_Window5", "Tf-idf"))
        self.after.setText(_translate("New_Window5", "Calculate Tf-idf"))
        self.kill.setText(_translate("New_Window5", "Close Window"))
        self.Previous.setText(_translate("New_Window5", "<<Previous"))
        self.label.setText(_translate("New_Window5", "Pre-Processing->Tokenization->Stopword Removal-> Stemming/Lemmatization->InfoGain->Tf-idf-Calculation"))
         
    def onUpdateText(self, text):
        cursor = self.textEdit.textCursor()
        cursor.movePosition(QtGui.QTextCursor.End)
        cursor.insertText(text)
        self.textEdit.setTextCursor(cursor)
        self.textEdit.ensureCursorVisible()

    def Close_program(self):
        sys.exit()

    def loadfile(self):
       
        data = pd.read_excel('f3.xlsx')
        df = pd.DataFrame(data, columns = ['X'])
        m=len(data.axes[0])
        pd.options.display.max_rows = 999
        an = data['Y']
        dna_sequence = an
        tfidf = {}
        print()
        stemmed_list = self.sort()
        print()
        print("\nTf-idf of the words are:")
        print()
        liststem = list(stemmed_list.keys())
        numofWords = dict.fromkeys(liststem,0)
        
        for i in range(m):
            d1 = df.iloc[i][0]
            tokenizer = RegexpTokenizer(r'\w+')
            data1 = tokenizer.tokenize(d1)
    
            for word in data1:
                ps = WordNetLemmatizer()
                h1 = ps.lemmatize(word, self.get_wordnet_pos(word))
                h = h1.lower()
                po = PorterStemmer()
                st = po.stem(word)
                st = st.lower()
                for x in liststem:  
                    if ((h == x) or (st == x)):

                        numofWords[h] +=1
                
            tf = self.computeTF(numofWords, data1)
            idfs = self.idf(df, m, liststem)
            tfidf =self.computeTFIDF(tf, idfs)
      
            numofWords = dict.fromkeys(liststem,0)
            ngo = pd.DataFrame(tfidf,index=[i])
            #ngo2 = pd.DataFrame(tfidf, index=[i]) 
            #print(ngo)
            #ngo.to_excel('/Final.xlsx',df)
            print(ngo)
            ngo.to_csv('filename2.txt',mode='a',sep=',')
            #with pd.ExcelWriter('Final.xlsx') as writer:  
                 #ngo2.to_excel(writer.append())
      

            
        f1 = open("filename2.txt", "r") 
        f2 =  pd.DataFrame(f1)
        f2.to_excel('.Final.xlsx', index=False)  
        
    def sort(self):
        
        dic = {}
        data = pd.read_excel('f3.xlsx')
        m=len(data.axes[0])
        pd.options.display.max_rows = 999
        an = data['Y']
        dna_sequence = an
        value = self.gain(m, dna_sequence)
        file = open(r"filename.txt")
        st = file.read()
        key = word_tokenize(st)
        for k,v in zip(key,value):
            dic.setdefault(k,[]).append(v)
        N = self.returnnum()
        sd = dict(sorted([(i,list(set(j))) for i, j in dic.items()], key=operator.itemgetter(1), reverse=True))
        output = dict(itertools.islice(sd.items(), N))
        print("Information Gain of top ",N," words are:", "\n")
        print(output)
        print()
        return output
    
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
    
    def computeTF(self, wordDict, bagsofwords):
        tfDict = {}
        bagOfWordsCount = len(bagsofwords)
        for word,count in wordDict.items():
            
            tfDict[word] = count / float(bagOfWordsCount)

        return tfDict
    
    def idf(self, df, m, liststem):
        documents = []
        numofWords = dict.fromkeys(liststem,0)

        for i in range(m):
            d1 = df.iloc[i][0]
            tokenizer = RegexpTokenizer(r'\w+')
            data1 = tokenizer.tokenize(d1)

            for word in data1:
                ps = WordNetLemmatizer()
                h1 = ps.lemmatize(word, self.get_wordnet_pos(word))
                h = h1.lower()
                po = PorterStemmer()
                stt = po.stem(word)
                st = stt.lower()
            
                for x in liststem:
                
                    if ((h == x) or (st ==x)):

                       numofWords[h] +=1

            documents.append(numofWords)
            numofWords = dict.fromkeys(liststem,0)

        N = len(documents)
        idfDict = dict.fromkeys(liststem,0)
        for document in documents:
            for word, val in document.items():
                if val > 0:
                  idfDict[word] += 1

        for word, val in idfDict.items():
            idfDict[word] = math.log(N / float(val))

        return idfDict

    def computeTFIDF(self, tfBagOfWords, idfs):
       
        tfidf = {}
        for word, val in tfBagOfWords.items():
            tfidf[word] = val * idfs[word]
        return tfidf
    
    def get_wordnet_pos(self, word):
        tag = nltk.pos_tag([word])[0][1][0].upper()
        tag_dict = {"J": wordnet.ADJ,
                    "N": wordnet.NOUN,
                    "V": wordnet.VERB,
                    "R": wordnet.ADV}
        
        return tag_dict.get(tag, wordnet.NOUN)
    
    def returnnum(self):
        file = open(r"n.txt")
        num = file.read()
        no = int(num)
        file.close()
        return no
    
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    New_Window5 = QtWidgets.QMainWindow()
    ui = Ui_New_Window5()
    ui.setupUi(New_Window5)
    New_Window5.show()
    sys.exit(app.exec_())

