# Complete the 'diagonalDifference' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#

arr = [[11, 2, 4], [4, 5, 6], [10, 8, -12]]

def diagonalDifference(arr):
    print(arr)

    #print(arr[0] + arr[1] + arr[2])

    #print(reversed(range(len(arr))))

    #print(arr[1][1])

    left_diag = 0
    for i in range(len(arr)):
      print(arr[i][i])
      left_diag = left_diag + arr[i][i]
    
    right_diag = 0
    for i in reversed(range(len(arr))):
      print(arr[i][i])
      right_diag = right_diag + arr[i][i]
    
    result = abs(left_diag - right_diag)
    print(result)
    return result
