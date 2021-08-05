#include <Wire.h> // I2C
#include <SPI.h> // SPI
#include <SD.h>//SD 
#define CS_PIN 53              
#include <virtuabotixRTC.h> 
virtuabotixRTC myRTC(5, 6, 7);
const byte zaznamu = 200;         //zaznamy na karte pro jeden den
#include <Wire.h>
#include <Adafruit_Sensor.h>
#include <Adafruit_BNO055.h>
#include <utility/imumaths.h>
#include <math.h>
float thetaM;
float Xm;
float Ym;
float psi;
float theta;
float phi;
float thetaRad;
float phiRad;
float dt;
unsigned long millisOld;
#define BNO055_SAMPLERATE_DELAY_MS (100)

Adafruit_BNO055 myIMU = Adafruit_BNO055();

float akc_naklon = 0;  
float azimut = 0;      
float zenit = 0;      
float azimut_n = 0;     //pozadovany azimut
float zenit_n = 0;      //pozadovany zenit
int i = 0;          
int j = -1;     
bool behXmotora=false;
bool behYmotora=false;
//promenne casu
byte second, minute, hour, dayOfWeek, dayOfMonth, month, year;
int cas_h, cas_m, den_m;
float pole[zaznamu][4]; 
byte cislo = 0;         
byte radek = 0;         
char soubor[9] = "";  
File file;             
size_t n;              
char str[20];         
//MOTORY
int M1A = 0;  //piny pre motorA
int M1B = 1;

int M2A = 2; //piny pre motorB
int M2B = 3;

int citlivost = 10; 
int pauza = 0;
int vypnut = 0;

size_t readField(File* file, char* str, size_t size,const char* delim) { //funkcia na pracu so suborom
  char ch;
  size_t n = 0;
  while ((n + 1) < size && file->read(&ch, 1) == 1) {
    if (ch == '\r') {
      continue;
    }
    str[n++] = ch;
    if (strchr(delim, ch)) {
        break;
    }
  }
  str[n] = '\0';
  return n;
}

void readDS3231time(byte *second, byte *minute, byte *hour, byte *dayOfWeek, byte *dayOfMonth, byte *month, byte *year){ //aktualizacia hodnot casu
     myRTC.updateTime(); 
    *second = myRTC.seconds;
    *minute = myRTC.minutes;
    *hour = myRTC.hours;
    *dayOfWeek = myRTC.dayofweek;
    *dayOfMonth = myRTC.dayofmonth;
    *month = myRTC.month;
    *year = myRTC.year;
}

void setup() {
    pinMode(M1A, OUTPUT);
    pinMode(M1B, OUTPUT);
    pinMode(M2A, OUTPUT);
    pinMode(M2B, OUTPUT);
    digitalWrite(M1A, LOW); 
    digitalWrite(M1B, LOW);
    digitalWrite(M2A, LOW); 
    digitalWrite(M2B, LOW); 
    Serial.begin(115200);
    myIMU.begin();
    delay(1000);
    int8_t temp=myIMU.getTemp();
    myIMU.setExtCrystalUse(true);
    millisOld=millis();
    myRTC.updateTime(); 
    Wire.begin();           // I2C
    Serial.begin(115200);   // seriove
    Serial.println("Pripojovanie");
    while (!SD.begin(CS_PIN)){
      Serial.println("Karta nejde pripojit");
      delay(2000);
    }
    readDS3231time(&second, &minute, &hour, &dayOfWeek, &dayOfMonth, &month, &year);//ziskanie data a casu
    sprintf(soubor, "%02d-%02d.txt", month, dayOfMonth);
    file = SD.open(soubor);           
    while (!file){
      Serial.println("Nie je mozne otvorit subor.");
      delay(2000);
    }
    file.seek(0);               
    while (true) {              
      n = readField(&file, str, sizeof(str), ",\n");
      if (n == 0) break;               
      if (str[n-1] == ',' || str[n-1] == '\n') {
      //i = sloupcovy index, j = radkovy index
          if (i == 0) j++;              
          if (i == 3) i = -1;
          i = i + 1;
        str[n-1] = 0;       
      } else{
        if (file.available()){
          Serial.print("Chyba!");
        }else{           
          i = 0;
        }
      }
      float cislo = atof(str);   
      pole[j][i == 0 ? 3 : i - 1] = cislo;  
    }
    file.close();                      
    cas_h = 100 * hour + minute;     
    cas_m = minute;
    den_m = dayOfMonth;
    for (i = 0; i < zaznamu; i++){      
      if (100 * pole[i][0] + pole[i][1] <= cas_h){
        radek = i;         
      }else{
        break;
      }
    }
    azimut_n = pole[radek][3];  
    zenit_n = pole[radek][2];    
    i = 0;                     
}

void loop() {
uint8_t system, gyro, accel, mg = 0;
myIMU.getCalibration(&system, &gyro, &accel, &mg);
imu::Vector<3> acc =myIMU.getVector(Adafruit_BNO055::VECTOR_ACCELEROMETER);//ziskanie dat z IMU
imu::Vector<3> gyr =myIMU.getVector(Adafruit_BNO055::VECTOR_GYROSCOPE);
imu::Vector<3> mag =myIMU.getVector(Adafruit_BNO055::VECTOR_MAGNETOMETER);
thetaM=-atan2(acc.x()/9.8,acc.z()/9.8)/2/3.141592654*360;
theta=(theta+gyr.y()*dt); //naklon1
phi=(phi-gyr.x()*dt); //naklon2
phiRad=phi/360*(2*3.14);// na Rad
thetaRad=theta/360*(2*3.14);// na Rad
Xm=mag.x()*cos(thetaRad)-mag.y()*sin(phiRad)*sin(thetaRad)+mag.z()*cos(phiRad)*sin(thetaRad);
Ym=mag.y()*cos(phiRad)+mag.z()*sin(phiRad);
float psi=atan2(Ym,Xm); //urcenie azimutu
float azimut = psi;
float deklinace = (4 + (32 / 60)) / (180 / PI);
azimut += deklinace; // upravy aj s deklinaciou
if (azimut < 0){azimut += 2 * PI;}
if (azimut > 2 * PI){azimut -= 2 * PI;}
azimut = azimut * 180/PI; //azimut z IMU
zenit = -thetaM; //vyska z IMU
dt=(millis()-millisOld)/1000.;
millisOld=millis();
      readDS3231time(&second, &minute, &hour, &dayOfWeek, &dayOfMonth, &month, &year);      //aktualni cas
      if (den_m != dayOfMonth){       
        asm volatile ("  jmp 0");    
      }
      if (minute != cas_m){          
        cas_m = minute;
        cas_h = 100 * hour + minute;
        if (pole[radek + 1][0] != 0){   //kontrola pole dat
          if (100 * pole[radek + 1][0] + pole[radek + 1][1] <= cas_h){
            radek++;
            azimut_n = pole[radek][3]; 
            zenit_n = pole[radek][2];
          }
        }
      }
      if (i >= 300){          
        i = 0;}
      i++;
      float R1=int(azimut)-int(azimut_n); //riadenie motorov
      if (behYmotora != true)
        {
          if (R1>0 && abs(R1)>citlivost) 
          {
            digitalWrite(M1A, HIGH); 
            digitalWrite(M1B, LOW);
            behXmotora = true;
          }
          if (R1<0 && abs(R1)>citlivost)
          {
            digitalWrite(M1B, HIGH); 
            digitalWrite(M1A, LOW);
            behXmotora = true;
           }
          if (abs(R1)<citlivost)
          {
            digitalWrite(M1A, LOW); 
            digitalWrite(M1B, LOW);
            behXmotora = false;
          }
        }
        float R2=int(zenit)-int(zenit_n);
        if (behXmotora != true)
        {
          if (R2>0 && abs(R2)>citlivost) 
          {
            digitalWrite(M2A, HIGH); 
            digitalWrite(M2B, LOW);
            behYmotora = true;
          }
          if (R2<0 && abs(R2)>citlivost)
          {
            digitalWrite(M2B, HIGH); 
            digitalWrite(M2A, LOW);
            behYmotora = true;
           }
          if (abs(R2)<citlivost)
          {
            digitalWrite(M2A, LOW); 
            digitalWrite(M2B, LOW);
            behYmotora = false;
          }
        }
        if (abs(R1)<citlivost && abs(R2)<citlivost) //dosiahnutie ziadaneho natocenia
        {
          Serial.println("Dosiahnuta poloha a odmlcanie systemu");
           delay(600000);

        }   
  }