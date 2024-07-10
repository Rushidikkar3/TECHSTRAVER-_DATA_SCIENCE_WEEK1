# Lists
my_list = [1, 2, 3]  # Create a list
print("List: ", my_list)

# Delete an element by value
my_list.remove(2)  # Remove the element 2
print("List after deletion: ", my_list )

# Reverse the order (modifies the original list)
my_list.reverse()
print("Reversed List: ", my_list)

# Append an element
my_list.append(4)
print("Appended List: ", my_list)



# Dictionaries
my_dict = {"name": "Alice", "age": 30}  # Create a dictionary
print("Dictionary: ", my_dict)

# Delete a key-value pair
del my_dict["age"]
print("Dictionary after deletion: ", my_dict)

#Reversal of dicitionary cannot be done.

# Append 
my_dict["city"] = "New York"
print("Appended Dictionary: ", my_dict)



# Sets
my_set = {1, 2, 3}  # Create a set
print("Set: ", my_set)

# Delete an element
my_set.remove(2)  # Remove the element 2
print("Set after deletion: ", my_set)

# Reversal of set cannot be done.

# Append 
my_set.add(4)
print("Appended Set: ", my_set)



# Tuples (immutable)
my_tuple = (1, 2, 3)  # Create a tuple
print("Tuple: ", my_tuple)

# Deletion of element cannot be done in tuples.

# Reverse 
reversed_tuple = my_tuple[::-1]
print("Reversed Tuple: ", my_tuple)

# Appending elements in tuple cannot be done.

