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
    time.sleep(2)

while True:
    print("Введите число (-1 для выхода):")
    n = input()
    if n == "-1":
        print("program is ended")  
        break
    try:
        int(n)
    except ValueError:
        print("int's not a number")
    else:
        n = int(n)
        if n < 0 or n > 255:
            print("íncorrect number")
        else:
            lightNumber(n)
D = [26, 19, 13, 6, 5, 11, 9, 10]
for i in D:
    GPIO.output(i, 0)
GPIO.cleanup()       



    


