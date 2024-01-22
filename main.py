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

data = pandas.read_csv("weather_data.csv")
# print(data)
print(data["temp"])
