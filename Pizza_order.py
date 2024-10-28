you = input("Enter your name :").lower()
partner = input("Enter your Partners name :").lower()

l = you.count("l") + partner.count("l")
o = you.count("o") + partner.count("o")
v = you.count("v") + partner.count("v")
e = you.count("e") + partner.count("e")



t = you.count("t") + partner.count("t")
r = you.count("r") + partner.count("r")
u = you.count("u") + partner.count("u")
e = you.count("e") + partner.count("e")

true_love = str(t+r+u+e) + str(l+o+v+e)

int_true_love = int(true_love)

if int_true_love < 10 or int_true_love > 90:
    print(f"Your score is {int_true_love},You are together like coke and mentos")

elif int_true_love >= 40 or int_true_love <=  50:
    print(f"Your score is {int_true_love},You are alright together")

else:
    print(f"Your score is {int_true_love}")

 