def letter_position_controller(pi):
    #control for letter
    if len(pi) > 1:
        print("Horizontal input is not a letter")
        exit(0)

    #control for range(a,h)
    if pi not in ["a", "b", "c", "d", "e", "f", "g", "h"]:
        print("Horizontal input is not a proper letter")
        exit(0)
              
def number_position_controller(pi):
    #control for str
    for i in pi:
        if i not in "0123456789":
            print("Vertical input is not a number")
            exit(0)
    #control for range(0,8)
    pi = int(pi)
    if pi < 1 or pi > 8:
        print("Vertical input for knight is not a proper number")
        exit(0)
            
        
def same_square_controller(lk, nk, lb, nb):
    #control for same square
    if lk == lb and nk == nb:
        print("They can't be in the same square")
        exit(0)    

def Attack_bishop(lk, nk, lb, nb):
    sc = "abcdefgh"
    temp = int(nb) - int(nk)
    if temp < 0:
        temp *= -1
    elif temp == 0:
        return  
       
    sm = lb
    if lk < lb:
        sm = lk
    
    if sc[sc.index(sm) + temp] == lk or sc[sc.index(sm) + temp] == lb:
        print("Bishop can attack knight")
        exit(0)

def Attack_knight(lk, nk, lb, nb):
    if abs(int(nk) - int(nb)) == 2 or abs(int(nk) - int(nb)) == 1:
        if abs(ord(lk) - ord(lb)) == 1 or abs(ord(lk) - ord(lb)) == 2:
            print("Knight can attack bishop")
            exit(0)
    


# for knight position
lpiok = input("please enter horizontal position of the knight :")
letter_position_controller(lpiok)
npiok = input("Please enter vertical position of the knight : ")
number_position_controller(npiok)


# for bishop position
lpiob = input("please enter horizontal position of the bishop :")
letter_position_controller(lpiob)
npiob = input("Please enter vertical position of the bishop : ")
number_position_controller(npiob)

same_square_controller(lpiok, npiok, lpiob, npiob)
Attack_bishop(lpiok, npiok, lpiob, npiob)
Attack_knight(lpiok, npiok, lpiob, npiob)
print("Neither of them can attack each other")
