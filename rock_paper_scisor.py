# rock ,paper ,scissors
import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
player_choice = int(input("What do you choose? Type 0 for Rock ,1 for Paper ,2 for Scissors :- \n"))
if player_choice == 0 :
    print("You choose Rock")
    print(rock)
elif player_choice == 1 :
    print("You choose Paper")
    print(paper)
elif player_choice == 2 :
    print("You choose Scissors")
    print(scissors)
else :
    print("Error! ,Please check your input and try again.")
# for computer code start
comp_choice = random.randint(0,2)
if comp_choice == 0 :
    print("Computer choose Rock")
    print(rock)
elif comp_choice == 1 :
    print("Computer choose Paper")
    print(paper)
elif comp_choice == 2 :
    print("Computer choose Scissors")
    print(scissors)
#game rule code
# first condition
if player_choice == 0:
    if comp_choice == 0:
        print("-----------------------------------------------------------------------------")
        print("Match Draw! , No one win.")
    elif comp_choice == 1:
        print("-----------------------------------------------------------------------------")
        print("Computer Win.")
        print(paper)
    else:
        print("-----------------------------------------------------------------------------")
        print("You Win.")
        print(rock)
# second condition
elif player_choice == 1:
    if comp_choice == 0:
        print("-----------------------------------------------------------------------------")
        print("You win.")
        print(paper)
    elif comp_choice == 1:
        print("-----------------------------------------------------------------------------")
        print("Match Draw! , No one win.")
    else:
        print("-----------------------------------------------------------------------------")
        print("Computer Win.")
        print(scissors)
# Third condition
else:
    if comp_choice == 0:
        print("-----------------------------------------------------------------------------")
        print("Computer win.")
        print(rock)
    elif comp_choice == 1:
        print("-----------------------------------------------------------------------------")
        print("You win.")
        print(scissors)
    else:
        print("-----------------------------------------------------------------------------")
        print("Match Draw! , No one win.")