# final_weather_file = []
# with open("./weather_data.csv", mode='r') as file:
#     csv_file = file.readlines()
# for data in csv_file:
#     stripped_csv_file = data.strip()
#     final_weather_file.append(stripped_csv_file)
# print(final_weather_file)

#using csv library
# import csv
# with open("./weather_data.csv", mode='r') as file:
#     csv_file = csv.reader(file)
#     temperatures = []
#     for row in csv_file:
#         if row[1] !='temp':
#             temperatures.append(int(row[1]))
#     print(temperatures)

#using pandas
import pandas
data = pandas.read_csv("weather_data.csv")
# print(type(data)) #dataframe type
# print(type(data['temp'])) #series type
# data_dict = data.to_dict()
# print(data_dict)
# temp_to_list = data['temp'].to_list()
# average_temp = data['temp'].mean()
# print(average_temp)
# max_temp = data['temp'].max()
# print(max_temp)
# print(data[data.temp == data.temp.max()]) #this is a conditional

day_temp_C = data.temp[0]
day_temp_F = (day_temp_C * 9/5) + 32
print(day_temp_F)
