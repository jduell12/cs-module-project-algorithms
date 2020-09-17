'''
Input: a List of integers as well as an integer `k` representing the size of the sliding window
Returns: a List of integers

Given an array of integers, there is a sliding window of size k which is moving from the left side of the array to the right, one element at a time. You can only interact with the k numbers in the window. Return an array consisting of the maximum value of each window of elements.
'''

def sliding_window_max(arr, k):
    window = []
    i = 0
    count = 0
    output = []
    #add first k elements to window
    while len(window) < k:
        if i == 0:
            window.append(arr[i])
        else:
            if window[len(window)-1] < arr[i]:
                window.pop(len(window)-1)
                window.append(arr[i])
                output.append(window[0])
            else:
                window.append(arr[i])
        i += 1
        count += 1
    
    #go through part of array we haven't checked yet
    for i in range(count, len(arr)):
        output.append(window.pop(0))
        if not window: 
            window.append(arr[i])
        elif arr[i] > window[0]:
            for j in range(len(window)):
                window.append(arr[i])
                window.pop(0)
    
    while len(output) < len(arr) - k + 1:
        output.append(window.pop(0))
    return output
        
        
 
    
    
#first pass
# def sliding_window_max(arr, k):
#     output = []
    
#     for index in range(len(arr)):
#         if index + k > len(arr):
#             return output
        
#         startW = index
#         endW = index + k
#         maxValue = arr[index]


#         while startW < endW:
#             if maxValue < arr[startW]:
#                 maxValue = arr[startW]
#             startW += 1
#         output.append(maxValue)
        


if __name__ == '__main__':
    # Use the main function here to test out your implementation 
    arr = [1, 3, -1, -3, 5, 3, 6, 7] #8
    k = 3
    print(sliding_window_max(arr, k))
    # print(f"Output of sliding_window_max function is: {sliding_window_max(arr, k)}")
