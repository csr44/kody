from PyQt5 import QtCore, QtGui, QtWidgets
import base64,hashlib,os,math,random,binascii,zipfile,shutil
from PyQt5.QtWidgets import (QMainWindow, QTextEdit,QAction, QFileDialog, QApplication)
from PyQt5.QtGui import QIcon
from os.path import basename
from datetime import datetime
import sys
d_ko=0
e_ko=0
n_ko=0
dokument=""
class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(283, 326)
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(30, 20, 221, 23))
        self.pushButton.setObjectName("pushButton")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(80, 40, 121, 20))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.pushButton_2 = QtWidgets.QPushButton(Dialog)
        self.pushButton_2.setGeometry(QtCore.QRect(30, 60, 221, 23))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(Dialog)
        self.pushButton_3.setGeometry(QtCore.QRect(30, 90, 221, 23))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(Dialog)
        self.pushButton_4.setGeometry(QtCore.QRect(30, 130, 221, 23))
        self.pushButton_4.setObjectName("pushButton_4")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(70, 110, 141, 20))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.pushButton_5 = QtWidgets.QPushButton(Dialog)
        self.pushButton_5.setGeometry(QtCore.QRect(30, 160, 221, 23))
        self.pushButton_5.setObjectName("pushButton_5")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(10, 200, 61, 16))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(10, 230, 121, 16))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(Dialog)
        self.label_5.setGeometry(QtCore.QRect(60, 200, 111, 31))
        self.label_5.setText("")
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(Dialog)
        self.label_6.setGeometry(QtCore.QRect(10, 250, 271, 71))
        self.label_6.setText("")
        self.label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_6.setObjectName("label_6")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

        self.pushButton.clicked.connect(self.gen)
        self.pushButton_2.clicked.connect(self.sukromny_kluc)
        self.pushButton_3.clicked.connect(self.vytvor_podpis_zazipuj)
        self.pushButton_4.clicked.connect(self.verejny_kluc)
        self.pushButton_5.clicked.connect(self.over_podpis)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.pushButton.setText(_translate("Dialog", "Generuj a uloz kluce"))
        self.label.setText(_translate("Dialog", "Vytvorenie podpisu"))
        self.pushButton_2.setText(_translate("Dialog", "Nacitaj sukromny kluc"))
        self.pushButton_3.setText(_translate("Dialog", "Vyber dokument a podpis"))
        self.pushButton_4.setText(_translate("Dialog", "Nacitaj verejny kluc"))
        self.label_2.setText(_translate("Dialog", "Overenie"))
        self.pushButton_5.setText(_translate("Dialog", "Over vybrany dokument"))
        self.label_3.setText(_translate("Dialog", "Platnost:"))
        self.label_4.setText(_translate("Dialog", "Informacie o dokumente:"))

    def gen(self):
        generuj_kluce()
        uloz_kluce()
    def vytvor_podpis_zazipuj(self):
        global dokument
        fname = QFileDialog.getOpenFileName(None, 'Vyber subor pre podpis', os.getcwd())
        udaje=""
        if fname[0]:
            f = open(fname[0], 'rb')
            pof=fname[0]
            po=os.stat(pof).st_ctime
            otp=datetime.fromtimestamp(po)
            otp=str(otp)
            otp=otp[:-7]
            cest=os.path.getsize(pof)
            gop=basename(fname[0])
            mn=str(gop)+str('\n')+str(pof)+str('\n')+str(otp)+str('\n')+str(cest)+str('bajtov')
            self.label_6.setText(mn)
            data = f.read()
            dokument=str(data)
            f.close()
            podpis = encrypt_string(dokument)
            podpis = str(podpis)
            podpis = rsa_sifruj(podpis)
            podpis = str(base64.b64encode(podpis.encode()))
            patpe = open("El_podpis.sign", 'x')
            patpe.write(podpis)
            patpe.close()
            ZipFile=zipfile.ZipFile("data_podpis.zip", "w")
            ZipFile.write('El_podpis.sign')
            ZipFile.write(fname[0],basename(fname[0]))
    def sukromny_kluc(self):
        global n_ko,e_ko
        fname = QFileDialog.getOpenFileName(None, 'Open file',os.getcwd()) #do fname da iba cestu
        if fname[0]:
            f = open(fname[0], 'r')
            data = f.read()
            zr = base64.b64decode(data.encode())
            zr = zr.decode('utf-8')
            zr=str(zr)
            zr=zr.replace(',',' ')
            zr=zr.split()
            n_ko=int(zr[0])
            e_ko=int(zr[1])
    def verejny_kluc(self):
        global n_ko,d_ko
        fname = QFileDialog.getOpenFileName(None, 'Open file',os.getcwd()) #do fname da iba cestu
        if fname[0]:
            f = open(fname[0], 'r')
            data = f.read()
            zr = base64.b64decode(data.encode())
            zr = zr.decode('utf-8')
            zr=str(zr)
            zr=zr.replace(',',' ')
            zr=zr.split()
            n_ko=int(zr[0])
            d_ko=int(zr[1])
    def over_podpis(self):
        fname = QFileDialog.getOpenFileName(None, 'Vyber subor pre overenie', os.getcwd())
        if fname[0]:
            zlozka = zipfile.ZipFile(fname[0])
            obsah = []
            h=[]

            #davam dokopy cestu k rozbalenemu dokumentu
            for info in zlozka.namelist():
                h.append(info)#h[1] je cely nazov dokumentu
            ju = str(r"\7") + h[1]
            ''.join(ju)
            ju=ju.replace('7','')
            cesta=os.getcwd()+str(ju)


            #sprav decode b64, desifroval
            for info in zlozka.infolist():
                premen = zlozka.open(info)
                k=premen.readlines()
                obsah.append(k)
            o=str(obsah[0])
            o=o[5:]
            o=o[:-3]
            text = base64.b64decode(o.encode())
            text=str(text)
            text=text[2:]
            text=text[:-1]
            hash=rsa_desifruj(text)

            #otvor binarne subor a zahashuj ho sha256

            k=os.getcwd()+str(r'\data_podpis.zip')
            with zipfile.ZipFile(k, 'r') as zip_ref:
                zip_ref.extractall(os.getcwd())
            patpe = open(cesta, 'rb')
            patpe=patpe.read()

            patpe=str(patpe)
            patpe=encrypt_string(patpe)
            if patpe==hash:
                self.label_5.setText("Dokument je pravy")
                self.label_5.setStyleSheet("color: green;")
            else:
                self.label_5.setText("Dokument je neplatny")
                self.label_5.setStyleSheet("color: red;")


def encrypt_string(hash_string):
    sha_signature = \
        hashlib.sha256(hash_string.encode()).hexdigest()
    return sha_signature
def rsa_sifruj(text):
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
def r_cislo():
    p=2
    while p%2==0 or p%10==5:
        p = random.randrange(1000000000000000,9999999999999999)
    return p
def uloz_kluce():
    f = open("kluc.pub", 'x')
    zr=str(n_ko)+','+str(e_ko)
    zr = base64.b64encode(zr.encode())
    zr=zr.decode("utf-8")
    f.write(zr)
    f.close()
    f1 = open("kluc.priv", 'x')
    man=str(n_ko)+','+str(d_ko)
    man = base64.b64encode(man.encode())
    man=man.decode("utf-8")
    f1.write(man)
    f1.close()
def prvocislo(cislo):
    koren=math.floor(math.sqrt(cislo))
    for priebeh in range(3 ,1+koren,2):
        if cislo%priebeh== 0:
            return False
    return True
def findmodinverse(a,m):
    if math.gcd(a,m)!=1:
        return None
    u1,u2,u3=1,0,a
    v1,v2,v3=0,1,m
    while v3!=0:
        q=u3//v3
        v1,v2,v3,u1,u2,u3=(u1-q*v1),(u2-q*v2),(u3-q*v3),v1,v2,v3
    return u1%m
def rsa_desifruj(text):
    text=text.split()
    desifra=""
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
    Dialog.setWindowTitle("Podpis_Casar")
    Dialog.show()
    sys.exit(app.exec_())

