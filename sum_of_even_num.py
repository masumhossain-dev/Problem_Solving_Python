num = int(input("Enter any number: "))
result = 0

for i in range(num+1):
    if (i%2 == 0):
        result = result + i

print(f"Sum of the positive numbers of 1 to {num} is: {result}")