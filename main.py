# with open("weather_data.csv") as file:
#     data = file.readlines()
#     list1 = []
#     for ele in data:
#         list1.append(ele.strip())
#     print(list1)

# import csv
#
# with open("weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     print(data)
#     temperatures = []
#     for row in data:
#         if row[1] == "temp":
#             pass
#         else:
#             temperatures.append(int(row[1]))
#     print(temperatures)

import pandas

# data = pandas.read_csv("weather_data.csv")
# print(data)
# print(data["temp"])
# data_dict = data.to_dict()
# print(data_dict)
#
# average = data["temp"].mean()
# print(average)
#
# max_value = data["temp"].max()
# print(max_value)

# Get Data in Column
# data["temp"]
# data.temp

# Get Data in Row
# print(data[data.day == "Monday"])
# print(data[data.temp == data.temp.max()])

# Convert Monday temperature to Fahrenheit
# monday_data = data[data.day == "Monday"]
# temp_to_fahrenheit = monday_data.temp[0] * 9 / 5 + 32
# print(temp_to_fahrenheit)

# Creating a data Frame

# data_dict = {
#     "students": ["Jai", "Shree", "Ram"],
#     "marks": [90, 98, 99]
# }

# custom_data_frame = pandas.DataFrame(data_dict)
# print(custom_data_frame)

# Converting Custom Data Frame to CSV data
# custom_data_frame.to_csv("custom_csv")
