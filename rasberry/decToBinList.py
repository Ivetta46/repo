
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
N = int(input())
print(decToBinList(N))