# Step 1: Create a set of all even numbers between 1 and 30
# The set comprehension iterates through numbers from 1 to 30 (inclusive) using range(1, 31).
# For each number, it checks if the number is divisible by 2 (num % 2 == 0).
# If the condition is true, the number is added to the set.
even_num = {num for num in range(1, 31) if num % 2 == 0}

# Step 2: Display Result
print("Set of Even Numbers Between 1 and 30:", even_num)
