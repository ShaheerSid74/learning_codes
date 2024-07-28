questions = [
    "1. What is the capital of Germany?\nA. Frankfurt\nB. Nuremberg\nC. Munich\nD. Berlin",
    "2. Who wrote the play \"Romeo and Juliet\"?\nA. Poelo\nB. Shakespeare\nC. Daniel\nD. Cameron",
    "3. Which is the smallest planet in our solar system?\nA. Earth\nB. Mars\nC. Jupiter\nD. Mercury",
    "4. What is the chemical symbol for water?\nA. H2O\nB. CO2\nC. HNO3\nD. MnO"
]
answers = ["a", "b", "d", "a"]

def play_game(questions, answers):
    money = []
    print("Welcome to the game")
    print("Each correct answer gets you 10 Euro")
    play = input("Do you want to play? (yes/no): ").strip().lower()
    
    if play == "yes":
        for i, question in enumerate(questions):
            print(question)
            user_answer = input("Select an option from a-d: ").strip().lower()
            if user_answer == answers[i]:
                print("Correct answer")
                money.append(10)
            else:
                print("Wrong answer")
        print(f"Congratulations, you get {len(money) * 10} Euro")
    else:
        print("Okay, have a good time")

play_game(questions, answers)
