import random

print("🎮 Welcome to Rock, Paper, Scissors! 🎮")

choices = ["rock", "paper", "scissors"]

while True:
    # user choice
    user_choice = input("\nEnter Rock, Paper, or Scissors (or 'quit' to exit): ").lower()

    if user_choice == "quit":
        print("Thanks for playing! Goodbye 👋")
        break
    if user_choice not in choices:
        print("❌ Invalid choice! Please enter Rock, Paper, or Scissors.")
        continue

    # computer choice
    computer_choice = random.choice(choices)
    print(f"Computer chose: {computer_choice}")

    # decide winner
    if user_choice == computer_choice:
        print("🤝 It's a Tie!")
    elif (user_choice == "rock" and computer_choice == "scissors") or \
         (user_choice == "paper" and computer_choice == "rock") or \
         (user_choice == "scissors" and computer_choice == "paper"):
        print("✅ You Win!")
    else:
        print("❌ You Lose!")
