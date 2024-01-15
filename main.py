def process_list(input_list):
    if (len(input_list) % 10 != 0):
        print("Error: The length of the list must be a multiple of 10.")
        return("Error: The length of the list must be a multiple of 10.")
    
    processed_list = [x for i, x in enumerate(input_list) if (i + 1) % 2 != 0 and (i + 1) % 3 != 0]
    
    print("Processed List:", processed_list)
    return processed_list

# try:
#     input_list = [int(x) for x in input("Enter a list of integers separated by spaces: ").split()]
#     result = process_list(input_list)
# except ValueError:
#     print("Error: Please enter valid integers.")
