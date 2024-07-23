questions = [
    "1. What is the capital of Germany?\nA. Frankfurt\nB. Nuremberg\nC. Munich\nD. Berlin",
    "2. Who wrote the play \"Romeo and Juliet\"?\nA. Poelo\nB. Shakespeare\nC. Daniel\nD. Cameron",
    "3. Which is the smallest planet in our solar system?\nA. Earth\nB. Mars\nC. Jupiter\nD. Mercury",
    "4. What is the chemical symbol for water?\nA. H2O\nB. CO2\nC. HNO3\nD. MnO"
]
money=[]
answers = ["a","b","d","a"]
print ("welcome to the game")
print("Each correct answer gets you 10 Euro")
print ("select do you want to play")
x=str(input("type your answer:"))
if x=="yes":
    print (questions[0])
    answer_0=str(input("select an option from a-d? : "))
    if answer_0=="a":
        print("correct answer")
        money.append(10)
    else:
        print("wrong answer")
    print (questions[1])
    answer_1=str(input("select an option from a-d? : "))
    if answer_1=="b":
        print("correct answer")
        money.append(10)
    else:
        print("wrong answer")
    print (questions[2])
    answer_2=str(input("select an option from a-d? : "))
    if answer_2=="d":
        print("correct answer")
        money.append(10)
    else:
        print("wrong answer")
    print (questions[3])
    answer_3=str(input("select an option from a-d? : "))
    if answer_3=="a":
        print("correct answer")
        money.append(10)
    else:
        print("wrong answer")
else:
    print("ok have a good time")
print(money)
print("congractulations you get ",len(money)*10, "Euro")