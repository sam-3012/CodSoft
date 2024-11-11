import random
import sys

# Function to get user's choice
def get_user_choice():
    while True:
        user_choice = input("Choose rock, paper, or scissors (or type 'quit' to end): ").lower()
        if user_choice in ['rock', 'paper', 'scissors', 'quit']:
            return user_choice
        else:
            print("Invalid choice. Please choose rock, paper, or scissors.")

# Function to determine the winner
def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (user_choice == 'rock'and computer_choice == 'scissors') or \
         (user_choice == 'scissors' and computer_choice == 'paper') or \
         (user_choice == 'paper' and computer_choice == 'rock'):
        return "You win!"
    else:
        return "Computer wins!"

# Function to play the game
def play_game():
    user_score = 0
    computer_score = 0

    while True:
        user_choice = get_user_choice()

        if user_choice == 'quit':
            print("\nThanks for playing!")
            break

        computer_choice = random.choice(['rock', 'paper', 'scissors'])

        print(f"\nYou chose: {user_choice}")
        print(f"Computer chose: {computer_choice}")

        result = determine_winner(user_choice, computer_choice)
        print(result)

        if result == "You win!":
            user_score += 1
        elif result == "Computer wins!":
            computer_score += 1

        print(f"\nScores - You: {user_score}, Computer: {computer_score}")

        play_again = input("\nDo you want to play again? (yes/no): ").lower()
        if play_again != 'yes':
            print("\nThanks for playing!")
            break

# Main function to start the game
def main():
    print("Welcome to Rock, Paper, Scissors!")
    play_game()

if __name__ == "__main__":
    main()
     
