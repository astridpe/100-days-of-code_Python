# import csv
#
# with open("weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     temperatures = []
#     for row in data:
#         if row[1] != "temp":
#             temperatures.append(int(row[1]))
#     print(temperatures)

import pandas
# data = pandas.read_csv("weather_data.csv")
# print(data)
#
# data_dict = data.to_dict()
# temp_list = data["temp"].to_list()
#
# print(data["temp"].mean())
# print(data["temp"].max())

# # Get the row of maximum temperature:
# print(data[data.temp == data.temp.max()])
#
# # Convert temp from C to F:
# monday = data[data.day == "Monday"]
# temp_f = (monday.temp * 1.8) + 32
# print(temp_f)

# Create a dataframe from scratch:
# data_dict = {
#     "students" : ["Amy", "James", "Angela"],
#     "scores" : [76, 56, 65]
# }
#
# data = pandas.DataFrame(data_dict)
# data.to_csv("new_data.csv")

data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
grey_squirrels_count = len(data[data["Primary Fur Color"] == "Gray"])
red_squirrels_count = len(data[data["Primary Fur Color"] == "Cinnamon"])
black_squirrels_count = len(data[data["Primary Fur Color"] == "Black"])

data_dict = {
    "Fur Color": ["grey", "red", "black"],
    "Count": [grey_squirrels_count, red_squirrels_count, black_squirrels_count]
}

data = pandas.DataFrame(data_dict)
data.to_csv("fur_color.csv")











