
#!/bin/python3

import math
import os
import random
import re
import sys

os.environ['OUTPUT_PATH'] = 'excercise.txt'

# Complete the alternatingCharacters function below.
def alternatingCharacters(s):

    s = [i for i in s]

    contador = 0

    quien_compara = s[0]

    for i in s[1:]:

        if quien_compara == i:

            contador +=1

        else:

            quien_compara = i


    print(contador)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        s = input()

        result = alternatingCharacters(s)

        fptr.write(str(result) + '\n')

    fptr.close()