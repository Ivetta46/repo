import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)

GPIO.setup(21, GPIO.OUT)
GPIO.setup(20, GPIO.OUT)
GPIO.setup(16, GPIO.OUT)
GPIO.setup(12, GPIO.OUT)
GPIO.setup(7, GPIO.OUT)
GPIO.setup(8, GPIO.OUT)
GPIO.setup(25, GPIO.OUT)
GPIO.setup(24, GPIO.OUT)

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
    D = [21, 20, 16, 12, 7, 8, 25, 24]
    for i in range(len(arr)):
        GPIO.output(D[i], arr[i])
    time.sleep(5)

D = [21, 20, 16, 12, 7, 8, 25, 24]
for i in D:
    GPIO.output(i, 0)
number = int(input())
lightNumber(number)
GPIO.cleanup()


