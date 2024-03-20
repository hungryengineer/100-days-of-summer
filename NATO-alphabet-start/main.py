# student_dict = {
#     "student": ["Angela", "James", "Lily"],
#     "score": [56, 76, 98]
# }
#
# #Looping through dictionaries:
# for (key, value) in student_dict.items():
#     #Access key and value
#     pass
#
# import pandas
# student_data_frame = pandas.DataFrame(student_dict)
#
# #Loop through rows of a data frame
# for (index, row) in student_data_frame.iterrows():
#     #Access index and row
#     #Access row.student or row.score
#     pass

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

#TODO 1. Create a dictionary in this format:
# {"A": "Alfa", "B": "Bravo"}

import pandas
file = pandas.read_csv("nato_phonetic_alphabet.csv")
# dict = file.to_dict()
# print(dict)
new_dict = {}
for (index,rows) in file.iterrows():
    new_dict[rows.letter] = rows.code
print(new_dict) #cleaned the file by converting it from csv to a dictionary
#below is through dictionary comprehension
# dict = {rows.letter:rows.code for (index,rows) in file.iterrows()}
# print(dict)

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.
def generate_phonetic_code():
    user_input = input("<<").upper()
    for i in user_input:
        try:
            code = new_dict[i] #to get the value of a key from dict
            print(code)
        except KeyError:
            if i in map(str, range(1, 11)):
                print("only alphabets accepted!")
                generate_phonetic_code() #recursion

generate_phonetic_code()




