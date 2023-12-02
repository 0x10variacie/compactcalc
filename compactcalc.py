import time
import math
val1 = 0
val2 = 0
memv = 0
memr = True

def value():
    while True:
        try:
            val1_input = input("Value 1: ")
            val1 = float(val1_input) if val1_input.strip() != "" else 0
            break
        except ValueError:
            print("Error: Numbers only!\n")
    while True:
        try:
            val2_input = input("Value 2: ")
            val2 = float(val2_input) if val2_input.strip() != "" else 0
            break
        except ValueError:
            print("Error: Numbers only!\n")
    return val1,val2

def swap(val1,val2):
    temp = val1
    val1 = val2
    val2 = temp
    print("Values swapped!\n")
    return val1,val2

def clear(val1,val2):
    if val1 == 0 and val2 == 0:
        print("Nothing to clear\n")
    else:
        val1 = float(0) if val1 != float(0) else val1
        val2 = float(0) if val2 != float(0) else val2
        print("Values cleared!\n")
    return val1,val2

def mems(memr):
    memr = not memr
    memr_status = "on" if memr else "off"
    print(f"Saving in memory {memr_status}\n")
    return memr

def add(val1,val2):
    addr = float(val1 + val2)
    return addr

def sub(val1,val2):
    subr = val2 - val1
    return subr

def mul(val1,val2):
    mulr = val1 * val2
    return mulr

def div(val1,val2):
    divr = val1 / val2
    return divr

def power(val1,val2):
    powr = val1 ** val2
    return powr

def root(val1,val2):
    rtr = val1 ** (1 / val2)
    return rtr

def abs1(val1):
    absr = abs(val1)
    return absr

def abs2(val2):
    absr = abs(val2)
    return absr

def exp1(val1):
    expr = math.exp(val1)
    return expr

def exp2(val2):
    expr = math.exp(val2)
    return expr

#Program goes here
print("CompactCalc v1.0 DEVTEST")
time.sleep(1.5)
print("by M. Veselov, 2023")
time.sleep(1)
print("")
time.sleep(0.5)
print("For help, type help")
print("To finish the script, type quit\n")
while True:                                         # The Program Core
    prompt = str(input(f"> ")) 
    
    #Settings go here
    if prompt == str("value"):
        print(f"Values are {val1} and {val2}.\n")

    if prompt == str("value set"):
        val1, val2 = value()
        print("Values set!\n")

    if prompt == str("value swap") or prompt == str("swap"):
        val1,val2 = swap(val1,val2)

    if prompt == str("value clear"):
        val1,val2 = clear(val1,val2)

    if prompt == str("mem"):
        print(f"Current memory: {memv}\n")

    if prompt == str("mem 1"):
        val1 = memv
        print(f"Value 1 is now {val1}\n")

    if prompt == str("mem 2"):
        val2 = memv
        print(f"Value 2 is now {val2}\n")

    if prompt == str("mem clear"):
        memv = float(0)
        print("Memory cleared\n")

    if prompt == str("mem save"):
        memr = mems(memr)

    #Math operations go here    
    if prompt == str("add") or prompt == str("calc add"):
        addr = add(val1,val2)
        print(f"{val1} + {val2} = {addr}\n")
        memv = addr if memr else memv

    if prompt == str("sub") or prompt == str("calc sub"):
        subr = sub(val1,val2)
        print(f"{val2} - {val1} = {subr}\n")
        memv = subr if memr else memv

    if prompt == str("mul") or prompt == str("calc mul"):
        mulr = mul(val1,val2)
        print(f"{val1} * {val2} = {mulr}\n")
        memv = mulr if memr else memv

    if prompt == str("div") or prompt == str("calc div"):
        if val2 != 0:
            divr = div(val1,val2)
            print(f"{val1} / {val2} = {divr}\n")
        else:
            print("Error: cannot divide by zero!\n")
        memv = divr if memr else memv

    if prompt == str("pow") or prompt == str("calc pow"):
        powr = power(val1,val2)
        print(f"{val1}^{val2} = {powr}\n")
        memv = powr if memr else memv

    if prompt == str("root") or prompt == str("calc root"):
        if val1 >= 0:
            rtr = root(val1,val2)
            print(f"{val1}^(1/{val2}) = {rtr}\n")          
        else:
            print("Error: cannot calculate!\n")
        memv = root if memr else memv

    if prompt == str("abs") or prompt == str("calc abs"):
        absr = abs1(val1)
        print(f"|{val1}| = {absr}\n")

    if prompt == str("abs2") or prompt == str("calc abs2"):
        absr = abs2(val2)
        print(f"|{val2}| = {absr}\n")

    if prompt == str("exp") or prompt == str("calc exp"):
        expr = exp1(val1)
        print(f"e^{val1} = {expr}\n")
        memv = expr if memr else memv

    if prompt == str("exp2") or prompt == str("calc exp2"):
        expr = exp2(val2)
        print(f"e^{val2} = {expr}\n")
        memv = expr if memr else memv

    # Menu commands go here
    elif prompt == str("help"):
        print ("Help page\n----------")
        print ("help - displays this page")
        print ("quit - terminates the program")
        print ("\nVALUES")
        print ("value - shows values 1 and 2")
        print ("value set - sets values 1 and 2")
        print ("value swap - swaps values 1 and 2, e.g. for subtraction or division")
        print ("value clear - clears values 1 and 2")
        print ("\nMEMORY")
        print ("0 at the beginning")
        print ("mem - displays the memory value (0)")
        print ("mem [1,2] - susbtitutes the memory value to any of the 2 values")
        print ("mem clear - clears the memory")
        print ("mem save - toggles saving the result in the memory (on by default)")
        print ("\nMATHEMATICAL OPERATIONS")
        print ("calc add: +")
        print ("calc sub: -")
        print ("calc mul: *")
        print ("calc div: /")
        print ("calc pow: ^")
        print ("calc root - root of a number")
        print ("calc abs[2] - absolute value [given the 2nd value]")
        print ("calc exp[2] - exponential function [given the 2nd value]")
        print ("NB: math commands can be executed without 'calc' as well!")
        print ("\n")
    elif prompt == str("quit"):
        break
    

