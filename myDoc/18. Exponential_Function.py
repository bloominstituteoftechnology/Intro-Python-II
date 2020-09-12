def raise_to_num(base_pow, pow_num):         # First create a function with two parameter
    result = 1                               # We set a variable to one for the iteration, 1 * anything will always give us anything
    for i in range(pow_num):                 # Now we create a variable and set it in range of the second paremeter
        result = result * base_pow           # and we use the result for the actual base. for example, let the base = 100, range = 3
                                             # 100 * result = 100, that is 1. the loop still need to go up 2 more times
                                             # now result is 100, the second time will be 100 * 100 = 10,000 one more to go
                                             # result now is 10,000. 10,000 * 100 = 1,000,000. 
                                             # Note the base remain the same.
    return result                            # Now we return the result which is now 1,000,000.
                                             # After a return statement we can't do anything except printing
print(raise_to_num(100,3))                   # Now we print the call function
