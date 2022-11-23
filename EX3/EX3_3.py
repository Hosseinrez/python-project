def EX3_3(x):
    n=0
    s=0
    w=0
    e=0
    for j in x :
        if (j=='n'):
            n+=1
        if (j=='s'):
            s+=1
        if (j=='w'):
            w+=1
        if (j=='e'):
            e+=1
    verticaln=n-s 
    horizontalw=w-e
    horizontale=e-w
    verticals=s-n
    if(verticaln==2 and horizontale==3):
        return("True")
        
    elif(horizontalw==4 and verticaln==3):    
        return("True")
    else:
        return("False")
