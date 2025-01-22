
sentence = "What is the Airspeed velocity of an Unladen Swallow?"

word_list = sentence.split()
print(word_list)

word_and_letter_count = {word:len(word) for word in word_list}

print(word_and_letter_count)