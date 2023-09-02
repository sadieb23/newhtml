#Gets a string input from the user
user_input = input("Enter a string: ")

#Initializes empty strings for lowercase and uppercase letters
lowercase_letters = ""
uppercase_letters = ""

#Loops through the input string with for loop
for char in user_input:
    if char.islower():
        #If character is lowercase add to lowercase_letters string
        lowercase_letters += char
    elif char.isupper():
        #If character is uppercase add to uppercase_letters string
        uppercase_letters += char

#Combine lowercase and uppercase letters and remove spaces
result_string = lowercase_letters + uppercase_letters

#Print the string
print(result_string)

#used chatgpt for help