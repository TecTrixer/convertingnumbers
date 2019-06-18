import csv

""" 
    This program has three functions for converting numbers

        1. conv_to_dec(x, y) converts any-system to dec-numbers
        
            x is the input which is a string because it contains various signs
            y is the number-system of the input which is an integer
    
        2. conv_to_any(x, y) converts dec-system to any-system
        
            x is the input which is a string because it contains various signs
            y is the number-system of the output which is an integer
            
        3. conv_a_to_a(x, y, z) converts any-system to any-system
            
            x is the input which is a string because it contains various signs
            y is the number-system of the input which is an integer
            z is the number-system of the output which is an integer
    
    The program uses the "converting.csv" file and the csv module
    
    If you have problems make sure that 
    
        1. The .csv file is in the same folder as the .py file 
        2. Your python interpreter has the csv module preinstalled
    
    Yet you can only use the 
    base10-, base16-, base2-, base3-, base4-, base5-, base6-, base7-, base8-, base9-, base12-, base20-, base26- and base64-system
"""

"""
-------------------------------------------------1---------------------------------------------------------------
"""


def conv_to_dec(x, sys_num):
    # ----------------------------------Input--------------------------------------------------------

    # get input

    str_hex = x

    # ---------------------------------Definitions---------------------------------------------------

    arr_hex = [None] * len(str_hex)  # array for converting

    int_dec = 0  # integer for final sum and output

    # defining number-system

    with open("converting.csv", newline="") as csvfile:
        for row in csv.reader(csvfile):
            if row[0] == str(sys_num):
                col1 = int(row[1])
                col2 = int(row[2])

    # ---------------------------------Program-------------------------------------------------------

    # string to array   ||   letters to numbers

    for i in range(0, len(str_hex)):
        with open("converting.csv", newline="") as csvfile:
            for row in csv.reader(csvfile):
                if str_hex[i] == row[col1] or str_hex[i] == row[col2]:
                    arr_hex[i] = int(row[3])
                    break

    # use decimal system   ||   add up to final number

    for i in range(0, len(str_hex)):
        int_dec += arr_hex[i] * int(sys_num) ** (len(str_hex) - i - 1)

    # output final number

    return int_dec


"""
--------------------------------------------------2-------------------------------------------------------------
"""


def conv_to_any(x, sys_num):

    # -------------------------------------------INPUT-------------------------------------------------------------

    # get input

    int_dec = int(x)

    # ------------------------------------------Definitions--------------------------------------------------------
    if int(sys_num) < 10:
        arr_base = [None] * len(str(int_dec)) * 4
    else:
        arr_base = [None] * len(str(int_dec))

    str_fin = ""

    str_out = ""

    begin = False

    # defining number-system

    with open("converting.csv", newline="") as csvfile:
        for row in csv.reader(csvfile):
            if row[0] == str(sys_num):
                col = int(row[2])

    # defining null element

    with open("converting.csv", newline="") as csvfile:
        for row in csv.reader(csvfile):
            null = row[col]
            break

    # ------------------------------------------Program-------------------------------------------------------------

    # converting

    for i in range(0, len(arr_base)):
        if int_dec >= (int(sys_num) ** (len(str(int_dec)) - i - 1)):
            arr_base[i] = (int_dec // (int(sys_num) ** (len(arr_base) - i - 1)))
            int_dec %= (int(sys_num) ** (len(arr_base) - i - 1))
    # replacing

    for i in range(0, len(arr_base)):
        with open("converting.csv", newline="") as csvfile:
            for row in csv.reader(csvfile):
                if str(arr_base[i]) == row[3]:
                    arr_base[i] = row[col]

        if arr_base[i] != None:
            str_fin += str(arr_base[i])
        else:
            str_fin += null

    # removing nulls from the beginning

    for i in range(0, len(str_fin)):
        if begin == True or str_fin[i] != null:
            begin = True
            str_out += str_fin[i]

    # output

    return str_out


"""
----------------------------------------------------3-------------------------------------------------
"""


def conv_a_to_a(x, inp_sys, out_sys):
    return conv_to_any(conv_to_dec(x, inp_sys), out_sys)
