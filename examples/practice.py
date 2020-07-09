#create a function called stupid_addition
    #check the data types

    #if data types are both strings
        #convert string to numbers
        #add the numbers together

    #if data types are both numbers
        #return two number concated

    #else two different data types
        #return None

def stupid_addition(a, b):
    if type(a)==str and type(b)==str:
        print(int(a) + int(b))
    elif type(a)==int and type(b)==int:
        print(str(a) + str(b))
    else:
        print("None")

stupid_addition(1,1)
stupid_addition('1','1')
stupid_addition(1,'1')