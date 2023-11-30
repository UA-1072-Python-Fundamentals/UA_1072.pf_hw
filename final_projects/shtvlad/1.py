import random
def choice_of_user(list):
    repeat = True
    while repeat:
        try:
            num_choice = int(input("Make your choice 0-Rock, 1-Scissors, 2-Paper\n"))
            result=list[num_choice]
            repeat = False
        except IndexError:
            print("Input correct number: 0, 1, 2")
        except ValueError:
            print("Input correct number: 0, 1, 2")
    return result

def choice_of_pc(list):
    num_choice=random.randint(0, 2)
    result = list[num_choice]
    return result

def determ_winner(user,pc):
    if (user=="Rock" and pc=="Scissors") or (user=="Scissors" and pc=="Paper") or (user=="Paper" and pc=="Rock"):
        return "user"
    elif (pc=="Rock" and user=="Scissors") or (pc=="Scissors" and user=="Paper") or (pc=="Paper" and user=="Rock"):
        return "pc"
    else:
        return "no one"

list = ["Rock", "Scissors", "Paper"]

x=70
print("-"*x)
print(" "*12,"*"*3,"GAME: Rock, Scissors, Paper","*"*3)
print("-"*x)
print("Rules: Rock beats Scissors, Paper beats Rock, Scissors beats Paper")
print("-"*x)

cnt_game=0
user_win=0
pc_win=0
game_process=True
while game_process:

    user_choice=choice_of_user(list)
    pc_choice=choice_of_pc(list)
    match_result=determ_winner(user_choice,pc_choice)
    if match_result=="user":
        print(f"Your choice: {user_choice}, PC choice: {pc_choice}\nMatch result: You are the winner!")
        user_win+=1
    elif match_result=="pc":
        print(f"Your choice: {user_choice}, PC choice: {pc_choice}\nMatch result: You lost:(")
        pc_win+=1
    else:
        print(f"Your choice: {user_choice}, PC choice: {pc_choice}\nMatch result: Friendship wins!")
    cnt_game+=1

    continue_game=input(f"Game score:\nTotal matches: {cnt_game}, user won: {user_win}, pc win: {pc_win}\nDo you want to continue?(y/n): ")

    res_input=True
    while res_input:
        if continue_game=="y":
            game_process=True
            res_input=False
        elif continue_game=="n":
            game_process=False
            res_input = False
        else:
            continue_game = input("Input 'y' or 'n':")
    print("*"*10)
print("GAME OVER")