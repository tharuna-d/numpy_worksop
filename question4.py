#write a program to find the sum of digits of a given number'
n=int(input("Enter number"))

sum=0

for digit in str(n):
    sum=sum+int(digit)

print("Sum of digits",sum)
