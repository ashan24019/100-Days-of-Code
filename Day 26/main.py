# sentence = "What is the Airspeed velocity of an Unladen Swallow?"
#
# word_list = sentence.split()
# print(word_list)
#
# word_and_letter_count = {word:len(word) for word in word_list}
#
# print(word_and_letter_count)

weather_c = {
    "Monday": 12,
    "Tuesday": 14,
    "Wednesday": 15,
    "Thursday": 14,
    "Friday": 21,
    "Saturday": 22,
    "Sunday": 24,
}

weather_f = {day: temp*9/5 + 32 for (day, temp) in weather_c.items()}

print(weather_f)