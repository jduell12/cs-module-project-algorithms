'''
Input: a List of integers as well as an integer `k` representing the size of the sliding window
Returns: a List of integers

Given an array of integers, there is a sliding window of size k which is moving from the left side of the array to the right, one element at a time. You can only interact with the k numbers in the window. Return an array consisting of the maximum value of each window of elements.
'''
def sliding_window_max(arr, k):
    #initialize empty array to hold max values
    maxValues = []
    #loop through the array
    for index in range(len(arr)-1):
        #check if the index plus k will go beyond the length of the array
        if index + k > len(arr):
            return maxValues
        #reset max value
        max = arr[index]
        i = index
        #loop through the window
        while i < index + k and i <= len(arr)-1:
            #check if the number in the array is greater than the max value
            if max < arr[i]:
                max = arr[i]
            i += 1
        maxValues.append(max)
    return maxValues


if __name__ == '__main__':
    # Use the main function here to test out your implementation 
    arr = [1, 3, -1, -3, 5, 3, 6, 7]
    k = 3

    print(f"Output of sliding_window_max function is: {sliding_window_max(arr, k)}")
