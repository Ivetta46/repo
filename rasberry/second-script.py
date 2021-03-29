import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)


GPIO.setup(10, GPIO.OUT)
GPIO.setup(9, GPIO.OUT)
GPIO.setup(11, GPIO.OUT)
GPIO.setup(5, GPIO.OUT)
GPIO.setup(6, GPIO.OUT)
GPIO.setup(13, GPIO.OUT)
GPIO.setup(19, GPIO.OUT)
GPIO.setup(26, GPIO.OUT)

def decToBinList(decNumber):
    arr = [0 for _ in range(8)]
    if decNumber == 0:
        return arr
    i = 0
    while decNumber != 1:
        arr[i] = decNumber % 2
        decNumber = decNumber // 2
        i += 1
    arr[i] = (decNumber)
    arr.reverse()
    return arr
def lightNumber(number):
    arr = decToBinList(number)
    D = [26, 19, 13, 6, 5, 11, 9, 10]
    for i in range(len(arr)):
        GPIO.output(D[i], arr[i])

print ("Введите число повторений:")
num = int(input())
i = 0
while i < num:
    for j in range(255):
        lightNumber(j)
        time.sleep(0.005)
    for j in range(255, -1, -1):
        lightNumber(j)
        time.sleep(0.005)
    i += 1

D = [26, 19, 13, 6, 5, 11, 9, 10]
for i in D:
    GPIO.output(i, 0)
GPIO.cleanup()       

