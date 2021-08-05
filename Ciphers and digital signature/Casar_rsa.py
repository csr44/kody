# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mpa.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import random,math,sys,binascii
n_ko=0
e_ko=0
d_ko=0
p_ko=0
q_ko=0
desifra=""
sifra=""
c=1
class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(531, 224)
        self.lineEdit = QtWidgets.QLineEdit(Dialog)
        self.lineEdit.setGeometry(QtCore.QRect(30, 110, 201, 20))
        self.lineEdit.setObjectName("lineEdit")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(20, 110, 16, 21))
        self.label.setObjectName("label")
        self.Spust = QtWidgets.QPushButton(Dialog)
        self.Spust.setGeometry(QtCore.QRect(280, 110, 201, 23))
        self.Spust.setObjectName("Spust")
        self.radioButton = QtWidgets.QRadioButton(Dialog)
        self.radioButton.setGeometry(QtCore.QRect(20, 10, 82, 17))
        self.radioButton.setObjectName("radioButton")
        self.radioButton_2 = QtWidgets.QRadioButton(Dialog)
        self.radioButton_2.setGeometry(QtCore.QRect(80, 10, 82, 17))
        self.radioButton_2.setObjectName("radioButton_2")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(20, 140, 16, 16))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(20, 170, 47, 13))
        self.label_3.setObjectName("label_3")
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(150, 10, 91, 23))
        self.pushButton.setObjectName("pushButton")
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(20, 80, 16, 16))
        self.label_4.setObjectName("label_4")
        self.lineEdit_3 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_3.setGeometry(QtCore.QRect(30, 80, 201, 20))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.label_5 = QtWidgets.QLabel(Dialog)
        self.label_5.setGeometry(QtCore.QRect(20, 30, 47, 13))
        self.label_5.setObjectName("label_5")
        self.lineEdit_4 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_4.setGeometry(QtCore.QRect(30, 140, 201, 20))
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.lineEdit_2 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_2.setGeometry(QtCore.QRect(20, 50, 491, 20))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_5 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_5.setGeometry(QtCore.QRect(20, 190, 491, 20))
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.pushButton_2 = QtWidgets.QPushButton(Dialog)
        self.pushButton_2.setGeometry(QtCore.QRect(250, 10, 91, 23))
        self.pushButton_2.setObjectName("pushButton_2")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

        self.radioButton.clicked.connect(self.sifr)
        self.radioButton_2.clicked.connect(self.desifr)
        self.Spust.clicked.connect(self.spt)
        self.pushButton.clicked.connect(self.generuj)
        self.pushButton_2.clicked.connect(self.aktualizuj1)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "e"))
        self.Spust.setText(_translate("Dialog", "Spust"))
        self.radioButton.setText(_translate("Dialog", "Sifruj"))
        self.radioButton_2.setText(_translate("Dialog", "Odsifruj"))
        self.label_2.setText(_translate("Dialog", "d"))
        self.label_3.setText(_translate("Dialog", "Vystup"))
        self.pushButton.setText(_translate("Dialog", "Generuj kluce"))
        self.label_4.setText(_translate("Dialog", "n"))
        self.label_5.setText(_translate("Dialog", "Vstup"))
        self.pushButton_2.setText(_translate("Dialog", "Uloz svoje kluce"))

    def sifr(self):
        global c
        c = 1

    def aktualizuj1(self):
        global n_ko,e_ko,d_ko
        n_ko = int(self.lineEdit_3.text())
        e_ko = int(self.lineEdit.text())
        d_ko = int(self.lineEdit_4.text())



    def desifr(self):
        global c
        c = 2

    def spt(self):
        vstup=self.lineEdit_2.text()
        if c==1:
            cp=rsa_sifruj(vstup)
            self.lineEdit_5.setText(cp)
        else:
            cp=rsa_desifruj(vstup)
            self.lineEdit_5.setText(cp)

    def generuj(self):
        generuj_kluce()
        self.lineEdit_3.setText(str(n_ko))
        self.lineEdit.setText(str(e_ko))
        self.lineEdit_4.setText(str(d_ko))

def generuj_kluce():
    global n_ko,d_ko,e_ko,p_ko,q_ko
    p = r_cislo()
    while prvocislo(p) == False:
        p = p + 2
    p_ko=p
    q = r_cislo()
    while prvocislo(q) == False:
        q = q + 2
    q_ko=q
    n=p*q
    while True:
        e=random.randrange(pow(10,16),pow(10,17)-1)
        if math.gcd(e,(p-1)*(q-1))==1:
            break
    d=findmodinverse(e,(p-1)*(q-1))
    n_ko=n
    d_ko=d
    e_ko=e
    return n_ko,d_ko,e_ko

def prvocislo(cislo):
    koren=math.floor(math.sqrt(cislo))
    for priebeh in range(3 ,1+koren,2):
        if cislo%priebeh== 0:
            return False
    return True

def rsa_sifruj(text):
    global sifra
    sifra=[]
    binar=[]
    poc=0
    for e in text:
        dlzka=len(format(ord(e),'b'))
        if dlzka == 7:
            pismeno = "000"
            pismeno=pismeno+format(ord(e),'b')
            binar.append(pismeno)
        else:
            cislo="0000"
            cislo=cislo+format(ord(e),'b')
            binar.append(cislo)
        poc=poc+1
        if poc==9:
            poc=0
            binar=map(str,binar)
            binar=''.join(binar)
            desiatky=int(binar,2)
            sifra.append(str(pow(desiatky,e_ko,n_ko)))
            binar=[]
    if len(binar)>0:
        binar=map(str,binar)
        binar = ''.join(binar)
        desiatky = int(binar, 2)
        sifra.append(str(pow(desiatky, e_ko, n_ko)))
    sifra=' '.join(sifra)
    return  sifra

def findmodinverse(a,m):
    if math.gcd(a,m)!=1:
        return None
    u1,u2,u3=1,0,a
    v1,v2,v3=0,1,m
    while v3!=0:
        q=u3//v3
        v1,v2,v3,u1,u2,u3=(u1-q*v1),(u2-q*v2),(u3-q*v3),v1,v2,v3
    return u1%m

def r_cislo():
    p=2
    while p%2==0 or p%10==5:
        p = random.randrange(1000000000000000,9999999999999999)
    return p

def rsa_desifruj(text):
    global desifra
    text=text.split()
    for i,j in enumerate(text):
        castica=int(j)
        cast = pow(castica, d_ko, n_ko)
        cast = bin(cast)
        cast = cast[2:]
        while len(cast) % 10 != 0:
            cast = '0' + cast
        o = len(cast) // 10
        for kru in range(0, o):
            zlozka = str(cast)[:10]
            zlozka = int(zlozka, 2)
            cast = cast[10:]
            desifra = str(desifra) + chr(zlozka)
    return desifra
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.setWindowTitle("RSA_Casar")
    Dialog.show()
    sys.exit(app.exec_())

