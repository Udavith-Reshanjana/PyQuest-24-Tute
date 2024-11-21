var = 10
for i in range(10):  # Outer loop runs 10 times (i = 0 to 9)
    for j in range(2, 10, 1):  # Inner loop runs for j = 2 to 9
        if var % 2 == 0:  # Checks if var is even
            continue  # Skips the rest of the loop for the current iteration
            var += 1  # This statement is never executed because `continue` skips it
    var += 1  # This increments `var` after the inner loop completes
else:
    var += 1  # Executed once after the outer loop finishes

print(var)
