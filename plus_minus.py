
import math
import os
import random
import re
import sys

#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

arr = [-4, 3, -9, 0, 4, 1]
test_list = [0, 100, 35, 0, 94, 40, 42, 87, 59, 0]

def plusMinus(arr):
    positive = 0.000000
    negative = 0.000000
    zero = 0.000000
    arr_dict = {1:0, -1:0, 0:0}
    
    for i in arr:
        if i < 0:
          i = -1
        if i > 0:
          i = 1
        if i in arr_dict:
            sign_count = arr_dict[i] + 1
            arr_dict[i] = sign_count
        else:
            print('Not valid for dict')
    arr_length = len(arr)
    positive = float(arr_dict[1]) / float(arr_length)
    negative = float(arr_dict[-1]) / float(arr_length)
    zero = float(arr_dict[0]) / float(arr_length)

    print("{:.6f}".format(positive))
    print("{:.6f}".format(negative))
    print("{:.6f}".format(zero))
    
plusMinus(arr)
