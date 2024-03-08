import pandas

data = pandas.read_csv("./2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
# print(data)

fur_color = data['Primary Fur Color'].to_list()
# print(fur_color)
# for color in fur_color:
#     if color == 'Gray':
#         gray_squirrels = data['Primary Fur Color'].count()
#         print(f"total gray squirrels:{gray_squirrels}")
#     # elif color == 'Black':
#     #     print(f"total black squirrels:{data['Primary Fur Color'].count()}")
#     # elif color == 'Cinnamon':
#     #     print(f"total red squirrels:{data['Primary Fur Color'].count()}")
color_data = data[data['Primary Fur Color'] == 'Gray']
print(len(color_data))
new_dict = {'Fur':['Gray'],
            'Gray':len(color_data)
            }
df = pandas.DataFrame(new_dict)
print(df)
df.to_csv("./new_data.csv")