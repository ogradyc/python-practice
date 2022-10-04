
'''
improvement would be to try a loop so that we could have any size of list. 
When I was doing that, I was getting strange behavior in either getting the loop to add the wrong values, or getting an index out of range
need to figure out a more elegant way to add a slice. 
    print(arr[1:-1])
    middle_sum = 0
    for i in arr[0:-2]: 
        print(arr[0:-2])
        print(arr[i])
        middle_sum = middle_sum + arr[i]
        print(middle_sum)
    max_sum = middle_sum + max_value
    min_sum = middle_sum + min_value
'''

arr = [7, 69, 2, 221, 8974]

def miniMaxSum(arr):
    arr = sorted(arr)
    max_value = arr[0]
    mid1 =  arr[1]
    mid2 =  arr[2]
    mid3 =  arr[3]
    middle_sum = mid1 + mid2 + mid3
    min_value = arr[-1]
    #print(max_value)
    #print(min_value)

    max_sum = middle_sum + max_value
    min_sum = middle_sum + min_value
        
    print(str(max_sum) + ' ' + str(min_sum))

miniMaxSum(arr)
