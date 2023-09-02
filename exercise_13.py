def count_letters(input_string):
   
    letter_counts = {}  # Initialize an empty dictionary to store letter counts
    
    # Iterate through each character in the input string
    for char in input_string:
        # Convert the character to lowercase
        char_lower = char.lower()
        
        # Ignores spaces
        if char_lower != ' ':
            # Update the count for the current letter in the dictionary
            letter_counts[char_lower] = letter_counts.get(char_lower, 0) + 1
    
    return letter_counts

# Get input from the user
user_input = input("Enter a string: ")

# Call the function to count letters and store the result in letter_count_dict
letter_count_dict = count_letters(user_input)

# Print the resulting dictionary
print(letter_count_dict)

#used chatgpt to help