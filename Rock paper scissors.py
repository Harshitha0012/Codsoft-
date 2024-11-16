import random
rock=''' 
_____
    ___)
    (____)
    (____)
    (___)
    (___)
'''
paper='''
    ______
    ____)___
    _______)
    _________)
    ______)
  _______)
  '''
scissors='''
    _________
    ____)____
        _____)
        ________)
     (____)
     (___)
     '''
game_images=[rock,paper,scissors]
user_choice=int(input("Enter your choice :Type 0 for Rock ,1 for Paper,2 for Scissors:"))
if user_choice>=3 or user_choice<0:
    print("You entered invalid number,You lose.")
else:
    print(game_images[user_choice])
    computer_choice=random.randint(0,2)
    print("computer Choice:")
    print(game_images[computer_choice])
    if computer_choice==user_choice:
        print("It's a draw")
    elif computer_choice==0 and user_choice==2:
        print("You lose.")
    elif computer_choice==2 and  user_choice==0:
        print("You win.")
    elif computer_choice>user_choice:
        print("You lose.")
    elif computer_choice<user_choice:
        print("You win.")
