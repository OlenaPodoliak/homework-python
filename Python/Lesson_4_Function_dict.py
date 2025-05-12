import random
import string

def create_dict():
    # Generate a random number of keys (1 to 5 keys per dictionary)
    num_keys = random.randint(1, 5)
    # Get  list of unique letters from string "abc...z"
    keys = random.sample(string.ascii_lowercase, num_keys)

    # Generate a dictionary with letters as keys and random values (0-100)
    new_dict = {}
    for key in keys:
        new_dict[key] = random.randint(0, 100)

    return new_dict

def update_dict(idx, d):
    for key, value in d.items():
        if key not in result_dict:
            result_dict[key] = (value, idx, 1)  # Store value and dict index
        else:
            # If key exists, compare and take max value
            if value > result_dict[key][0]:
                result_dict[key] = (value, idx, result_dict[key][2]+1)  # Update with max value and index
            else:
                result_dict[key] = (result_dict[key][0], result_dict[key][1], result_dict[key][2]+1)
    return result_dict

# Step 1: Create a random number of dictionaries (from 2 to 10)

num_dicts = random.randint(2, 10)  # Randomly choose how many dicts to create

list_of_dicts = []

for _ in range(num_dicts):
    # Append the dictionary to the list
    list_of_dicts.append(create_dict())

# Step 2: Create common dict with the specified rules (max_value, dict number with max_value, number of occurrences)

result_dict = {}

# Iterate through all dictionaries: idx - dictionary number, d - dictionaries
for idx, d in enumerate(list_of_dicts):
    update_dict(idx, d)

final_dict = {}  # This will store the final result with renamed keys

for key, (value, idx, cnt) in result_dict.items():
    if cnt > 1: # If key appears in more than one dict, rename key adding dictionary number
        final_key = f"{key}_{idx}"
    else:
        final_key = key
    final_dict[final_key] = value

# Step 3: Print the results
print("List of dictionaries:")
for i, d in enumerate(list_of_dicts):
    print("Dict", i, d)

print("\nMerged dictionary with renamed keys:")
print(final_dict)