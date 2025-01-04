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

import pandas

data = pandas.read_csv("weather-data.csv")

print(data["temp"])

