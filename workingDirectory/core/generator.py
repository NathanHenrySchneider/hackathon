import time
import math
import random

 #000, 001, 010, 011, 100, 101, 110, 111

# class Generator():


arrayLength = 20
dataCurrent = []
dataPrevious = []
ruleSet = "01011000"

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
    neighborhood = neighborhood << 1
    #print("shift:" +str(neighborhood))
    neighborhood = neighborhood & 7
    #print("and7: " + str(neighborhood))
    #print("index: " + str(index))
    #print("currind: " + str(dataCurrent[index]))
    if (index != arrayLength):
        # print("index: " + str(index))
        # print("currind: " + str(dataCurrent[index]))
        neighborhood = neighborhood | dataCurrent[index]
    #print("nieghCalc: " + str(neighborhood))
    #print("neighborhood:" + str(neighborhood) + "\n")
    return neighborhood

def arrayAnalysis():
    global dataCurrent
    count = 0
    neighborhood = int( ("0" + str(dataCurrent[0]) + str(dataCurrent[1])) , 2)
    #print("start: " + str(neighborhood))
    arr = [0] * arrayLength
    #arr[0] = int(ruleSet [neighborhood])
    index = 2
    while(index < arrayLength + 1):
        #print("ruleSet: " + (ruleSet [neighborhood]))
        arr[count] = int(ruleSet [neighborhood])
        neighborhood = bitWiseCalc(neighborhood, index)
        #print("while: " + str(neighborhood))
        count += 1
        index += 1
    arr[count] = int(ruleSet [neighborhood])
    dataPrevious = dataCurrent
    dataCurrent = arr



def generatorCycle():
    while(True):
    #for i in range(20):
        #print(dataCurrent)
        prnt()
        arrayAnalysis()
    prnt()
    #print(dataCurrent)

def prnt():
    global dataCurrent
    n = 0
    str = ""
    while (n < arrayLength):
        if (dataCurrent[n] == 1):
            str += "X"
        else:
            str += " "
        n += 1
    print(str)

def __init__(length):
    #print("VGUHB JHUNHs")
    arrayLength = length
    generate_initial_seed()
    #print("VGUHB JHUNHs")
    generatorCycle()

def main():
    #print("yugvbhjuibjn")
    __init__(20)
    #print("UYUHUUJHUIJUI")

if __name__ == "__main__":
    main()
