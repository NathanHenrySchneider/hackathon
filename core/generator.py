import time
import math
import random
from rulesets import RULE_SETS

 #000, 001, 010, 011, 100, 101, 110, 111

# Size of each key in bits, before appending the timestamp-related characters
SIZE = 1024 

array_length = 0
data_current = []
rule_set = ''

# Randomly generate the first key using python's random module.
def generate_initial_seed():
    global array_length
    seed_array = []

    # Fill the first key with 0's and 1's.
    for i in range(array_length):
        seed_array.append(random.randint(0, 1))
    global data_current
    data_current = seed_array

# Shifting the neighborhood within data_current to the right by 1.
def bit_wise_calc(neighborhood, index):
    global data_current

    # Bit shift neighborhood to the left by 1.
    neighborhood = neighborhood << 1
    # Bitwise "and" with 7 to eliminate any 1's that arent in the first 3 bits.
    neighborhood = neighborhood & 7

    # If another element of data_current exists, put it in the last bit of neighborhood.
    # Otherwise, the last bit of neighborhood is an "imaginary" 0 that represents the "array_length" index of data_current
    if (index != array_length):
        neighborhood = neighborhood | data_current[index]
    return neighborhood

def array_analysis():
    global data_current, rule_set
    count = 0

    # The initial neighborhood is an "imaginary" zero that represents the "-1" index of data_current.
    neighborhood = (0<<2) + (data_current[0]<<1) + data_current[1]
    arr = [0] * array_length
    index = 2

    # Using the neighborhoods in data_current to generate the next array.
    while(index < array_length + 1):
        arr[count] = int(rule_set[neighborhood])
        neighborhood = bit_wise_calc(neighborhood, index)
        count += 1
        index += 1
    arr[count] = int(rule_set[neighborhood])
    data_current = arr

# Starts the infinite key generation cycle.
def generator_cycle():
    change_rule_set()
    while True:
        array_analysis()
        change_rule_set()

# Change the current rule_set that is being used to generate keys.
def change_rule_set():
    global rule_set
    rule_set = RULE_SETS[random.randint(0, len(RULE_SETS) - 1)]

# Translates a string of 0's and 1's to ascii characters
def translate_to_ASCII(binary_string):

    # Gets the first 8 decimal places of the current timestamp to ensure uniqueness of the key.
    timestamp = str(int((time.time() % 1) * 10**8))

    # Breaks the binary string up into 8-bit sections for ascii translation
    ascii_list = [binary_string[i:i+8] for i in range(0, len(binary_string), 8)]
    ascii_string = []

    # Converts each 8-bit binary string into an ascii character and append it to ascii_string.
    for char_list in ascii_list:
        string = ''
        for char in char_list:
            string += str(char)

        # These next few lines ensure that only keyboard characters are present in the key.
        num = int(string, 2) % 127
        num = num if num > 32 else num + 33
        if num == 92: # Backslashes cause problems, so we don't allow them.
            num += 1
        ascii_string.append(chr(num))

    # Break the 8-number timestamp string up into 2-digit integers
    timestamp = [timestamp[i:i+2] for i in range(0, len(timestamp), 2)]

    # Translate each of the four 2-digit integers into ascii characters
    for num in timestamp:
        num = int(num)
        num = num if num > 32 else num + 33
        if num == 92: # Backslashes cause problems, so we don't allow them.
            num += 1
        ascii_string.append(chr(num))
    return ''.join(ascii_string)

# Sets initial conditions and starts the key generation cycle.
def generate():
    global array_length
    array_length = SIZE
    generate_initial_seed()
    generator_cycle()

# Gets an ascii representation of the current key. 
def get_current_key():
    global data_current
    return translate_to_ASCII(data_current)
