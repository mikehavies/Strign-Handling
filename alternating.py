# Program will recieve a string from the user and perform several different maipulations on it.

######### User Input ###############
original_text = input("Enter a sentence:\n")

############## Every other character upper case ##################
original_text.lower() # Make every character the same case

i = 0
string_list = []

while i < len(original_text):
    if i % 2 == 0:
       string_list.append(original_text[i].upper())
    else:
        string_list.append(original_text[i])
    i = i + 1

print("".join(string_list))

############### Every other word upper case ######################
split_sentence = original_text.split()
string_list = []

i = 0

while i < len(split_sentence):
    temp = split_sentence[i]
    if i % 2 == 0:
        string_list.append(temp.upper())
    else:
        string_list.append(temp)
    i = i + 1

print(" ".join(string_list))