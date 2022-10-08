#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'caesarCipher' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. STRING s
#  2. INTEGER k
#

s = 'middle-Outz'
a = 'abcdefghijklmnopqrstuvwxyz'
k = 2
cipher_dict = {}


def caesarCipher(s, k):
    encrypted_s = ''
    cipher_key = a[k:] + a[:k]

    s = s.lower()
    for i in range(len(a)):
      cipher_dict[a[i]] = cipher_key[i]
    
    for l in s:
      if l in cipher_dict:
        encrypted_s = encrypted_s + cipher_dict[l]
      else:
        encrypted_s = encrypted_s + l
    
    result = encrypted_s
    print(result)
    return result

caesarCipher(s, k)
