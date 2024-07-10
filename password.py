import random 
import array

lowercase_letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h','i', 'j', 'k', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
uppercase_letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
digits_list = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
special_symbols = ['@', '#', '$', '%', '^', '&', '*', '(',')', '=', ':', '?', '.', '/', '|', '~', '>', '<']

combined_characters = lowercase_letters + uppercase_letters + digits_list + special_symbols
 
random_lower = random.choice(lowercase_letters) 
random_upper = random.choice(uppercase_letters) 
random_digit = random.choice(digits_list)
random_symbol = random.choice(special_symbols)

temporary_password = random_lower + random_upper + random_digit + random_symbol

max_length = 12

for i in range(max_length - 3):
    temporary_password += random.choice(combined_characters)

temporary_password_list = array.array('u', temporary_password) 
random.shuffle(temporary_password_list)

generated_password = "" 

for char in temporary_password_list: 
    generated_password += char 
          
print("Generated Password: ", generated_password)
