'''
Input: a List of integers where every int except one shows up twice
Returns: an integer
'''
def single_number(arr):
    #dictionary to keep track of numbers visited in array
    visited = {}
    #loop through the array 
    for item in arr:
        #check if the number is in the dictionary already
        if item in visited:
            #if already in dictionary add to the count
            visited[item] += 1
        else:
            #if not in diciontary add it to the dictionary with the value of 1
            visited[item] = 1
            
    #looks for the count of 1 in the dictionary
    for key, value in visited.items():
        if value == 1:
            return key
    


if __name__ == '__main__':
    # Use the main function to test your implementation
    arr = [1, 1, 4, 4, 5, 5, 3, 3, 9, 0, 0]

    print(f"The odd-number-out is {single_number(arr)}")