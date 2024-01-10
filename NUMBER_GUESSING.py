import random
from logo import art
def check_number():
    '''Function checks the number with user input and give suggestions'''
    user_guess=int(input("Make a Guess : "))
    if user_guess > number:
        set=1
        print("Too High\nGuess Again")
        return set
    elif user_guess < number:
        set=2
        print("Too Low\nGuess Again")
        return set
    else:
        set=3
        print("You Got it\n You won Hurray!")
        return set
        

def check_choice():
    global flag
    
    if choice=='easy':
        while flag<=10:
            print(f"You have {flag} attempts remaining to guess the number ")
            set1=check_number()
            if set1==3:
                break

            
            flag+=1

    elif choice=='hard':
        while flag<=5:
            print("FLAG",flag)
            set1=check_number()
            if set1==3:
                break
            print(f"You have {5-flag} attempts remaining to guess the number ")
            flag+=1
         


print(art)
number=random.randint(1,100)
#print(number)
print("Welcome to the number guessing")
print("I am thinking of a number between 1  and 100 ")
choice=input("Choose a Difficulty type 'easy' or 'hard' : ").lower()
#check_number()
flag=1 # this checks the number times user need to attempt
check_choice()

