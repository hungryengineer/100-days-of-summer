#lets try with a file that doesn't exist

# try:
#     with open ('new_file.txt', 'r') as datafile:
#      print(datafile)
# except FileNotFoundError:
#     print("file not found, creating a new file")
#     with open ('new_file.txt', 'w') as datafile:
#      datafile.write("datafile")
# else:
#     with open ('new_file.txt', 'r') as datafile:
#      text = datafile.read()
#      print(text)

# height = int(input("enter your height"))
# if height > 2:
#     raise ValueError ("unrealistic value")
# else:
#     print("OK")

#
# fruits = eval(input())
# # TODO: Catch the exception and make sure the code runs without crashing.
# def make_pie(index):
#   try:
#     fruit = fruits[index]
#     print(fruit + " pie")
#   except IndexError:
#     if len(fruits) <= 4:
#       print("FruitPie")
#   else:
#     print(fruit + " pie")
#
# make_pie(4)

