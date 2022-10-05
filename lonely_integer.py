#
# Complete the 'lonelyinteger' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY a as parameter.
#

a = [1,2,3,4,3,2,1]

def lonelyinteger(a):
    lonely_hash = {}
    for i in a:
      if i in lonely_hash:
        lonely_hash[i] = lonely_hash[i] + 1
      else:
        lonely_hash[i] = 1

    #print(lonely_hash)
    
    result = None
    '''
    for i in lonely_hash:
      if lonely_hash[i] == 1:
        result = i
    '''
    
    inverted = {}
    for key, value in lonely_hash.items():
      inverted.setdefault(value, []).append(key)
    
    print(inverted)
    
    if 1 in inverted:
      result = inverted.get(1)[0]

    print(result)
    return result

lonelyinteger(a)
