# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'New_Window.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import *
from PyQt5.QtCore import *
from New_Window_3 import Ui_Main_Window_3
from tkinter import *
from tkinter.ttk import *
#tkinter window
#self.base = Tk()
import sys
class Stream(QtCore.QObject):
    newText = QtCore.pyqtSignal(str)

    def write(self, text):
        self.newText.emit(str(text))

class Ui_New_Window(QObject):
    def openWindow(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_Main_Window_3()
        self.ui.setupUi(self.window)
        self.window.show()

    def openWindow_2(self):
        
        from Home_page import Ui_MainWindow
        self.window = QtWidgets.QMainWindow()
        #self.window.termination()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self.window)
        self.refreshAll()
        
        #self.window.close()
        
   

      

    def setupUi(self, New_Window):
        New_Window.setObjectName("New_Window")
        New_Window.showMaximized()
        New_Window.setStyleSheet("background-image: url(hp3.jpg)")
        sys.stdout = Stream(newText=self.onUpdateText)
        self.centralwidget = QtWidgets.QWidget(New_Window)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(500, 40, 691, 28))
        font = QtGui.QFont()
        font.setFamily("Cambria")
        font.setPointSize(20)
        font.setBold(True)
        font.setItalic(True)
        font.setUnderline(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet("color: white;")
        self.label.setObjectName("label")
        #self.label_2 = QtWidgets.QLabel(self.centralwidget)
        #self.label_2.setGeometry(QtCore.QRect(60, 80, 651, 61))
        font = QtGui.QFont()
        font.setFamily("Cambria")
        font.setPointSize(14)
        font.setItalic(True)
        #self.label_2.setFont(font)
        #self.label_2.setScaledContents(True)
        #self.label_2.setWordWrap(True)
        #self.label_2.setStyleSheet("color: white;")
        #self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(80, 170, 181, 41))
        font = QtGui.QFont()
        font.setFamily("Cambria")
        font.setPointSize(18)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("color: white;")
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(80, 200, 101, 41))
        font = QtGui.QFont()
        font.setFamily("Cambria")
        font.setPointSize(18)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("color: white;")
        self.label_4.setObjectName("label_4")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(300, 170, 700, 41))
        self.lineEdit.setStyleSheet("Background-color : white;" )
        self.lineEdit.setStyleSheet("background-color: white;")
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setFamily("Cambria")
        self.lineEdit.setFont(font)
        self.lineEdit.setObjectName("lineEdit")
        self.Output = QtWidgets.QTextEdit(self.centralwidget)
        self.Output.setGeometry(QtCore.QRect(300, 220, 700, 380))
        self.Output.setStyleSheet("background-color: white;")
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setFamily("Cambria")
        self.Output.setFont(font)
        self.Output.setObjectName("Output")
        self.BROWSE = QtWidgets.QPushButton(self.centralwidget)
        self.BROWSE.setGeometry(QtCore.QRect(1050, 170, 176, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setWeight(75)
        font.setFamily("Cambria")
        self.BROWSE.setFont(font)
        self.BROWSE.setStyleSheet("QPushButton""{""background-color : white;""}""QPushButton::pressed""{""background-color : aqua;""}")
        self.BROWSE.setObjectName("BROWSE")
        self.LC= QtWidgets.QPushButton(self.centralwidget)
        self.LC.setStyleSheet("color: white;")
        self.LC.setGeometry(QtCore.QRect(1050, 250, 176, 41))
        self.LC.setFont(font)
        self.LC.setStyleSheet("QPushButton""{""background-color : white;""}""QPushButton::clicked""{""background-color : aqua;""}")
        self.LC.setObjectName("LC")
        self.PR= QtWidgets.QPushButton(self.centralwidget)
        self.PR.setGeometry(QtCore.QRect(1050, 320, 176, 41))
        self.PR.setFont(font)
        self.PR.setStyleSheet("QPushButton""{""background-color : white;""}""QPushButton::pressed""{""background-color : aqua;""}")
        self.PR.setObjectName("PR")
        self.NAR = QtWidgets.QRadioButton(self.centralwidget)
        self.NAR.setGeometry(QtCore.QRect(1050, 390, 186, 41))
        self.NR = QtWidgets.QRadioButton(self.centralwidget)
        self.NR.setGeometry(QtCore.QRect(1050, 460, 176, 41))
        self.NAR.setFont(font)
        self.NAR.setStyleSheet("color: white")
        self.NAR.setObjectName("NAR")
        self.NR.setFont(font)
        self.NR.setStyleSheet("color: white")
        self.NR.setObjectName("NR")
        self.WSR = QtWidgets.QPushButton(self.centralwidget)
        self.WSR.setGeometry(QtCore.QRect(1050, 530, 176, 41))
        self.WSR.setFont(font)
        self.WSR.setStyleSheet("QPushButton""{""background-color : white;""}""QPushButton::pressed""{""background-color : aqua;""}")
        self.WSR.setObjectName("WSR")
        #self.SWR = QtWidgets.QPushButton(self.centralwidget)
        #self.SWR.setGeometry(QtCore.QRect(600, 450, 171, 31))
        #self.SWR.setFont(font)
        #self.SWR.setObjectName("SWR")
        self.Next = QtWidgets.QPushButton(self.centralwidget)
        self.Next.setGeometry(QtCore.QRect(675, 680, 150, 41))
        self.Next.setStyleSheet("QPushButton""{""background-color : white;""}""QPushButton::pressed""{""background-color : aqua;""}")
        self.Next.setFont(font)
        self.Next.setObjectName("Next")
        self.Previous = QtWidgets.QPushButton(self.centralwidget)
        self.Previous.setGeometry(QtCore.QRect(440, 680, 150, 41))
        self.Previous.setStyleSheet("QPushButton""{""background-color : white;""}""QPushButton::pressed""{""background-color : aqua;""}")
        self.Previous.setFont(font)
        self.Previous.setObjectName("Previous")
        New_Window.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(New_Window)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        New_Window.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(New_Window)
        self.statusbar.setObjectName("statusbar")
        New_Window.setStatusBar(self.statusbar)

        self.BROWSE.clicked.connect(self.BrowseSlot)
        self.WSR.clicked.connect(self.wsr)
        self.LC.clicked.connect(self.lc)
        self.PR.clicked.connect(self.pr)
        self.NAR.toggled.connect(self.nar)
        self.NR.toggled.connect(self.nr)
        #self.SWR.clicked.connect(self.swr)
        #self.Token.clicked.connect(self.tokenization)
        self.lineEdit.returnPressed.connect(self.returnedPressedSlot)
        self.Next.clicked.connect(self.openWindow)
        self.Previous.clicked.connect(self.openWindow_2)
        self.retranslateUi(New_Window)
        QtCore.QMetaObject.connectSlotsByName(New_Window)
        

    def retranslateUi(self, New_Window):
        _translate = QtCore.QCoreApplication.translate
        New_Window.setWindowTitle(_translate("New_Window", "MainWindow"))
        self.label.setText(_translate("New_Window", "Pre-Processing->Tokenization"))
        self.label_3.setText(_translate("New_Window", "Enter FileName :"))
        self.label_4.setText(_translate("New_Window", "Output :"))
        self.BROWSE.setText(_translate("New_Window", "Browse"))
        self.LC.setText(_translate("New_Window", "Convert to LowerCase"))
        self.PR.setText(_translate("New_Window", "Remove Punctuations"))
        self.NAR.setText(_translate("New_Window", "Remove Non Alpha-Numerics"))
        self.NR.setText(_translate("New_Window", "Remove Non Alphabetics"))
        self.WSR.setText(_translate("New_Window", "Remove Multi-Whitespaces"))
        #self.SWR.setText(_translate("New_Window", "Remove Stop-Words"))
        #self.Token.setText(_translate("New_Window", "Tokens"))
        self.Next.setText(_translate("New_Window", "Next>>"))
        self.Previous.setText(_translate("New_Window", "<<Previous"))

    def onUpdateText(self, text):
        cursor = self.Output.textCursor()
        cursor.movePosition(QtGui.QTextCursor.End)
        cursor.insertText(text)
        self.Output.setTextCursor(cursor)
        self.Output.ensureCursorVisible()

    def __del__(self):
        sys.stdout = sys.__stdout__


    def isValid( self, fileName ):
        '''
        returns True if the file exists and can be
        opened.  Returns False otherwise.
        '''
        try: 
            file = open( fileName, 'rb' )
            file.close()
            return True
        except:
            return False
    
    #def OpenClick(self,filename):
        
        # load data     
        #file = open(r"C:\Users\ujjwal\Documents\agenda.txt")
        #file = open(fileName)
        #text = file.read()
        #file.close()
        #print("DATA FILE CONTENTS")
        #print(text)
        #print()
        #print("_TOKENIZATION_")
        #print()
        # split into words
    #def tokenization(self,filename) :
        #from nltk.tokenize import word_tokenize
        #import pandas as pd
        #print("_TOKENIZED_")
        #print()
        #file = open(self.fileName, 'rb')
        #tex = pd.read_excel(file)
        #df = pd.DataFrame(data=tex).T
        #s = df.to_csv()
        #print(tex)
        #file.close()
        #text = tex.values.tolist()
        #self.tokens = word_tokenize(s)
        #print(self.tokens[:300])
        # convert to lower case
        

    def lc(self,filename) :
        
        #print(tex)
        self.s = self.s.lower()
        print()
        print("_Converted To Lower Case_")
        print()
        print("".join(self.s))
        # remove punctuation from each word
        stdout = sys.stdout
        sys.stdout=open('filename.txt','w')
        print(self.s)
        sys.stdout=stdout
        f1=open('filename.txt','r')
        f2=open('filename_2.txt','w')
        f3=f1.read()
        f2.write(f3)
        
        
        
            

    def pr(self,token) :
      
        import string
        table = str.maketrans('', '', string.punctuation)
        #[w.translate(table) for w in self.token]
        
        self.s = self.s.translate(table)
        print()
        print("_Punctuations Removed_")
        print()
        print(self.s)
        stdout = sys.stdout
        sys.stdout=open('filename.txt','w')
        print(self.s)
        sys.stdout=stdout
        f1=open('filename.txt','r')
        f2=open('filename_2.txt','w')
        f3=f1.read()
        f2.write(f3)
        
        
            
 
    def nar(self, selected) :
        #word for word in self.stripped if word.isalpha()
        if selected :
            import re
            
            #self.stripped = re.sub(r'[^a-zA-Z]', " ", self.stripped)
            self.s = re.sub(r'[\W_]+', " ",self.s)
            #self.word  = alphanumeric_string = " ".join(self.words)
            print()
            print("_Non Alpha-Numeric Characters Removed_")
            print()
            print(self.s)
            stdout = sys.stdout
            sys.stdout=open('filename.txt','w')
            print(self.s)
            sys.stdout=stdout
            f1=open('filename.txt','r')
            f2=open('filename_2.txt','w')
            f3=f1.read()
            f2.write(f3)
            #else:
                #words = [word for word in stripped]
            #filter out stop words
            
        
               

    def nr(self, selected) :
        if selected :
            import re
            
            self.s = re.sub(r'[^a-zA-Z]', " ", self.s)
            print()
            print("_Non Alphabetic Characters Removed_")
            print()
            print(self.s)
            stdout = sys.stdout
            sys.stdout=open('filename.txt','w')
            print(self.s)
            sys.stdout=stdout
            f1=open('filename.txt','r')
            f2=open('filename_2.txt','w')
            f3=f1.read()
            f2.write(f3)
        
       

    def wsr(self) :
        import re
        
        self.s = re.sub(' +',' ',self.s)
        print()
        print('_White Spaces Removed_')
        print()
        print(self.s)
        stdout = sys.stdout
        sys.stdout=open('filename.txt','w')
        print(self.s)
        sys.stdout=stdout
        f1=open('filename.txt','r')
        f2=open('filename_2.txt','w')
        f3=f1.read()
        f2.write(f3)
        

         

    #def swr(self) :
        #from gensim.parsing.preprocessing import remove_stopwords
        #[w for w in self.words if not w in stop_words]
        #import nltk
        #from nltk.corpus import stopwords
        #from nltk.tokenize import word_tokenize
        #stop_words = nltk.corpus.stopwords.words('english')
        #self.word = [w for w in self.w if not w in stop_words]
        #text_tokens = word_tokenize(self.w)
        #newStopWords = ['shall','should','could','could not','should not','would','would not']
        #stop_words.extend( newStopWords)
        #tokens_without_sw = [word for word in text_tokens if not word in stop_words]
        #tokens_without_sw = " ".join(tokens_without_sw)
        #print()
        #print("_Stop Words Removed_")
        #print()
        #print(tokens_without_sw)
        #with open('filename.txt', 'w') as f:
            #sys.stdout = f # Change the standard output to the file we created.
            #print(tokens_without_sw)
            #sys.stdout = sys.stdout

        


    def setFileName( self, fileName ):
        '''
        sets the member fileName to the value of the argument
        if the file exists.  Otherwise resets both the filename
        and file contents members.
        '''
        import pandas as pd
        if self.isValid( fileName ):
            self.fileName = fileName
            #self.fileContents = open( fileName, 'r' ).read()
            self.fileContents = pd.read_excel( fileName )
        else:
            self.fileContents = ""
            self.fileName = ""
            
    def getFileName( self ):
        '''
        Returns the name of the file name member.
        '''
        return self.fileName

    def getFileContents( self ):
        '''
        Returns the contents of the file if it exists, otherwise
        returns an empty string.
        '''
        return self.fileContents

    def refreshAll( self ):
        '''
        Updates the widgets whenever an interaction happens.
        '''
        self.lineEdit.setText( self.getFileName() )

    @pyqtSlot( )
    def returnedPressedSlot( self ):
        fileName =  self.lineEdit.text()
        if self.isValid( fileName ):
            self.setFileName( self.lineEdit.text() )
            self.refreshAll()
        else:
            m = QtWidgets.QTextBrowser()
            m.setText("Invalid file name!\n" + fileName )

    @pyqtSlot( )
    def BrowseSlot( self ):
        import pandas as pd
        options = QtWidgets.QFileDialog.Options()
        options |= QtWidgets.QFileDialog.DontUseNativeDialog
        fileName, _ = QtWidgets.QFileDialog.getOpenFileName(
                        None,
                        "QFileDialog.getOpenFileName()",
                        "",
                        "All Files (*);;Python Files (*.py)",
                        options=options)
        

        if fileName:
            file = open(fileName,'r')
            self.setFileName( fileName )
            self.refreshAll()
            file = open(self.fileName, 'rb')
            tex = pd.read_excel(file)
           
            df = pd.DataFrame(tex, columns = ['X'])
            df2 = pd.DataFrame(tex)
            df2.to_excel('./f3.xlsx')
            df = df.set_index('X')
            self.s = df.to_csv()
            print("The Original file:\n")
            #print()
            #print((tex['X']).to_string(index=False))
            #print(df)
            df = pd.DataFrame(data=tex)
            self.s = df.to_csv(header= False, columns= ['X'], index=False)
            print(self.s)


            
            #import openpyxl as xl; 
  
# opening the source excel file 
            #filename = open(fileName)
            #wb1 = xl.load_workbook(filename) 
            #ws1 = wb1.worksheets[0] 
  
# opening the destination excel file  
            #filename1 =open(f3.xlsx)
            #wb2 = xl.load_workbook(filename1) 
            #ws2 = wb2.active 
  
# calculate total number of rows and  
# columns in source excel file 
            #mr = ws1.max_row 
            #mc = ws1.max_column 
  
# copying the cell values from source  
# excel file to destination excel file 
            #for i in range (1, mr + 1): 
                #for j in range (1, mc + 1): 
        # reading cell value from source excel file 
                    #c = ws1.cell(row = i, column = j) 
  
        # writing the read value to destination excel file 
                    #ws2.cell(row = i, column = j).value = c.value 
  
# saving the destination excel file 
            #wb2.save(str(filename1)) 
            

if __name__ == "__main__":
    import sys
    
    app = QtWidgets.QApplication(sys.argv)
    New_Window = QtWidgets.QMainWindow()
    stylesheet = """
    New_Window {
        background-image: url("hp.jpg"); 
        background-repeat: no-repeat; 
        background-position: center;
    }
""" 
    app.setStyleSheet(stylesheet)
    ui = Ui_New_Window()
    ui.setupUi(New_Window)
    New_Window.show()
    sys.exit(app.exec_())
    
