from PyQt5 import QtCore, QtGui, QtWidgets

dlzka_kluc=0
c=11
vystup=""
matica=[]
abeceda=""
import random
class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(683, 446)
        self.CZSK = QtWidgets.QRadioButton(Dialog)
        self.CZSK.setGeometry(QtCore.QRect(490, 50, 51, 17))
        self.CZSK.setChecked(False)
        self.CZSK.setObjectName("CZSK")
        self.EN = QtWidgets.QRadioButton(Dialog)
        self.EN.setGeometry(QtCore.QRect(450, 50, 31, 17))
        self.EN.setObjectName("EN")
        self.textprevstup = QtWidgets.QLineEdit(Dialog)
        self.textprevstup.setGeometry(QtCore.QRect(20, 30, 301, 21))
        self.textprevstup.setObjectName("textprevstup")
        self.infovstup = QtWidgets.QLabel(Dialog)
        self.infovstup.setGeometry(QtCore.QRect(20, 10, 51, 21))
        self.infovstup.setObjectName("infovstup")
        self.infokluc = QtWidgets.QLabel(Dialog)
        self.infokluc.setGeometry(QtCore.QRect(20, 60, 31, 16))
        self.infokluc.setObjectName("infokluc")
        self.vystup = QtWidgets.QLabel(Dialog)
        self.vystup.setGeometry(QtCore.QRect(20, 280, 41, 16))
        self.vystup.setObjectName("vystup")
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(20, 250, 201, 23))
        self.pushButton.setObjectName("pushButton")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(330, 130, 133, 16))
        self.label_3.setObjectName("label_3")
        self.prepinac_ad = QtWidgets.QSlider(Dialog)
        self.prepinac_ad.setGeometry(QtCore.QRect(450, 20, 81, 22))
        self.prepinac_ad.setMaximum(1)
        self.prepinac_ad.setOrientation(QtCore.Qt.Horizontal)
        self.prepinac_ad.setObjectName("prepinac_ad")
        self.label_5 = QtWidgets.QLabel(Dialog)
        self.label_5.setGeometry(QtCore.QRect(410, 20, 41, 20))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(Dialog)
        self.label_6.setGeometry(QtCore.QRect(540, 20, 41, 20))
        self.label_6.setObjectName("label_6")
        self.lineEdit = QtWidgets.QLineEdit(Dialog)
        self.lineEdit.setGeometry(QtCore.QRect(20, 80, 301, 21))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_2.setGeometry(QtCore.QRect(20, 300, 411, 20))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_3 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_3.setGeometry(QtCore.QRect(330, 161, 331, 20))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.pushButton_2 = QtWidgets.QPushButton(Dialog)
        self.pushButton_2.setGeometry(QtCore.QRect(180, 160, 141, 23))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(Dialog)
        self.pushButton_3.setGeometry(QtCore.QRect(20, 160, 141, 23))
        self.pushButton_3.setObjectName("pushButton_3")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(440, 190, 91, 20))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(330, 80, 111, 16))
        self.label_2.setObjectName("label_2")
        self.zost_pismena = QtWidgets.QLabel(Dialog)
        self.zost_pismena.setGeometry(QtCore.QRect(440, 75, 211, 31))
        self.zost_pismena.setText("")
        self.zost_pismena.setAlignment(QtCore.Qt.AlignCenter)
        self.zost_pismena.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByMouse|QtCore.Qt.TextSelectableByMouse)
        self.zost_pismena.setObjectName("zost_pismena")
        self.pushButton_4 = QtWidgets.QPushButton(Dialog)
        self.pushButton_4.setGeometry(QtCore.QRect(480, 132, 181, 23))
        self.pushButton_4.setObjectName("pushButton_4")
        self.tableWidget = QtWidgets.QTableWidget(Dialog)
        self.tableWidget.setGeometry(QtCore.QRect(440, 210, 201, 211))
        self.tableWidget.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tableWidget.setTabKeyNavigation(False)
        self.tableWidget.setProperty("showDropIndicator", False)
        self.tableWidget.setDragDropOverwriteMode(False)
        self.tableWidget.setSelectionMode(QtWidgets.QAbstractItemView.NoSelection)
        self.tableWidget.setCornerButtonEnabled(True)
        self.tableWidget.setRowCount(6)
        self.tableWidget.setColumnCount(6)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.horizontalHeader().setDefaultSectionSize(30)
        self.tableWidget.verticalHeader().setMinimumSectionSize(30)
        self.pushButton_5 = QtWidgets.QPushButton(Dialog)
        self.pushButton_5.setGeometry(QtCore.QRect(230, 250, 201, 23))
        self.pushButton_5.setObjectName("pushButton_5")

        self.prepinac_ad.valueChanged.connect(self.gen)
        self.EN.clicked.connect(self.jazykEN)
        self.CZSK.clicked.connect(self.jazykSK)
        self.pushButton_3.clicked.connect(self.generuj_ab)
        self.pushButton.clicked.connect(self.spus)
        self.pushButton_5.clicked.connect(self.spus0)
        self.pushButton_4.clicked.connect(self.aktua)
        self.pushButton_2.clicked.connect(self.uloz)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.CZSK.setText(_translate("Dialog", "CZ/SK"))
        self.EN.setText(_translate("Dialog", "EN"))
        self.infovstup.setText(_translate("Dialog", "Vstup:"))
        self.infokluc.setText(_translate("Dialog", "Kluc:"))
        self.vystup.setText(_translate("Dialog", "Vystup:"))
        self.pushButton.setText(_translate("Dialog", "Sifruj"))
        self.label_3.setText(_translate("Dialog", "Zadanie vlastnej abecedy:"))
        self.label_5.setText(_translate("Dialog", "ADFGX"))
        self.label_6.setText(_translate("Dialog", "ADFGVX"))
        self.pushButton_2.setText(_translate("Dialog", "Uloz vlastnu abecedu"))
        self.pushButton_3.setText(_translate("Dialog", "Generuj nahodnu abecedu"))
        self.label.setText(_translate("Dialog", "Aktualna matica:"))
        self.label_2.setText(_translate("Dialog", "Zostavajuce pismena:"))
        self.pushButton_4.setText(_translate("Dialog", "Aktualizuj"))
        self.pushButton_5.setText(_translate("Dialog", "Desifruj"))

    def uloz(self):
        global abeceda,matica
        ab = self.lineEdit_3.text()
        ab=OsetriKluc(ab)
        if c==2:
            if len(ab)==36:
                abeceda=ab
                self.zost_pismena.setText("Matica ulozena")
                matica=[]
                for e in abeceda:
                    matica.append(e)
                matica = sestice(matica)
            else:
                self.zost_pismena.setText("Nedokoncena matica")
        else:
            if len(ab)==25:
                abeceda=ab
                self.zost_pismena.setText("Matica ulozena")
                matica=[]
                for e in abeceda:
                    matica.append(e)
                matica = patice(matica)
            else:
                self.zost_pismena.setText("Nedokoncena matica")

    def aktua(self):
        ab=self.lineEdit_3.text()
        ab = OsetriKluc(ab)
        at=""
        if c == 11:
            at = "ABCDEFGHIJKLMNOPQRSTUVXYZ"
        if c == 12:
            at = "ABCDEFGHIKLMNOPQRSTUVWXYZ"
        if c == 2:
            at = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
        pismenka=""
        for z in at:
            if z not in ab:
                pismenka=pismenka+z
        self.zost_pismena.setText(pismenka)

    def gen(self):
        global c
        hodnota=self.prepinac_ad.value()
        if hodnota==0:
            c=11
            self.EN.setDisabled(False)
            self.CZSK.setDisabled(False)
        else:
            c=2
            self.EN.setDisabled(True)
            self.CZSK.setDisabled(True)


    def spus(self):
        text=self.textprevstup.text()
        key = self.lineEdit.text()
        if c==2:
            vyst=adfgvx(text,key)
            self.lineEdit_2.setText(vyst)
        else:
            vyst=adfgx(text,key)
            self.lineEdit_2.setText(vyst)

    def spus0(self):
        text=self.textprevstup.text()
        key = self.lineEdit.text()
        if c==2:
            vyst=adfgvx_desifruj(text,key)
            self.lineEdit_2.setText(vyst)
        else:
            vyst=adfgx_desifruj(text,key)
            self.lineEdit_2.setText(vyst)

    def jazykSK(self):
        global c
        c = 11

    def jazykEN(self):
        global c
        c = 12

    def generuj_ab(self):
        generuj_n_abecedu()
        l_abeceda=list(abeceda)
        manipul00 = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
        manipul00=list(manipul00)
        manipul00=sestice(manipul00)
        if c ==11:
            l_abeceda=patice(l_abeceda)
        if c ==12:
            l_abeceda=patice(l_abeceda)
        if c==2:
            l_abeceda=sestice(l_abeceda)
        for e,ee in enumerate(manipul00):
            for i,j in enumerate(ee):
                self.tableWidget.setItem(e,i,QtWidgets.QTableWidgetItem(' '))
        for e,ee in enumerate(l_abeceda):
            for i,j in enumerate(ee):
                self.tableWidget.setItem(e,i,QtWidgets.QTableWidgetItem(j))


def Osetrivstup_adfgx(text, czen):
    diakritika = {"Á" :"A", "Č" :"C", "É" :"E", "Ě" :"E", "Ď" :"D", "Í" :"I", "Ň" :"N", "Ó" :"O", "Ř" :"R", "Š" :"S", "Ť" :"T", "Ů" :"U", "Ú" :"U", "Ý" :"Y", "Ž" :"Z"}
    znaky={" " :"MEZERA", "_" :"POMLCKA", "-" :"MINUS", "+" :"PLUS", "/" :"DELENO", "." :"BODKA","*":"HVEZDA","?":"OTAZNIK","%":"PERCENT","!":"VYKRIC",",":"CIARKA"}
    osetrenyvstup = ""
    text = text.upper()
    if czen == 11:
        validniAbeceda = ["A" ,"B" ,"C" ,"D" ,"E" ,"F" ,"G" ,"H" ,"I" ,"J" ,"K" ,"L" ,"M" ,"N" ,"O" ,"P" ,"Q" ,"R" ,"S"
                          ,"T" ,"U" ,"V" ,"X" ,"Y" ,"Z"]
        text=text.replace("W", "V")
    else:
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

def Osetrivstup_adfgvx(text):
    diakritika = {"Á" :"A", "Č" :"C", "É" :"E", "Ě" :"E", "Ď" :"D", "Í" :"I", "Ň" :"N", "Ó" :"O", "Ř" :"R", "Š" :"S", "Ť" :"T", "Ů" :"U", "Ú" :"U", "Ý" :"Y", "Ž" :"Z"}
    znaky={" " :"MEZERA", "_" :"POMLCKA", "-" :"MINUS", "+" :"PLUS", "/" :"DELENO", "." :"BODKA","*":"HVEZDA","?":"OTAZNIK","%":"PERCENT","!":"VYKRIC",",":"CIARKA"}
    osetrenyvstup = ""
    text = text.upper()
    validniAbeceda = ["A" ,"B" ,"C" ,"D" ,"E" ,"F" ,"G" ,"H" ,"I" ,"J" ,"K" ,"L" ,"M" ,"N" ,"O" ,"P" ,"Q" ,"R" ,"S" ,"T" ,"U" ,"V" ,"W" ,"X" ,"Y" ,"Z","0","1", "2","3", "4","5", "6","7", "8","9"]
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

def pozicia1(matica,pismeno):
    for i, e in enumerate(matica):
        for j, ee in enumerate(e):
            if pismeno in ee:
                return [i,j]

def pozicia1_desifrovanie(matica,pismeno):
    for i, e in enumerate(matica):
        for j, ee in enumerate(e):
            if pismeno in ee:
                return i

def vrat_pismeno_zmatice(tabulka,x,y):
    for i, e in enumerate(tabulka):
        for j, ee in enumerate(e):
            if x==i and  y==j:
                return ee

def pozicia2(tabulka,index):
    tp=[]
    for i, e in enumerate(tabulka):
        for j, ee in enumerate(e):
            if j==index:
                tp.append(ee)
    tp.append(' ')
    return tp

def pozicia3(tabulka,index):
    tp=[]
    for i, e in enumerate(tabulka):
        for j, ee in enumerate(e):
            if j==index:
                tp.append(ee)
    tp=''.join(tp)
    tp=str(tp)+' '
    return tp

def sestice(par1):
    o = []
    while par1:
        o.append(par1[:6])
        par1 = par1[6:]
    return o

def patice(par1):
    o = []
    while par1:
        o.append(par1[:5])
        par1 = par1[5:]
    return o

def rozdelpodla_klucu(par1,par2):
    o = []
    while par1:
        o.append(par1[:par2])
        par1 = par1[par2:]
    return o

def OsetriKluc(kluc):
    global dlzka_kluc
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
    dlzka_kluc=len(osetrenyKluc)
    return osetrenyKluc

def vrat_index(matic_a,p_index):
    tp=[]
    dlzka_bloku=[]
    for i, e in enumerate(matic_a):
        for j, ee in enumerate(e):
            if j==p_index:
                tp.append(ee)
    dlzka_bloku.append(len(tp))
    tp.append(' ')
    return dlzka_bloku

def generuj_n_abecedu():
    global abeceda
    if c==11:
        abeceda = "ABCDEFGHIJKLMNOPQRSTUVXYZ"
    if c==12:
        abeceda = "ABCDEFGHIKLMNOPQRSTUVWXYZ"
    if c==2:
        abeceda = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
    konvert = list(abeceda)
    for n in range(10):
        random.shuffle(konvert)
    abeceda = ''.join(konvert)
    return abeceda

def adfgx(plany_text,klic):
    global vystup,matica
    matica=[]
    nezoradeny=OsetriKluc(klic)
    diakritika = {"00": "AA", "01": "AD", "02": "AF", "03": "AG", "04": "AX", "10": "DA", "11": "DD", "12": "DF", "13": "DG", "14": "DX", "20": "FA", "21": "FD", "22": "FF", "23": "FG", "24": "FX","30" :"GA", "31" :"GD", "32" :"GF", "33" :"GG", "34" :"GX", "40" :"XA", "41" :"XD", "42" :"XF", "43" :"XG", "44" :"XX"}
    for e in abeceda:
        matica.append(e)
    matica=patice(matica)
    upraveny_text=Osetrivstup_adfgx(plany_text,c)
    rez=[]
    for n in upraveny_text:
        x,y=pozicia1(matica,n)
        z=str(x)+str(y)
        try:
            rez += diakritika[z]
        except:
            pass
    sifra=[]
    rez=rozdelpodla_klucu(rez,dlzka_kluc)
    zoradeny=sorted(nezoradeny)
    y=[]
    for e,r in enumerate(zoradeny):
        for u,j in enumerate(nezoradeny):
            if r==j:
                y.append(u)
    x=[]
    for i in y:
        if i not in x:
            x.append(i)
    for g in x:
        sifra=sifra+pozicia2(rez,g)
    sifra=''.join(sifra)
    vystup=sifra
    return sifra

def adfgvx(plany_text,klic):
    global matica,vystup
    matica = []
    os_kluc = OsetriKluc(klic)
    diakritika = {"00": "AA", "01": "AD", "02": "AF", "03": "AG", "04": "AV", "05": "AX", "10": "DA", "11": "DD",
                  "12": "DF", "13": "DG", "14": "DV", "15": "DX", "20": "FA", "21": "FD", "22": "FF", "23": "FG",
                  "24": "FV", "25": "FX", "30": "GA", "31": "GD", "32": "GF", "33": "GG", "34": "GV", "35": "GX",
                  "40": "VA", "41": "VD", "42": "VF", "43": "VG", "44": "VV", "45": "VX", "50": "XA", "51": "XD",
                  "52": "XF", "53": "XG", "54": "XV", "55": "XX"}
    for e in abeceda:
        matica.append(e)
    matica = sestice(matica)
    upraveny_text = Osetrivstup_adfgvx(plany_text)
    rez = []
    for n in upraveny_text:
        x, y = pozicia1(matica, n)
        z = str(x) + str(y)
        try:
            rez += diakritika[z]
        except:
            pass
    sifra = []
    rez = rozdelpodla_klucu(rez, dlzka_kluc)
    nezoradeny = os_kluc
    zoradeny = sorted(os_kluc)
    y = []
    for e, r in enumerate(zoradeny):
        for u, j in enumerate(nezoradeny):
            if r == j:
                y.append(u)
    x = []
    for i in y:
        if i not in x:
            x.append(i)
    for g in x:
        sifra = sifra + pozicia2(rez, g)
    sifra = ''.join(sifra)
    vystup=str(sifra)
    return sifra

def adfgvx_desifruj(plany_text,klic):
    global vystup
    plany_text=plany_text.split()
    adfgvx_transfer = {"AA": "00", "AD": "01", "AF": "02", "AG": "03", "AV": "04", "AX": "05", "DA": "10", "DD": "11",
                       "DF": "12", "DG": "13", "DV": "14", "DX": "15", "FA": "20", "FD": "21", "FF": "22", "FG": "23",
                       "FV": "24", "FX": "25", "GA": "30", "GD": "31", "GF": "32", "GG": "33", "GV": "34", "GX": "35",
                       "VA": "40", "VD": "41", "VF": "42", "VG": "43", "VV": "44", "VX": "45", "XA": "50", "XD": "51",
                       "XF": "52", "XG": "53", "XV": "54", "XX": "55"}
    kluc=sorted(klic)
    kluc = ''.join(kluc)
    manipul=""
    while kluc:
        for e,ee in enumerate(plany_text):
            pismeno=str(kluc)[:1]
            manipul=str(manipul)+pismeno+str(ee)+' '
            kluc=kluc[1:]
    manipul=manipul.split()
    rozrad=[]
    for e in klic:
        ind=pozicia1_desifrovanie(manipul,e)
        obsah=manipul[ind]
        rozrad.append(obsah[1:])
        manipul.remove(obsah)
    predsifra=""
    for ee in range(len(klic)):
        predsifra=str(predsifra)+str(pozicia3(rozrad,ee))
    predsifra=predsifra.replace(' ','')
    odsifra=""
    while predsifra:
        transfer=predsifra[:2]
        predsifra=predsifra[2:]
        try:
            rez = adfgvx_transfer[transfer]
            x=int(rez[0])
            y=int(rez[1])
            odsifra=str(odsifra)+str(vrat_pismeno_zmatice(matica,x,y))
        except:
            pass
    odsifra=odsifra.replace('MEZERA',' ')
    odsifra=odsifra.replace('POMLCKA','_')
    odsifra = odsifra.replace('MINUS', '-')
    odsifra = odsifra.replace('PLUS', '+')
    odsifra = odsifra.replace('DELENO', '/')
    odsifra = odsifra.replace('BODKA', '.')
    odsifra = odsifra.replace('HVEZDA', '*')
    odsifra = odsifra.replace('OTAZNIK', '?')
    odsifra = odsifra.replace('PERCENT', '%')
    odsifra = odsifra.replace('VYKRIC', '!')
    odsifra = odsifra.replace('CIARKA', ',')
    vystup=odsifra
    return odsifra

def adfgx_desifruj(plany_text,klic):
    global vystup
    plany_text=plany_text.split()
    adfgx_transfer = {"AA": "00", "AD": "01", "AF": "02", "AG": "03",  "AX": "04", "DA": "10", "DD": "11",
                       "DF": "12", "DG": "13", "DX": "14", "FA": "20", "FD": "21", "FF": "22", "FG": "23",
                       "FX": "24", "GA": "30", "GD": "31", "GF": "32", "GG": "33", "GX": "34",
                        "XA": "40", "XD": "41", "XF": "42", "XG": "43", "XX": "44"}
    kluc=sorted(klic)
    kluc = ''.join(kluc)
    manipul=""
    while kluc:
        for e,ee in enumerate(plany_text):
            pismeno=str(kluc)[:1]
            manipul=str(manipul)+pismeno+str(ee)+' '
            kluc=kluc[1:]
    manipul=manipul.split()
    rozrad=[]
    for e in klic:
        ind=pozicia1_desifrovanie(manipul,e)
        obsah=manipul[ind]
        rozrad.append(obsah[1:])
        manipul.remove(obsah)
    predsifra=""
    for ee in range(len(klic)):
        predsifra=str(predsifra)+str(pozicia3(rozrad,ee))
    predsifra=predsifra.replace(' ','')
    odsifra=""
    while predsifra:
        transfer=predsifra[:2]
        predsifra=predsifra[2:]
        try:
            rez = adfgx_transfer[transfer]
            x=int(rez[0])
            y=int(rez[1])
            odsifra=str(odsifra)+str(vrat_pismeno_zmatice(matica,x,y))
        except:
            pass
    odsifra=odsifra.replace('MEZERA',' ')
    odsifra=odsifra.replace('POMLCKA','_')
    odsifra = odsifra.replace('MINUS', '-')
    odsifra = odsifra.replace('PLUS', '+')
    odsifra = odsifra.replace('DELENO', '/')
    odsifra = odsifra.replace('BODKA', '.')
    odsifra = odsifra.replace('HVEZDA', '*')
    odsifra = odsifra.replace('OTAZNIK', '?')
    odsifra = odsifra.replace('PERCENT', '%')
    odsifra = odsifra.replace('VYKRIC', '!')
    odsifra = odsifra.replace('CIARKA', ',')
    vystup=odsifra
    return odsifra

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.setWindowTitle("Casar_adfg(v)x")
    Dialog.show()
    sys.exit(app.exec_())

