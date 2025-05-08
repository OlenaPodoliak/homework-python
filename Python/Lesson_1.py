import random  # Import the random module to generate random numbers

# Step 1: Create a list of 100 random integers between 0 and 1000
random_numbers = []
for i in range(100):
    random_numbers.append(random.randint(0, 1000))

print("list of integers:", random_numbers)

# Step 2: Sort the list from minimum to maximum without using the built-in sort()
for i in range(len(random_numbers)):
    min_index = i  # Assume the current index has the minimum value
    for j in range(i + 1, len(random_numbers)):
        if random_numbers[j] < random_numbers[min_index]:
            min_index = j  # Update the index of the minimum value
    # Swap the found minimum element with the current element
    swap_number = random_numbers[i]
    random_numbers[i] = random_numbers[min_index]
    random_numbers[min_index] = swap_number

print("Sorted list:", random_numbers)

# Step 3: calculate average for even and odd numbers
sum_even = 0
count_even = 0
sum_odd = 0
count_odd = 0
for i in range(len(random_numbers)):
    if random_numbers[i] % 2 == 0:
        sum_even = sum_even + random_numbers[i]
        count_even = count_even + 1
    else:
        sum_odd = sum_odd + random_numbers[i]
        count_odd = count_odd + 1

# Step 4: Print the average results to the console
try:
    print("Average of even numbers:", sum_even/count_even)
    print("Average of odd numbers:", sum_odd/count_odd)
except ZeroDivisionError:
    print("Error: division by zero  (may be List is empty)")
