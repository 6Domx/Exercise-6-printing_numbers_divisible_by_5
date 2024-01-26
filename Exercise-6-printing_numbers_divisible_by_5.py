# Pseudocode
# 1. Create a sample set
# 2. Evaluate the numbers in the sample set
# 3. Print those divisible by 5

# Sample number set.
number_set = [12, 25, 15, 4, 27, 5]

# For printing the sample set.
print("Sample set is: ", number_set)

# For printing those only divisible by 5.
print("These are the only number/s divisible by 5: ")
for num in number_set:
    if num % 5 == 0:
        print(num)
    
