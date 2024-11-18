import random
word_list = ["cracker" , "wiscker" , "snoopikitty" , "nishmo"]
chosen_word = random.choice(word_list)

print(f"pssst , the solution is :{chosen_word}")

display = []

for _ in chosen_word:
    display += "_"
print(display)



while "_" in display:
    guess = input("Guess a letter: ").lower()

    for index in range(len(chosen_word)):
        if chosen_word[index] == guess:
            display[index]=guess

    print(display)

print("YOU WIN MY SWEET GIRLFRIEND🥳🥳🎉✨")