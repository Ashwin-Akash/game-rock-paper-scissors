#rock,paper,scissors 
import random
print("check your luck:")
def game():
    while True:
        game=['rock','paper','scissors']
        user=input("enter yours:").lower()
        computer=random.choice(game)
        print(f"computer choies:{computer}")
        if user==computer:
            print("match tie")
        elif user=='rock':
            if computer=='paper':
                print("computer won")
            else:
                print("you won")
        elif user=='paper':
            if computer=='scissors':
                print("computer won")
            else:
                print("you won")
        elif user=='scissors':yes
            if computer=='rock':
                print("computer won")
            else:
                print("you won")
        
            
        play_again=input("wanna play again?:(yes/no)")
        if play_again.lower() !='yes':
            break
game()