def EX3_1(x):
    if (type(x)==int):
        if ((x%2)==1):
            x=x*3+1
            return(x)
        elif ((x%2)==0):
            x=x/2
            return(x)
    else:
        return("the variable is not integer")
    
    
    
    
