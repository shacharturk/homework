from BullsCode_instantiation import BullsCode
combination = BullsCode()
condition = False
for i in range(0, 10):
    guess = str(input("please guess a four digits code: "))
    score = combination.check(guess)
    print(f"your score is: {score}")
    if score == ["B", "B", "B", "B"]:
        condition = True
        break
if condition:
    print("you have won!")
else:
    print("you have lost")
