# with open("weather-data.csv") as datafile:
#     data = datafile.readlines()
#     print(data)

# import csv
#
# with open("weather-data.csv") as data_file:
#     data = csv.reader(data_file)
#     temperature = []
#     next(data, None)
#     for row in data:
#         temperature.append(int(row[1]))
#
#     print(temperature)

# data = pandas.read_csv("weather-data.csv")

# print(data["temp"])
#
# data_dict = data.temp.to_dict()
# print(data_dict)
#
# average = sum(data["temp"]) / len(data["temp"])
#
#
# print(f"Average temperature: {round(average)}")
#
# print(round(data["temp"].mean()))

# max_num = max(data.temp)
#
# print(data[data.temp == max_num])
#
# monday = data[data.day == "Monday"]
# print(monday.condition)
#
# temp_in_f = monday.temp + 273
#
# print(temp_in_f)

import pandas

data = pandas.read_csv("2018-Central-Park-Squirrel-Census-Squirrel-Data.csv")
grey_squirrels_count = len(data[data["Primary Fur Color"] == "Gray"])
red_squirrels_count = len(data[data["Primary Fur Color"] == "Cinnamon"])
black_squirrels_count = len(data[data["Primary Fur Color"] == "Black"])

print(grey_squirrels_count)
print(red_squirrels_count)
print(black_squirrels_count)

data_dict = {
    "Fur Color": ["Gray", "Cinnamon", "Black"],
    "Count": [grey_squirrels_count, red_squirrels_count, black_squirrels_count]
}
df = pandas.DataFrame(data_dict)
df.to_csv("squirrel_count.csv")



