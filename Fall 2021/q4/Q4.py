#This function gets to run with a linear equation. And its task is to output the root of the linear equation that is given by the user.
def find_root(a,b):
    
    #We checked the parameters are invalid or not.
    try:
        
        float(a)
        float(b) 
        
        #We showed to the user his/her function.
        print(f"This [f(x) = {a}x + {b}]")
           
        #If the function is constant,
        if a == 0:
            print(f"There is no root. Stable at {b}")
            
        #If the function is basic.
        else:
            # y = ax + b --> 0 = ax + b --> -b = ax --> -b/a = x
            root = (-1)*(b/a)
        
        print(f"The function's root is ({root}) .\nIntersection with Y is ({b}) .")
        
    except ValueError:
        print("Invalid value for parameter 'a' or 'b'!!!\nPlease enter a float or integer type parameter.")