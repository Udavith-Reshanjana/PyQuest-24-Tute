# Step 1: Create a set with at least six different fruits
fruits = {"apple", "banana", "cherry", "date", "grape", "mango"}

# Step 2: Add a new fruit to the set
fruits.add("orange")

# Step 3: Remove a fruit from the set
fruits.remove("banana")  # You can replace "banana" with any fruit in the set

# Step 4: Check if a certain fruit is in the set
fruit_to_check = "apple"
is_present = fruit_to_check in fruits  # Returns True if the fruit is in the set, otherwise False

# Display Results
print("Updated Set of Fruits:", fruits)
print(f"Is '{fruit_to_check}' in the set? {is_present}")
