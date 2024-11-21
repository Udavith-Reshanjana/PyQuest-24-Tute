# Step 1: Create a List
numbers = [18, 26, 52, 15, 10]

# Step 2: Add Items to the List
numbers.append(30)
numbers.append(40)
numbers.append(60)

# Step 3: Modify the List
index_30 = numbers.index(30)  # Find the index of the value 30
numbers[index_30] = 70        # Replace 30 with 70

# Step 4: Remove an Item
numbers.remove(60)  # Remove the value 60 from the list

# Step 5: Sum of the List
total_sum = sum(numbers)

# Step 6: Find the Average
average = total_sum / len(numbers)

# Step 7: Identify Maximum and Minimum Values
max_value = max(numbers)
min_value = min(numbers)

# Step 8: Sort the List
ascending_order = sorted(numbers)               # Sort in ascending order
descending_order = sorted(numbers, reverse=True)  # Sort in descending order

# Display Results
print("Updated List:", numbers)
print("Sum of the List:", total_sum)
print("Average of the List:", average)
print("Maximum Value:", max_value)
print("Minimum Value:", min_value)
print("Ascending Order:", ascending_order)
print("Descending Order:", descending_order)
