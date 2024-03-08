# #TODO: Create a letter using starting_letter.txt
# #for each name in invited_names.txt
# #Replace the [name] placeholder with the actual name.
# #Save the letters in the folder "ReadyToSend".
#
# #Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
#     #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
#         #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp
#
# PLACEHOLDER = "[name]"
#
#
# with open("./Input/Names/invited_names.txt", mode='r') as file:
#     file_template2 = file.readlines()
#     file.close()
# #print(file_template2)
#
# with open("./Input/Letters/starting_letter.txt", mode='r') as file:
#     file_template1 = file.read()
#     for name in file_template2:
#         stripped_name = name.strip()
#         new_name = file_template1.replace(PLACEHOLDER, name)
#         print(new_name)
#         with open(f"./Output/ReadyToSend/send to {stripped_name}.txt", mode='w') as file1:
#             file1.write(new_name)


#new attempt#
PLACEHOLDER = "[name]"
guest_list = []
with open("./Input/Names/invited_names.txt", mode='r') as file1:
    # invitation_list = file1.read()
    '''we need to convert the strings inside invitation_list into an actual list using readline()'''
    invitation_list = file1.readlines()
    for names in invitation_list:
        stripped_names = names.strip()
        guest_list.append(stripped_names)
print(guest_list)

'''now we need to replace the placeholder with our names, so we will use another function called replace()'''
with open("./Input/Letters/starting_letter.txt", mode='r') as file2:
    starting_letter = file2.read()
    for name in guest_list:
        final_letter = starting_letter.replace(PLACEHOLDER, name)
        print(final_letter)
        with open(f"./Output/ReadyToSend/send to {name}.txt", mode='w') as file3:
          file3.write(final_letter)




























