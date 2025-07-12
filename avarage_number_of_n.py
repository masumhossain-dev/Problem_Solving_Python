num = int(input("Enter any number: "))
result = 0
num_list = []

for i in range(num+1):
    result = result + i
    num_list.append(i)

size = len(num_list)
average = result / size

print(f"Sum of the 1 to {num}: {result}")
print(f"Average of these numbers is: {average}")
