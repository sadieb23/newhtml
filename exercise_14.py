def get_valid_int_input(prompt):
   
    while True:
        try:
            user_input = int(input(prompt))  # Try to convert user input to an integer
            return user_input  # Return the valid input
        except ValueError:
            print("Invalid input. Please enter an int.")

# Initialize a variable to store the sum
total_sum = 0

# Get 5 valid integer inputs from the user
for i in range(5):
    valid_input = get_valid_int_input(f"Enter int # {i+1}: ")
    total_sum += valid_input

# Print the resulting sum
print("Your sum is ", total_sum)
 
 #used chatgpt for help