def EX3_5(x):
    j=0
    earn=0
    for j in x:
        if (j<0):
            j=j*-1
        earn=j+earn
        
    if(earn==25):
       return("true") 
    else:
       return("false") 
