'''
Input: a List of integers
Returns: a List of integers
'''
def moving_zeroes(arr):
    #loop through array given
    for index in range(len(arr)):
        #check if zero
        if arr[index] == 0:
            #remove from spot 
            arr.pop(index)
            #append 0 to right side of the array
            arr.insert(len(arr)-1, 0)
        else:
            #remove from spot 
            number = arr.pop(index)
            #append to left side of the array
            arr.insert(0, number)
    return arr


if __name__ == '__main__':
    # Use the main function here to test out your implementation
    arr = [0, 3, 1, 0, -2]

    print(f"The resulting of moving_zeroes is: {moving_zeroes(arr)}")