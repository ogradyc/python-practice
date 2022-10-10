'''
Rotational Cipher
One simple way to encrypt a string is to "rotate" every alphanumeric character by a certain amount. Rotating a character means replacing it with another character that is a certain number of steps away in normal alphabetic or numerical order.
For example, if the string "Zebra-493?" is rotated 3 places, the resulting string is "Cheud-726?". Every alphabetic character is replaced with the character 3 letters higher (wrapping around from Z to A), and every numeric character replaced with the character 3 digits higher (wrapping around from 9 to 0). Note that the non-alphanumeric characters remain unchanged.
Given a string and a rotation factor, return an encrypted string.
Signature
string rotationalCipher(string input, int rotationFactor)
Input
1 <= |input| <= 1,000,000
0 <= rotationFactor <= 1,000,000
Output
Return the result of rotating input a number of times equal to rotationFactor.
Example 1
input = Zebra-493?
rotationFactor = 3
output = Cheud-726?
Example 2
input = abcdefghijklmNOPQRSTUVWXYZ0123456789
rotationFactor = 39
output = nopqrstuvwxyzABCDEFGHIJKLM9012345678
'''

import math
# Add any extra import statements you may need here


# Add any helper functions you may need here

alpha = 'abcdefghigjlmnopqrstuvwxyz'
nums = '1234567890'

def reduce_rotation(rotation_factor, string):
  if rotation_factor > len(string):
    result = rotation_factor % len(string)
  else:
    result = rotation_factor
  return result

def create_cypher_dict(rotation_factor):
  alpha_rotation = reduce_rotation(rotation_factor, alpha)
  nums_rotation = reduce_rotation(rotation_factor, nums)
  cypher_dict = {}
  alpha_r = alpha[alpha_rotation:] + alpha[:alpha_rotation]
  nums_r = nums[nums_rotation:] +  nums[:nums_rotation]
  alpha_nums = alpha + nums
  alpha_nums_r = alpha_r + nums_r
  
  for i in range(len(alpha_nums)):
    cypher_dict[alpha_nums[i]] = alpha_nums_r[i]
    
  return cypher_dict
  

def rotationalCipher(input_str, rotation_factor):
  # Write your code here
  cypher = create_cypher_dict(rotation_factor)
  result = ''
  
  for i in input_str:
    upper = False
    if i.isupper() == True:
      upper = True
    if i.lower() in cypher:
      if upper == True:
        result = result + cypher[i.lower()].upper()
      else:
        result = result + cypher[i.lower()]
    else:
      result = result + i
  
  return result

