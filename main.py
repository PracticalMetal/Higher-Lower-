import os
os.system('cls' if os.name=='nt' else 'clear')

import random
from art import logo,vs
from game_data import data
cur_score=0
user_input=""
end_of_game=False

choice_one={}
choice_two={}
higher_choice={}

def choice_generator():
    global data
    new_choice=random.choice(data)
    data.remove(new_choice)
    return new_choice

def display(choice_one,choice_two):
    # printing the choice
    global user_input
    print(logo)
    print(f"Compare A: {choice_one['name']}, a {choice_one['description']}, from {choice_one['country']}.")
    print(vs)
    print(f"Compare B: {choice_two['name']}, a {choice_two['description']}, from {choice_two['country']}.")
    # taking user input for the option they select
    user_input=input("Who has more followers? Type 'A' or 'B': ").upper()

    
# randomly selecting the choice and deleting its occurrence from the data list 
choice_one=random.choice(data)
data.remove(choice_one)
choice_two=random.choice(data)
data.remove(choice_two)
    

while not end_of_game:
    
    

    display(choice_one,choice_two)

     # checking whether the input was right
    if user_input=='A':
        if choice_one['follower_count']>choice_two['follower_count']:
            cur_score+=1
            os.system('clear')
            print(f"You're correct! Current score is {cur_score}.")
            choice_two=choice_generator()
            # display(choice_one,choice_two)
        else:
            end_of_game=True
            os.system('clear')
            print(f"Sorry you lost, you scored: {cur_score}")
    
    elif user_input=='B':
        if choice_one['follower_count']<choice_two['follower_count']:
            cur_score+=1
            os.system('clear')
            print(f"You're correct! Current score is {cur_score}.")
            choice_one=choice_generator()
            # display(choice_two,choice_one)
        else:
            end_of_game=True
            os.system('clear')
            print(f"Sorry you lost, you scored: {cur_score}")
    





