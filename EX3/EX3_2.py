
def EX3_2(x):
    
    largest_number1 =-100000
    for number in x:
        if (number > largest_number1):
            largest_number1 = number



   
    
    largest_number2 = -100000
    for number in x:
        if (number > largest_number2):
            if (number!=largest_number1):
                largest_number2 = number
            
            

    return(largest_number1*largest_number2)
    
