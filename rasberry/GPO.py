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

GPIO.output(21, 0)

def lightUp(ledNumber, period):
    GPIO.output(ledNumber, 1)
    time.sleep(period)
    GPIO.output(ledNumber, 0)
     
def blink(ledNumber, blinkCount, blinkPeriod):
    k = 0
    while k < blinkCount:
        k += 1
        GPIO.output(ledNumber, 1)
        time.sleep(blinkPeriod)
        GPIO.output(ledNumber, 0)
        time.sleep(blinkPeriod)


def runningLight(count, period):
    D = [21, 20, 16, 12, 7, 8, 25, 24]
    k = 0
    while k < count:
        k += 1
        for i in D:
            GPIO.output(i, 1)
            time.sleep(period)
            GPIO.output(i, 0)

def runningDark(count, period):
    D = [21, 20, 16, 12, 7, 8, 25, 24]
    k = 0
    for i in D:
        GPIO.output(i, 1)
    while k < count:
        k += 1
        for i in D:
            GPIO.output(i, 0)
            time.sleep(period)
            GPIO.output(i, 1)
    for i in D:
        GPIO.output(i, 0)


def decToBinList(decNumber):
    arr = []
    while decNumber != 1:
        arr.append(decNumber%2)
        decNumber //= 2
    arr.append(decNumber)
    arr1 = arr.reverse()
    return arr1

N = int(input())
print(decToBinList(N))








#GPIO.output(7, 0)