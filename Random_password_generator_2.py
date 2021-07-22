"# Random password generator"

import random

print("Hi, Welcome to Password Generator. Press Enter to continue")
Welcome = input()
print("I will gather simple information from you, Enter your name:")
Enter = str(input())
print("Thanks " + Enter + ".", "Press Enter for next step")
Nextstep = input()

while True:
    print("Press 1 for password with Number, or Press 2 for password with Character!")
    Press = int(input())

    Colours = ["Blue", "Red", "Green", "Yellow", "Black", "White", "Grey", "Purple",
               "Brown", "Beige", "Magenta", "Orange", "Pink", "Gold", "Silver"]
    Places = ["Paris", "London", "New york", "Miami", "Dubai", "Rome", "Tokyo",
              "Toronto", "Maui", "Tahiti", "Bali", "Spain", "Sydney", "Greece", "Ibiza"]
    Allsample = Colours + Places

    for choice in range(1):

        if Press == 1:
            print("enter a word you wish to add")
            letters = input()
            Numbers = "0" "1" "2" "3" "4" "5" "6" "7" "8" "9" "09" "67" "32" "21" "43"
            c = "".join(random.choice(Allsample))
            r = "".join(random.choice(Numbers))
            Combine = c + letters + r
            print("Your Generated Password is:")
            print(Combine)
            print("""Did not like that password """ + Enter + """?
Try again for desired result!, Press Enter """)
            Continue = input()

        if Press == 2:
            print("enter a word you wish to add")
            letters = input()
            Characters = "!" "@" "#" "$" "%" "&" "#@" "%$" "&!" "&#" "@!" "$!"
            C = "".join(random.choice(Characters))
            p = "".join(random.choice(Allsample))
            Combine = p + letters + C
            print("Your Generated Password is:")
            print(Combine)
            print("""Did not like that password """ + Enter + """?
Try again for desired result!, Press Enter """)
            Continue = input()
