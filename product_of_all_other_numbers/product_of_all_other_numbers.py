'''
Input: a List of integers
Returns: a List of integers

Write a function that receives an array of integers and returns an array consisting of the product of all numbers in the array except the number at that index.
'''
def product_of_all_other_numbers(arr):
    #initialize empty list
    output = []

    #loop through array
    for index in range(len(arr)):
        #reset product
        product = 1
        
        if index == 0:
            #get right side - only have right side for this case
            right = arr[index+1:]
            for num in right:
                product *= num
            output.append(product)
        else:
            #get left side of arr
            left = arr[:index]
            #get right side of arr
            right = arr[index+1:]
            for num in left:
                product *= num
            for num in right:
                product *= num
            output.append(product)
            
    return output 
        




if __name__ == '__main__':
    # Use the main function to test your implementation
    # arr = [1, 2, 3, 4, 5]
    arr = [2, 6, 9, 8, 2, 2, 9, 10, 7, 4, 7, 1, 9, 5, 9, 1, 8, 1, 8, 6, 2, 6, 4, 8, 9, 5, 4, 9, 10, 3, 9, 1, 9, 2, 6, 8, 5, 5, 4, 7, 7, 5, 8, 1, 6, 5, 1, 7, 7, 8]

    print(f"Output of product_of_all_other_numbers: {product_of_all_other_numbers(arr)}")
