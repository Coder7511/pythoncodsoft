import random
#Create class of Rock scissor paper game
class RockPaperScissorsGame:
    def __init__(self):
        self.user_score = 0
        self.computer_score = 0
#defining user choice
    def get_user_choice(self):
        while True:
            user_choice = input("Choose 1.rock \n2.paper \n3.scissors. \n Enter your Choose: ").lower()
            if user_choice in ['1', '2', '3']:
                return user_choice
            else:
                print("Invalid choice. Please choose rock, paper, or scissors.")
#defining computer choice
    def get_computer_choice(self):
        return random.choice(['1.Rock', '2.Paper', '3.Scissors'])
#defining  who is winner 
    def determine_winner(self, user_choice, computer_choice):
        if user_choice == computer_choice:
            return "It's a tie!"
        elif (
            (user_choice == 'rock' and computer_choice == 'scissors') or
            (user_choice == 'scissors' and computer_choice == 'paper') or
            (user_choice == 'paper' and computer_choice == 'rock')
        ):
            return "You win!"
        else:
            return "You lose!"
#defining how to play game
    def play_game(self):
        while True:
            print("\nRock, Paper, Scissors Game")
            print("----------------------------")

            user_choice = self.get_user_choice()
            computer_choice = self.get_computer_choice()

            print(f"\nYour choice: {user_choice}")
            print(f"Computer's choice: {computer_choice}")

            result = self.determine_winner(user_choice, computer_choice)
            print(result)

            if 'win' in result:
                self.user_score += 1
            elif 'lose' in result:
                self.computer_score += 1

            print(f"Score - You: {self.user_score}, Computer: {self.computer_score}")

            play_again = input("\nDo you want to play again? (yes/no): ").lower()
            if play_again != 'yes':
                print("\nThanks for playing!")
                break

if __name__ == "__main__":
    game = RockPaperScissorsGame()
    game.play_game()
