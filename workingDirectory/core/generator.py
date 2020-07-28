import time
import math
import random

 #000, 001, 010, 011, 100, 101, 110, 111

# class Generator():


arrayLength = 10
dataCurrent = []
dataPrevious = []
ruleSet = "01001000"

def generate_initial_seed():
    global arrayLength
    arr = [0] * arrayLength
    index = 0
    while (index < arrayLength):
        arr[index] = random.randint(0, 1)
        index += 1
    global dataCurrent
    dataCurrent = arr


def bitWiseCalc(neighborhood, index):
    global dataCurrent
    mask = 0x1
    mask = mask << 2
    mask = ~mask
    neighborhood = neighborhood & mask
    neighborhood = neighborhood << 1
    if (index != arrayLength - 1):
        neighborhood = neighborhood | dataCurrent[index]
    #print(neighborhood)
    return neighborhood

def arrayAnalysis():
    global dataCurrent
    index = 0
    neighborhood = int("0" + str((10 * dataCurrent[index]) + dataCurrent[index + 1]), base=2)
    arr = [0] * arrayLength
    arr[index] = int(ruleSet [neighborhood])
    while(index < arrayLength):
        arr[index] = int(ruleSet [neighborhood])
        neighborhood = bitWiseCalc(neighborhood, index)
        index += 1

    dataPrevious = dataCurrent
    dataCurrent = arr



def generatorCycle():
    for i in range(10):
        print(dataCurrent)
        arrayAnalysis()
    print(dataCurrent)

def prnt():
    global dataCurrent
    n = 0
    while (n < arrayLength):
        print(dataCurrent[n])
        n += 1
    print("")

def __init__(length):
    print("VGUHB JHUNHs")
    arrayLength = length
    generate_initial_seed()
    print("VGUHB JHUNHs")
    generatorCycle()

def main():
    print("yugvbhjuibjn")
    __init__(10)
    print("UYUHUUJHUIJUI")

if __name__ == "__main__":
    main()
