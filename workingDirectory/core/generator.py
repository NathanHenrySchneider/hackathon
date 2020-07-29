import time
import math
import random
from rulesets import RULESETS

 #000, 001, 010, 011, 100, 101, 110, 111

# class Generator():

SIZE = 1024
ITERATIONS = 10

arrayLength = SIZE
dataCurrent = []
dataPrevious = []
ruleSet = ''

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
    neighborhood = neighborhood & 7
    if (index != arrayLength):
        neighborhood = neighborhood | dataCurrent[index]
    return neighborhood

def arrayAnalysis():
    global dataCurrent, ruleSet
    count = 0
    neighborhood = int( ("0" + str(dataCurrent[0]) + str(dataCurrent[1])) , 2)
    arr = [0] * arrayLength
    index = 2
    while(index < arrayLength + 1):
        arr[count] = int(ruleSet[neighborhood])
        neighborhood = bitWiseCalc(neighborhood, index)
        count += 1
        index += 1
    arr[count] = int(ruleSet[neighborhood])
    dataPrevious = dataCurrent
    dataCurrent = arr


def generatorCycle():
    global ruleSet
    changeRuleSet()
    #while True:
    for i in range(ITERATIONS):
        print_ASCII()
        arrayAnalysis()
        changeRuleSet()
    print_ASCII()

def changeRuleSet():
    global ruleSet
    ruleSet = RULESETS[random.randint(0, len(RULESETS) - 1)]

def translate_to_ASCII(binary_string):
    ascii_list = [binary_string[i:i+8] for i in range(0, len(binary_string), 8)]
    ascii_string = []
    for char_list in ascii_list:
        string = ''
        for char in char_list:
            string += str(char)
        num = int(string, 2) % 127
        num = num if num > 32 else num + 33
        ascii_string.append(chr(num))
    return ''.join(ascii_string)

def printRulesAndData():
    global ruleSet
    global dataCurrent
    print(dataCurrent, end='\n\n')
    print(ruleSet)

def printX():
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

def print_ASCII():
    global dataCurrent
    print(translate_to_ASCII(dataCurrent))

def generate():
    arrayLength = SIZE
    generate_initial_seed()
    generatorCycle()

def get_current_key():
    global dataCurrent
    return translate_to_ASCII(dataCurrent)
