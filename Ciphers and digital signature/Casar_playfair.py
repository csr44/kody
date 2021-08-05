# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'playfair.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
c = 1
zasifrovany_text = ""
odsifrovany_text = ""
global_matica = []
kluc = ""
vstup=""
class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(403, 238)
        self.CZSK = QtWidgets.QRadioButton(Dialog)
        self.CZSK.setGeometry(QtCore.QRect(347, 20, 51, 17))
        self.CZSK.setChecked(False)
        self.CZSK.setObjectName("CZSK")
        self.EN = QtWidgets.QRadioButton(Dialog)
        self.EN.setGeometry(QtCore.QRect(310, 20, 31, 17))
        self.EN.setObjectName("EN")
        self.buttonzasifruj = QtWidgets.QPushButton(Dialog)
        self.buttonzasifruj.setGeometry(QtCore.QRect(210, 50, 75, 23))
        self.buttonzasifruj.setObjectName("buttonzasifruj")
        self.buttondesifruj = QtWidgets.QPushButton(Dialog)
        self.buttondesifruj.setGeometry(QtCore.QRect(290, 50, 75, 23))
        self.buttondesifruj.setObjectName("buttondesifruj")
        self.textprevstup = QtWidgets.QLineEdit(Dialog)
        self.textprevstup.setGeometry(QtCore.QRect(90, 20, 211, 21))
        self.textprevstup.setObjectName("textprevstup")
        self.textprekluc = QtWidgets.QLineEdit(Dialog)
        self.textprekluc.setGeometry(QtCore.QRect(90, 50, 111, 20))
        self.textprekluc.setObjectName("textprekluc")
        self.infovstup = QtWidgets.QLabel(Dialog)
        self.infovstup.setGeometry(QtCore.QRect(10, 20, 71, 16))
        self.infovstup.setObjectName("infovstup")
        self.infokluc = QtWidgets.QLabel(Dialog)
        self.infokluc.setGeometry(QtCore.QRect(60, 50, 21, 16))
        self.infokluc.setObjectName("infokluc")
        self.line = QtWidgets.QFrame(Dialog)
        self.line.setGeometry(QtCore.QRect(0, 70, 401, 16))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.vystup = QtWidgets.QLabel(Dialog)
        self.vystup.setGeometry(QtCore.QRect(10, 85, 41, 16))
        self.vystup.setObjectName("vystup")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(270, 85, 41, 16))
        self.label_2.setObjectName("label_2")
        self.line_2 = QtWidgets.QFrame(Dialog)
        self.line_2.setGeometry(QtCore.QRect(250, 80, 20, 161))
        self.line_2.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.textEdit = QtWidgets.QTextEdit(Dialog)
        self.textEdit.setGeometry(QtCore.QRect(10, 100, 241, 131))
        self.textEdit.setObjectName("textEdit")
        self.textEdit.setReadOnly(True)
        self.matica_zobrazenie = QtWidgets.QTableWidget(Dialog)
        self.matica_zobrazenie.setGeometry(QtCore.QRect(270, 100, 121, 131))
        self.matica_zobrazenie.setAutoScroll(False)
        self.matica_zobrazenie.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.matica_zobrazenie.setTabKeyNavigation(False)
        self.matica_zobrazenie.setProperty("showDropIndicator", False)
        self.matica_zobrazenie.setDragDropOverwriteMode(False)
        self.matica_zobrazenie.setSelectionMode(QtWidgets.QAbstractItemView.NoSelection)
        self.matica_zobrazenie.setRowCount(5)
        self.matica_zobrazenie.setColumnCount(5)
        self.matica_zobrazenie.setObjectName("matica_zobrazenie")
        self.matica_zobrazenie.horizontalHeader().setDefaultSectionSize(20)
        self.matica_zobrazenie.verticalHeader().setDefaultSectionSize(20)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

        self.CZSK.clicked.connect(self.jazykSK)
        self.EN.clicked.connect(self.jazykEN)
        self.buttonzasifruj.clicked.connect(self.vygeneruj)
        self.buttondesifruj.clicked.connect(self.vygeneruj1)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.CZSK.setText(_translate("Dialog", "CZ/SK"))
        self.EN.setText(_translate("Dialog", "EN"))
        self.buttonzasifruj.setText(_translate("Dialog", "Zasifruj"))
        self.buttondesifruj.setText(_translate("Dialog", "Desifruj"))
        self.infovstup.setText(_translate("Dialog", "Text pre vstup"))
        self.infokluc.setText(_translate("Dialog", "Kluc"))
        self.vystup.setText(_translate("Dialog", "Vystup:"))
        self.label_2.setText(_translate("Dialog", "Matica:"))

    def vygeneruj(self):
        global kluc, vstup
        kluc = self.textprekluc.text()
        vstup = self.textprevstup.text()
        zasifruj(vstup, kluc)
        self.textEdit.setText(zasifrovany_text)
        for e,ee in enumerate(global_matica):
            for i,j in enumerate(ee):
                self.matica_zobrazenie.setItem(e,i,QtWidgets.QTableWidgetItem(j))

    def vygeneruj1(self):
        global kluc, vstup
        kluc = self.textprekluc.text()
        vstup = self.textprevstup.text()
        desifruj(vstup, kluc)
        self.textEdit.setText(odsifrovany_text)
        for e,ee in enumerate(global_matica):
            for i,j in enumerate(ee):
                self.matica_zobrazenie.setItem(e,i,QtWidgets.QTableWidgetItem(j))


    def jazykSK(self):
        global c
        c = 1

    def jazykEN(self):
        global c
        c = 2

def zmaz_duplikat(par1):
    nove = ""
    for m in par1:
        if m not in nove:
            nove = nove + m
    return nove
def os_matica(kluc):
    global global_matica
    matica =[]
    for e in zmaz_duplikat(OsetriKluc(kluc)):
        matica.append(e)
    if c==1:
        abeceda = "ABCDEFGHIJKLMNOPQRSTUVXYZ"
    else:
        abeceda = "ABCDEFGHIKLMNOPQRSTUVWXYZ"

    for e in abeceda:
        if e not in matica:
            matica.append(e)
    global_matica=patice(matica)
    return patice(matica)
def OsetriKluc(kluc):
    diakritika = {"Á" :"A", "Č" :"C", "É" :"E", "Ě" :"E", "Ď" :"D", "Í" :"I", "Ň" :"N", "Ó" :"O", "Ř" :"R", "Š" :"S", "Ť" :"T", "Ů" :"U", "Ú" :"U", "Ý" :"Y", "Ž" :"Z"}
    osetrenyKluc = ""
    kluc = kluc.upper()
    validniAbeceda = ["A" ,"B" ,"C" ,"D" ,"E" ,"F" ,"G" ,"H" ,"I" ,"J" ,"K" ,"L" ,"M" ,"N" ,"O" ,"P" ,"Q" ,"R" ,"S","T" ,"U" ,"V" ,"W","X" ,"Y" ,"Z"]

    for i in kluc:
        if validniAbeceda.count(i) > 0:
            osetrenyKluc += i
        else:
            try:
                osetrenyKluc += diakritika[i]
            except:
                pass
    if c==1:
        if 'W' in osetrenyKluc:
            osetrenyKluc=osetrenyKluc.replace('W','V')
    if c==2:
        if 'J' in osetrenyKluc:
            osetrenyKluc=osetrenyKluc.replace('J','I')
    return osetrenyKluc
def miesto(par):
    m=(par +1)% 5
    return m
def miesto1(par):
    m=(par -1)% 5
    return m
def uprav_text(par1):
    nove=[]
    for m in par1:
        nove.append(m)
    for i in range(0,len(nove) - 1,2):
        if nove[i] == nove[i + 1]:
            nove.insert(i + 1, 'X')
    if (len(nove))%2==1:
        if nove[-1]=="X":
            nove.append("Q")
        else:
            nove.append("X")
    return nove
def dvojice(par1):
    o = []
    while par1:
        o.append(par1[:2])
        par1 = par1[2:]
    return o
def pozicia1(matica,pismeno):
    for i, e in enumerate(matica):
        for j, ee in enumerate(e):
            if pismeno in ee:
                return [i,j]
def patice(par1):
    o = []
    while par1:
        o.append(par1[:5])
        par1 = par1[5:]
    return o
def zasifruj(vstup_text,kluc):
    global zasifrovany_text
    sprava01=dvojice(uprav_text(Osetrivstup(vstup_text,c)))#
    matica=os_matica(kluc)
    sifra=[]
    for n in sprava01:
        riadok1,stlpec1=pozicia1(matica,n[0])
        riadok2,stlpec2=pozicia1(matica,n[1])
        if riadok1==riadok2:
            sifra.append(matica[riadok1][miesto(stlpec1)])
            sifra.append(matica[riadok1][miesto(stlpec2)])
        elif stlpec1==stlpec2:
            sifra.append(matica[miesto(riadok1)][stlpec1])
            sifra.append(matica[miesto(riadok2)][stlpec2])
        else:
            sifra.append(matica[riadok1][stlpec2])
            sifra.append(matica[riadok2][stlpec1])
    sifra=''.join(sifra)
    sifra=' '.join([sifra[i:i+5] for i in range(0, len(sifra), 5)])
    zasifrovany_text=sifra
    return sifra
def desifruj(sprava,kluc):
    global odsifrovany_text
    sprava=dvojice(Osetrivstup_desifruj(sprava))  #
    matica=os_matica(kluc)
    sifra=[]
    for n in sprava:
        riadok1,stlpec1=pozicia1(matica,n[0])
        riadok2,stlpec2=pozicia1(matica,n[1])
        if riadok1==riadok2:
            sifra.append(matica[riadok1][miesto1(stlpec1)])
            sifra.append(matica[riadok1][miesto1(stlpec2)])
        elif stlpec1==stlpec2:
            sifra.append(matica[miesto1(riadok1)][stlpec1])
            sifra.append(matica[miesto1(riadok2)][stlpec2])
        else:
            sifra.append(matica[riadok1][stlpec2])
            sifra.append(matica[riadok2][stlpec1])
    sifra=''.join(sifra)
    sifra=sifra.replace('MEZERA',' ')
    sifra=sifra.replace('POMLCKA','_')
    sifra = sifra.replace('MINUS', '-')
    sifra = sifra.replace('PLUS', '+')
    sifra = sifra.replace('DELENO', '/')
    sifra = sifra.replace('BODKA', '.')
    sifra = sifra.replace('HVEZDA', '*')
    sifra = sifra.replace('OTAZNIK', '?')
    sifra = sifra.replace('PERCENT', '%')
    sifra = sifra.replace('VYKRIC', '!')
    sifra = sifra.replace('CIARKA', ',')
    odsifrovany_text=sifra
    return sifra
def Osetrivstup_desifruj(text):
    diakritika = {"Á" :"A", "Č" :"C", "É" :"E", "Ě" :"E", "Ď" :"D", "Í" :"I", "Ň" :"N", "Ó" :"O", "Ř" :"R", "Š" :"S", "Ť" :"T", "Ů" :"U", "Ú" :"U", "Ý" :"Y", "Ž" :"Z"}
    osetrenyvstup = ""
    text = text.upper()
    validniAbeceda = ["A" ,"B" ,"C" ,"D" ,"E" ,"F" ,"G" ,"H" ,"I" ,"J" ,"K" ,"L" ,"M" ,"N" ,"O" ,"P" ,"Q" ,"R" ,"S","T" ,"U" ,"V" ,"W","X" ,"Y" ,"Z"]
    for i in text:
        if validniAbeceda.count(i) > 0:
            osetrenyvstup += i
        else:
            try:
                osetrenyvstup += diakritika[i]
            except:
                pass
    return osetrenyvstup
def Osetrivstup(text, czen):
    diakritika = {"Á" :"A", "Č" :"C", "É" :"E", "Ě" :"E", "Ď" :"D", "Í" :"I", "Ň" :"N", "Ó" :"O", "Ř" :"R", "Š" :"S", "Ť" :"T", "Ů" :"U", "Ú" :"U", "Ý" :"Y", "Ž" :"Z"}
    znaky={" " :"MEZERA", "_" :"POMLCKA", "-" :"MINUS", "+" :"PLUS", "/" :"DELENO", "." :"BODKA","*":"HVEZDA","?":"OTAZNIK","%":"PERCENT","!":"VYKRIC",",":"CIARKA"}
    osetrenyvstup = ""
    text = text.upper()
    validniAbeceda=[]
    if czen == 1:
        validniAbeceda = ["A" ,"B" ,"C" ,"D" ,"E" ,"F" ,"G" ,"H" ,"I" ,"J" ,"K" ,"L" ,"M" ,"N" ,"O" ,"P" ,"Q" ,"R" ,"S"
                          ,"T" ,"U" ,"V" ,"X" ,"Y" ,"Z"]
        text=text.replace("W", "V")

    if czen == 2:
        validniAbeceda = ["A" ,"B" ,"C" ,"D" ,"E" ,"F" ,"G" ,"H" ,"I" ,"K" ,"L" ,"M" ,"N" ,"O" ,"P" ,"Q" ,"R" ,"S" ,"T"
                          ,"U" ,"V" ,"W" ,"X" ,"Y" ,"Z"]
        text=text.replace("J", "I")
    for i in text:
        if validniAbeceda.count(i) > 0:
            osetrenyvstup += i
        else:
            try:
                osetrenyvstup += diakritika[i]
            except:
                try:
                    osetrenyvstup += znaky[i]
                except:
                    pass
    return osetrenyvstup
def okno():
    if __name__ == "__main__":
        import sys
        app = QtWidgets.QApplication(sys.argv)
        Dialog = QtWidgets.QDialog()
        ui = Ui_Dialog()
        ui.setupUi(Dialog)
        Dialog.setWindowTitle("Playfair_Casar")
        Dialog.show()
        sys.exit(app.exec_())
okno()
