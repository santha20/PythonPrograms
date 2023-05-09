def rotateLeft(d, arr):
    arr1= arr
    arr2=arr[d:]
    #print(arr2)
    s=arr[0:d]
    arr2.extend(s)
    #print(arr2)
    for i in arr2:
        print(i,end=" ")
    """for i in arr:
        arr3=arr2.append(s)
    print(str(arr3))"""
     
firstMultipleInput = input().rstrip().split()
n = int(firstMultipleInput[0])


d = int(firstMultipleInput[1])


arr = list(map(int, input().rstrip().split()))

result = rotateLeft(d, arr)




"""

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'rotateLeft' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER d
#  2. INTEGER_ARRAY arr
#

def rotateLeft(d, arr):
    # Write your code here
    def rotateLeft(d, arr):
       arr1= arr
       arr2=arr[d:]
       s=arr[0:d]
       arr2.extend(s)
       for i in arr2:
          print(i,end=" ")
    
     
firstMultipleInput = input().rstrip().split()
print(firstMultipleInput)

n = int(firstMultipleInput[0])
print(n)

d = int(firstMultipleInput[1])
print(d)

arr = list(map(int, input().rstrip().split()))

result = rotateLeft(d, arr)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    d = int(first_multiple_input[1])

    arr = list(map(int, input().rstrip().split()))

    result = rotateLeft(d, arr)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
"""

