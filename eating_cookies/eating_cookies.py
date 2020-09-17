import math
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
def eating_cookies(n, cache={}):
    if cache == {}:
        cache = {i: 0 for i in range(n+1)}
    #checks if negative cookies which would have no way of eating it
    if n < 0:
        return 0
    #if 0 cookies only 1 way to eat it
    elif n == 0:
        return 1
    #check cache to see if answer is stored in there 
    if cache and cache[n] > 0:
        return cache[n]
    else:
        #store answers in cache 
        cache[n] = eating_cookies(n-1, cache) + eating_cookies(n-2, cache) + eating_cookies(n-3, cache)
        return cache[n]
            
    

#first pass solution
# def eating_cookies(n, cache=[]):
#     #check if n is less than 2 
#     if n < 2:
#         #only 1 way to eat the cookie
#         return 1
#     #check if n is 2
#     if n == 2:
#         #there are 2 ways to eat it , 1 1 or 2
#         return 2
#     #check if n is 3
#     if n == 3:
#         #there are 4 ways to eat the cookie (from prompt)
#         return 4
#     #if n is larger than 3
#     else:
#         #call the function recursively
#          return eating_cookies(n-1) + eating_cookies(n-2) + eating_cookies(n-3)

if __name__ == "__main__":
    # Use the main function here to test out your implementation
    num_cookies = 5

    print(f"There are {eating_cookies(num_cookies)} ways for Cookie Monster to each {num_cookies} cookies")
