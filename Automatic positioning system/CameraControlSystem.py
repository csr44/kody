import cv2
import numpy as np
import time
import RPi.GPIO as gpio
vid = cv2.VideoCapture(0) #objekt vid
vid.set(3, 320) #znizenie rozlisenia kvoli vypoctovej narocnosti
vid.set(4, 240)
X=320
Y=240 
centerX = int(X/2) # definovanie stredu obrazovky
centerY = int(Y/2)
R3=1 #
behXmotora=False # Boolean pomocne premenne pre korektnu cinnost motorov
behYmotora=False
citlivost=1
VMplus=False
VMmin=False
HMplus=False
HMmin=False
i=1
def Stop(): #nevyuzita funkcia - dalsi spôsob riadenia
    if VMplus == True and RoY<=0:
        print("STOP")
    if VMmin == True and RoY>=0:
        print("STOP1")
    if HMplus == True and RoX<=0:
        print("STOP2")
    if HMmin == True and RoX>=0:
        print("STOP3")

gpio.setmode(gpio.BCM)
gpio.setwarnings(False)
gpio.setup(27, gpio.OUT, initial=gpio.LOW) #pri inicializacii systemu su oba motory uzemnene - prostredníctvom relé 
gpio.setup(22, gpio.OUT, initial=gpio.LOW)
gpio.setup(23, gpio.OUT, initial=gpio.LOW)
gpio.setup(24, gpio.OUT, initial=gpio.LOW)
#zaciatok=time.time()
while(True):
    ret, img = vid.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) # prevod do monochromatickej stupnice sedi - takto ma kazdy pixel definovanu hodnotu podla intenzity ziarenia
    gauss = cv2.GaussianBlur(gray, (R3, R3), 0)  # Gaussiansky filter pre odstranenie zkreslenia a neziaducich detailov 
    minVal, maxVal, minLoc, maxLoc = cv2.minMaxLoc(gauss) # Najdena lokacia (x,y) najjasnejsieho pixela 
    x,y=maxLoc
    tval=0.98*maxVal # znizenie maximalnej hodnoty najjasnejsieho pixela 
    ret,thresh = cv2.threshold(gauss,tval,255,cv2.THRESH_BINARY) # Prevod do binárnej podoby (prahová hodnota urcena podla premennej tval) - biela zostane iba cast najjasnejsich pixelov
    pocet=cv2.countNonZero(thresh) #spocitanie nenulovych pixelov 
    x_center, y_center= np.argwhere(thresh==255).sum(0) #sucet pozdlz riadkov
    Xx = int(y_center/pocet) #vypocitany stred z bielych pixelov
    Yy = int(x_center/pocet)
    cv2.circle(img, (Xx, Yy), 3, (0, 0, 255), -1) #kruh v strede bielych pixelov
    cv2.circle(img, (centerX, centerY), 3, (0, 255, 255), -1) #kruh v strede obrazovky
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    #cv2.imshow('image', thresh)
    cv2.imshow('real', img) #vyobrazenie jednotlivych filtrov do okien
    cv2.imshow('binar', thresh)
    cv2.imshow('rozmazanie', gauss)
    #Motory
    RoY = centerY - Yy #rozdiel stredu obrazovky a stredu bieleho objektu na ose X
    if (abs(RoY)>citlivost or behYmotora==True) and behXmotora!=True: #Zapnutie polohovania vertikalneho motora, horizontalny teraz nepolohuje, po dosiahnuti stredu (RoY=~0) sa motor vypne
        if RoY>0 and behYmotora!=True and abs(RoY)>citlivost:#DOPREDU
            behYmotora = True
            gpio.output(27, gpio.HIGH)
            gpio.output(22, gpio.LOW)
            #VMplus=True
            
        if RoY<0 and behYmotora!=True and abs(RoY)>citlivost:#DOZADU
            behYmotora = True
            gpio.output(22, gpio.HIGH)
            gpio.output(27, gpio.LOW)
                #VMmin=True
                #Stop()

        if behYmotora == True and abs(RoY)<citlivost:#Vypni
            #ZASTAVENIE 
            behYmotora = False
            gpio.output(27, gpio.LOW)
            gpio.output(22, gpio.LOW)
    
    RoX = centerX - Xx 
    
    if (abs(RoX)>citlivost or behXmotora==True) and behYmotora!=True: #Zapnutie polohovania horizontalneho motora
        if RoX>0 and behXmotora!=True and abs(RoX)>citlivost:#DOPREDU
            behXmotora = True
            gpio.output(23, gpio.HIGH)
            gpio.output(24, gpio.LOW)
            #HMplus=True
            
        if RoX<0 and behXmotora!=True and abs(RoX)>citlivost:#DOZADU
            behXmotora = True
            gpio.output(24, gpio.HIGH)
            gpio.output(23, gpio.LOW)
            #HMmin=True
        #Stop()
        
        if behXmotora == True and abs(RoX)<citlivost: #Vypni
        #ZASTAVENIE POHYBOV VERTIKALNEHO
            behXmotora = False
            gpio.output(23, gpio.LOW)
            gpio.output(24, gpio.LOW)
            
    #if i == 1:
        #print("%s sekund" % (time.time() - zaciatok))
        #i=2
            
    if abs(RoX)<citlivost and abs(RoY)<citlivost: #DOSIAHNUTIE NASMEROVANIA
        print("Motory sa vypinaju na 60 sekund z dovodu spravneho nasmerovania")
        time.sleep(60)
        
gpio.setup(27, gpio.OUT, initial=gpio.HIGH)
gpio.setup(22, gpio.OUT, initial=gpio.HIGH)
gpio.setup(23, gpio.OUT, initial=gpio.HIGH)
gpio.setup(24, gpio.OUT, initial=gpio.HIGH)        
vid.release()
cv2.destroyAllWindows()
