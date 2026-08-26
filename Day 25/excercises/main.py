# with open("./excercises/weather_data.csv") as data_file:
#     data = data_file.read()
#     print(data)

# import csv

# with open("./excercises/weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     temperatures = []
#     next(data, None)
#     for row in data:
#         temperatures.append(int(row[1]))
#     print(temperatures)

import pandas

data = pandas.read_csv("./excercises/weather_data.csv")
# print(type(data))
# print(type(data["temp"]))

# data_dict = data.to_dict()
# print(data_dict)

# temp_list = data["temp"].to_list()
# average_temp = sum(temp_list) / len(temp_list)
# print(average_temp)

# print(data["temp"].mean())
# print(data["temp"].max())

# print(data["condition"])
# print(data.condition)

# print(data[data["temp"] == data["temp"].max()])

# monday = data[data["day"] == "Monday"]
# print((monday["temp"] * 9 / 5) + 32)


# Create a datafame from scratch
data_dict = {"students": ["Amy", "James", "Angela"], "scores": [76, 56, 65]}
print(data_dict)
data = pandas.DataFrame(data_dict)
# data.to_csv("./excercises/new_data.csv")
