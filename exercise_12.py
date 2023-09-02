def get_combined_dict(dict1, dict2):

    combined_dict = {}  # Initialize empty dictionary to store the combined results
    
    # Iterate through keys in the first dictionary
    for key in dict1:
        # Check if key is present in the second dictionary
        if key in dict2:
            # If key is common, sum the values from both dictionaries and add to the combined_dict
            combined_dict[key] = dict1[key] + dict2[key]
    
    return combined_dict

# Test the function
my_dict_1 = {'a': 5, 'b': 12, 'c': 3, 'd': 9}
my_dict_2 = {'b': 4, 'c': 9, 'd': 10, 'e': 16}
combined_dict = get_combined_dict(my_dict_1, my_dict_2)
print(combined_dict)

#used chatgpt to help