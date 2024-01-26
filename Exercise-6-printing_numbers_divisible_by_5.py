# Pseudocode
# 1. Create a sample set
# 2. Evaluate the numbers in the sample set
# 3. Print those divisible by 5

number_set = [12, 25, 15, 4, 27, 5]

print("Sample set is: ", number_set)

print("These are the only number/s divisible by 5: ")
for num in number_set:
    if num % 5 == 0:
        print(num)
    
