from random import randint

# message when user doesn't do what's intended
def print_message():
    print("Sorry, that's not how you play the game. You have to pick Rock, Paper or Scissors. Tip: try typing a, b or c or just type out your choice.")

#generates computers choice
def choice():
    choice = ""
    num = randint(1, 3)
    if num == 1:
        choice = "Rock"
        return choice
    elif num == 2:
        choice = "Paper"
        return choice
    elif num == 3:
        choice = "Scissors"
        return choice

cpu_choice = choice()

#asks user for their choice of rock paper or scissors
def get_user_choice():
    user_choice = ""
    res = input("Rock, Paper or Scissors? \n[a] Rock\n[b] Paper\n[c] Scissors\n>>>")
    if res == 'a' or res == 'A':
        user_choice = "Rock"
        return user_choice
    elif res == 'b' or res == 'B':
        user_choice = "Paper"
        return user_choice
    elif res == 'c' or res == 'C':
        user_choice = "Scissors"
        return user_choice
    else:
        print_message()
        
player_choice = get_user_choice()

#checks to see who won the round
def results():
    if player_choice == "Rock" and cpu_choice == "Paper":
        winner = "Computer wins!"
        return winner
    elif player_choice == "Rock" and cpu_choice == "Scissors":
        winner = "You win!"
        return winner
    elif player_choice == "Paper" and cpu_choice == "Scissors":
        winner = "Computer wins!"
        return winner
    elif player_choice == "Paper" and cpu_choice == "Rock":
        winner = "You win!"
        return winner
    elif player_choice == "Scissors" and cpu_choice == "Rock":
        winner = "Computer wins!"
        return winner
    elif player_choice == "Scissors" and cpu_choice == "Paper":
        winner = "You win!"
        return winner
    else:
        winner = "It's a draw!"
        return winner

#Tally's the score
def scoring():
        player_score = 0
        cpu_score = 0
        if results() == "You win!":
            player_score += 1
            print("Your score is: " + str(player_score))
            print("Computer's score is: " + str(cpu_score))
        elif results() == "Computer wins!":
            cpu_score += 1
            print("Your score is: " + str(player_score))
            print("Computer's score is: " + str(cpu_score))
        else:
            print("Your score is: " + str(player_score))
            print("Computer's score is: " + str(cpu_score))

#The game
def play_game():
    print("Welcome to the ancient game of Rock, Paper, Scissors!!")
    print("You will play 3 rounds of Rock, Paper, Scissors. The best of 3 is the winner")
    
    games_played = 0

    while games_played < 3:

        yes_responses = ["yeah", "y", "sure", "definitely", "ye", "ready", "yup", "oui", "yes"]
        no_responses = ["n", "no", "nope", "nah", "non"]
        res = input("Are you ready?\n>>>").lower()
        if res in yes_responses:
            print("Go!")
        elif res in no_responses or (res not in yes_responses):
            print("Game Over!")
            break
        
        player_choice
        cpu_choice

        answer = 'You chose %s and the computer chose %s' % ( player_choice, cpu_choice)
        print(answer)

        results()

        scoring()

        games_played += 1

        break
play_game()
