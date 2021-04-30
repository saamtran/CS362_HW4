import math
import random
import unittest

def calcAverage(array):
    total = 0
    for x in range(len(array)):
        total += array[x]
    
    total = total / len(array)
    print(" == Total: ", total)

    return total
