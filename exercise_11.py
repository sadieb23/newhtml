def get_unique_elements(input_list): #function takes input_list as parameter
    unique_list = [] #empty list
    for item in input_list: #loop through each element in input_list with a for loop
        if item not in unique_list: #check if it's already present in unique_list using not in condition. 
            unique_list.append(item) #append element
    return unique_list #returns list

# Test the function
test_list = [1, 2, 3, 4]
result = get_unique_elements(test_list)
print(result)

#used chatgpt for help