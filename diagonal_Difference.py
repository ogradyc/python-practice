# Complete the 'diagonalDifference' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#

arr = [[11, 2, 4], [4, 5, 6], [10, 8, -12]]

def diagonalDifference(arr):
    range_list = []
    for i in range(len(arr)):
        range_list = range_list + [i]

    print('left')
    left_diag = 0
    for i in range_list:
      print(arr[i][i])
      left_diag = left_diag + arr[i][i]
    
    print(' ')
    print('right')
    right_diag = 0
    for i, j in zip(range_list, range_list[::-1]):
      print(arr[i][j])
      right_diag = right_diag + arr[i][j]
    
    print(' ')
    result = abs(left_diag - right_diag)
    print(result)
    return result

diagonalDifference(arr)
