#ROCK PAPPER SCISSIORS GAME THROUGH PYTHON - TASK 4 - CODSOFT

#Rock beats scissors, scissors beat paper, and paper beats rock.

import random

choices=["rock","paper","scissor"]         
user_points,computer_points=0,0

def rpsgame(user,computer):
    global user_points           #to make updation on global env for evaluation
    global computer_points
    if user == computer:
        print("User chooses {} and Computer chooses {} and hence the round draws..!!".format(user,computer))
    
    elif user == 'rock':
        if computer == 'paper':
            print("Computer chooses paper and wins..!!")
            computer_points+=1
        else:
            print("Computer chooses scissors and loses..!!")
            user_points+=1
            
    elif user == 'paper':
        if computer == 'scissor':
            print("Computer chooses scissors and wins..!!")
            computer_points+=1
        else:
            print("Computer chooses rock and loses..!!")
            user_points+=1
            
    elif user == 'scissor':
        if computer == 'rock':
            print("Computer chooses rock and wins..!!")
            computer_points+=1
        else:
            print("Computer chooses paper and loses..!!")
            user_points+=1
    else:

        print("Enter Invalid options apart for ' rock / paper / scissir ',Try Again..!!")
        
   
    
   
while True:

    print(""" --- ENTER YOUR CHOICE ---

          --- rock ---
          --- paper ---
          --- scissor --- """)
    
    user=input("Enter your choice based on above condition :")
    computer=random.choice(choices)   #machine choice
    rpsgame(user,computer)   #function call
    ch=int(input("Enter 1 to continue and 0 to end the game :"))
    if ch:
        print("\nYour Score: {} and Computer Score: {}\n".format(user_points,computer_points))   #spot scorecard
    else:
        print("""
                    **** GAME RESULT ****
        """)
        
        if user_points == computer_points:                  #end results
            print(" -- TIE UP --")
        elif user_points > computer_points:
            print(" -- Hurray, YOU WIN --")
        else:
            print(" -- Oops, COMPUTER WINS --")
        break
