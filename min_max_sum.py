arr = [7, 69, 2, 221, 8974]

def miniMaxSum(arr):
    arr = sorted(arr)
    print(arr)
    min_value = arr[0]
    max_value = arr[-1]

    middle_sum = 0
    for i in arr[1:-1]: 
        print(i)
        middle_sum = middle_sum + i

    print(min_value)
    print(max_value)
    print(middle_sum)
    min_sum = middle_sum + min_value
    max_sum = middle_sum + max_value
        
    result = str(min_sum) + ' ' + str(max_sum)
    print(result)
    return result
    

miniMaxSum(arr)
