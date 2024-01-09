# This project is a game called Highlow
import data
import random
from art import high_low,vs1
print("Welcome to HighLow Game! This is more fun")
computer=None
versus=None
def guess():
     return random.choice(data.celeb)
#computer=guess()

def vs(computer):
    ver=guess() 
    if ver==computer:
        return guess()
    else:
         return ver
#versus=vs(computer)

def format(computer,versus):
    print(f"Compare A:\n {computer['name']}, a {computer['Description']}, from {computer['Country']}")
    #print(vs1)
    #print(f"Compare A:\n {type['name']}, a {type['Description']}, from {type['Country']}") 
    print(f"Compare B: \n {versus['name']}, a {versus['Description']}, from {versus['Country']}")
    
#format(computer,versus)
#print(high_low)
def check(computer,versus):
    #print(computer)
    #print(versus)
    for i in range(0,len(data.celeb)):
        #follow=data.celeb[i]['followers']
        if computer['followers']>=versus['followers']:
            highest=computer
        else:
            highest=versus
    return highest

def game():
    score=0
    flag=True
    while flag==True:
       
        computer=guess()
        versus=vs(computer)
        format(computer,versus)
        
        user_guess=input("Who has more followers Type 'A' or 'B' : ").upper()
        if user_guess=='A':
                compare=computer
                validate=check(computer,versus)
        if user_guess=='B':
                compare=versus
                validate=check(computer,versus)   
        #validate=check() 
        print("validate",validate)
        print("compare",compare)

        if validate==compare:
                score+=1
                print(f"User won, your score is {score}")
        else:
                flag=False
                print(f"You lost your score is {score}")



game()

    

