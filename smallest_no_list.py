numbers = input("Enter numbers separated by spaces: ")
numbers_list = [int(num) for num in numbers.split()]

smallest = numbers_list[0]
i = 1
while i < len(numbers_list):
    if numbers_list[i] < smallest:
        smallest = numbers_list[i]
    i += 1

print(f"The smallest number in the list is {smallest}")
