n = int(input("Enter a number to find the sum of natural numbers up to: "))

sum_n = 0
for i in range(1, n + 1):
    sum_n += i

print("The sum of natural numbers up to", n , "is" , sum_n)
