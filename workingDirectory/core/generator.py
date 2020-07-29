import time
import math
import random
from rulesets import RULESETS

 #000, 001, 010, 011, 100, 101, 110, 111

SIZE = 1024

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
    neighborhood = (0<<2) + (dataCurrent[0]<<1) + dataCurrent[1]
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
    changeRuleSet()
    while True:
        arrayAnalysis()
        changeRuleSet()

def changeRuleSet():
    global ruleSet
    ruleSet = RULESETS[random.randint(0, len(RULESETS) - 1)]

def translate_to_ASCII(binary_string):
    timestamp = str(int((time.time() % 1) * 10**8))
    ascii_list = [binary_string[i:i+8] for i in range(0, len(binary_string), 8)]
    ascii_string = []
    for char_list in ascii_list:
        string = ''
        for char in char_list:
            string += str(char)
        num = int(string, 2) % 127
        num = num if num > 32 else num + 33
        if num == 92:
            num += 1
        ascii_string.append(chr(num))
    timestamp = [timestamp[i:i+2] for i in range(0, len(timestamp), 2)]
    for num in timestamp:
        num = int(num)
        num = num if num > 32 else num + 33
        if num == 92:
            num += 1
        ascii_string.append(chr(num))
    return ''.join(ascii_string)

def generate():
    arrayLength = SIZE
    generate_initial_seed()
    generatorCycle()

def get_current_key():
    global dataCurrent
    return translate_to_ASCII(dataCurrent)
