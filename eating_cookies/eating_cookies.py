'''
Input: an integer
Returns: an integer

Cookie Monster can eat either 1, 2, or 3 cookies at a time. If he were given a jar of cookies with n cookies inside of it, how many ways could he eat all n cookies in the cookie jar? Implement a function eating_cookies that counts the number of possible ways Cookie Monster can eat all of the cookies in the jar.

For example, for a jar of cookies with n = 3 (the jar has 3 cookies inside it), there are 4 possible ways for Cookie Monster to eat all the cookies inside it:

He can eat 1 cookie at a time 3 times
He can eat 1 cookie, then 2 cookies
He can eat 2 cookies, then 1 cookie
He can eat 3 cookies all at once.
Thus, eating_cookies(3) should return an answer of 4.
'''
def eating_cookies(n):
    #initialize number of ways to 1 for when eating only 1 cookie at a time
    ways = 1
    #check when eating 3 cookies at once
    #check that there is at least 3 cookies
    if n >= 3:
        #get number of times can eat 3 cookies at once
        threeC = n // 3
        #add the number of times you can eat 3 cookies at once to ways
        ways += threeC
        
        #check if n is not divisible by 3 (left over cookies)
        if n % 3 != 0:
            leftOver = n - (threeC * 3)
            #check if leftOver is 2 
            if leftOver == 2:
                ways += 1
            else:
                ways += leftOver
    #check when eating 2 cookies at once
    #check that there is at least 2 cookies
    elif n >= 2:
        #get the number of times can eat 2 cookies at a time
        twoC = n // 2
        #add the number of times to ways
        ways += twoC
        #check if n is not divisible by 2 
        if n % 2 != 0:
            leftOver = n - (twoC * 2)
            ways += leftOver
    
    #return the number of ways
    return ways 


if __name__ == "__main__":
    # Use the main function here to test out your implementation
    num_cookies = 5

    print(f"There are {eating_cookies(num_cookies)} ways for Cookie Monster to each {num_cookies} cookies")
