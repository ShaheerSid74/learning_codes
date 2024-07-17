#macth case example
print("have you vote as of 18th july ?")
print("select type yes or no")
x=str(input("Type your answer: "))
if x == "yes":
    print("congractulations")
elif x == "no":
    print ("please select an option who do you want to vote for ?")
    print ("1. Arsal Sohail")
    print ("2. Ghulam Mustafa")
    print ("3. Bilal Asghar")
    print ("4. Muhammad Shaheer")
    def voting_now():
        while True:
          y = int(input("Enter your selection: "))
          match y:
                    case 1:
                        print("you have voted for Arsal sohail")
                    case 2:
                        print("you have voted for Ghulam Mustafa")
                    case 3:
                        print("you have voted for Bilal Asghar")
                    case 4:
                        print("you have voted for Muhammad Shaheer")
                    case _:
                        print("please select a valid option")
    voting_now()