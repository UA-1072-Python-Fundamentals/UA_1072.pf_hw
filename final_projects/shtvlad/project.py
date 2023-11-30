import random
class print_colors:
    HEADER = '\033[0;32m'
    TITLE = '\033[1;33m'
    FAIL = '\033[0;31m'
    ENDC = '\033[0m'
def choice_of_user(list):
    # функція для визначення вибору користувача
    # на вхід подається список з варіантами, один з яких потрібно вибрати
    # використаний цікл, який працює поки не буде зроблений вибір зі списку, якщо вибір не віподає
    # критеріям є виключення, які на це вказують

    repeat = True
    while repeat:
        try:
            num_choice = int(input(f"{print_colors.TITLE}"
                                   f"Make your choice 0-Rock, 1-Scissors, 2-Paper:\n"
                                   f"{print_colors.ENDC}"))
            result=list[num_choice]
            repeat = False
        except IndexError:
            print(f"{print_colors.FAIL}Input correct number: 0, 1, 2{print_colors.ENDC}")
        except ValueError:
            print(f"{print_colors.FAIL}Input correct number: 0, 1, 2{print_colors.ENDC}")
    return result

def choice_of_pc(list):
    # функція для визначення вибору комп'ютера
    # на вхід подається список з варіантами, один з яких потрібно вибрати
    # використаний метод randint з модуля random, який повертає випадкове число
    # та підставі якого визначається елемент списку
    num_choice=random.randint(0, 2)
    result = list[num_choice]
    return result

def determ_winner(user,pc):
    # функція, яка визначає переможця в залежності від комбінації виборів,
    # які були зроблені на попередніх етапах
    if (user=="Rock" and pc=="Scissors") or (user=="Scissors" and pc=="Paper") or (user=="Paper" and pc=="Rock"):
        return "user"
    elif (pc=="Rock" and user=="Scissors") or (pc=="Scissors" and user=="Paper") or (pc=="Paper" and user=="Rock"):
        return "pc"
    else:
        return "no one"

list = ["Rock", "Scissors", "Paper"]

x=70
print(f"{print_colors.HEADER}{'-'*x}")
print(f"{' '*12} {'*'*3} GAME: Rock, Scissors, Paper {'*'*3}")
print("-"*x)
print("Rules: Rock beats Scissors, Paper beats Rock, Scissors beats Paper")
print(f"{'-'*x}{print_colors.ENDC}")

cnt_game=0
user_win=0
pc_win=0
game_process=True
# основний процес,
# де визначається вибір кожної сторони,
# визначається переможець,
# ведеться рахунок
while game_process:

    user_choice=choice_of_user(list)
    pc_choice=choice_of_pc(list)
    match_result=determ_winner(user_choice,pc_choice)
    if match_result=="user":
        print(f"{print_colors.TITLE}Your choice:{print_colors.ENDC} {user_choice}, "
              f"{print_colors.TITLE}PC choice: {print_colors.ENDC} {pc_choice}\n"
              f"{print_colors.TITLE}Match result: {print_colors.ENDC} You are the winner!")
        user_win+=1
    elif match_result=="pc":
        print(f"{print_colors.TITLE}Your choice: {print_colors.ENDC}{user_choice}, "
              f"{print_colors.TITLE}PC choice: {print_colors.ENDC}{pc_choice}\n"
              f"{print_colors.TITLE}Match result: {print_colors.ENDC}You lost:(")
        pc_win+=1
    else:
        print(f"{print_colors.TITLE}Your choice: {print_colors.ENDC}{user_choice}, "
              f"{print_colors.TITLE}PC choice: {print_colors.ENDC}{pc_choice}\n"
              f"{print_colors.TITLE}Match result: {print_colors.ENDC}Friendship wins!")
    cnt_game+=1

    continue_game=input(f"{print_colors.TITLE}Game score:{print_colors.ENDC}\n"
                        f"total matches: {cnt_game}, user won: {user_win}, pc won: {pc_win}\n"
                        f"{print_colors.TITLE}Do you want to continue?(y/n): {print_colors.ENDC}")

    res_input=True
    while res_input:
        if continue_game=="y":
            game_process=True
            res_input=False
        elif continue_game=="n":
            game_process=False
            res_input = False
        else:
            continue_game = input(f"{print_colors.FAIL}Input 'y' or 'n':{print_colors.ENDC}")
    print("*"*10)
print(f"{print_colors.HEADER}GAME OVER{print_colors.ENDC}")