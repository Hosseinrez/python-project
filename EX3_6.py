def EX3_6(x):
    largest_number =-100000
    for number in x:
        if (number > largest_number):
            largest_number = number
    smallest_number =100000
    for number in x:
        if (number < smallest_number):
            smallest_number = number
    if(len(x)==0):
        print(":/")
    
    search=largest_number-smallest_number
    if (search in x):
        print(":)")
    elif(len(x)!=0):
        print(":(")
