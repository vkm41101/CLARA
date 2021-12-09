from matplotlib import pyplot as plt
import serial
import RPi.GPIO as GPIO
import numpy
import requests
import time
ser=serial.Serial('/dev/ttyUSB0')
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(26,GPIO.OUT)
GPIO.output(26,GPIO.LOW)
time.sleep(0.1)
GPIO.output(26,GPIO.HIGH)
yu=''
a=[0]
t=[0]
A=ser.readline()
plt.show()
d='{"macstat":"\\"running\\""}'
r=requests.patch('https://board-project-ee011.firebaseio.com/ecg.json',data=d)
plt.xlim(0, 0.15)
plt.ylim(-200, 200)
plt.autoscale(False)
while A!=-401:
    
    A=str(ser.readline())
    if A=='Null':
        A=0
    else:
        print(A)
        A=int(A[2:A.find('\\')])-400
        print(A)
    t+=[t[-1]+0.001]
    a+=[A]
    yu+=str(A)+','
    plt.plot(t,a)
    plt.pause(0.001)
plt.savefig('fig.jpg')    
plt.close()
d='{"macstat":"\\"done\\""}'
r=requests.patch('https://board-project-ee011.firebaseio.com/ecg.json',data=d)
yu=yu[0:len(yu)-6]
r=requests.patch('https://marat-89129.firebaseio.com/indication/tr.json',data='{"tr":"'+yu+'"}')
f=open('h.dll','wb')
f.close()





