num = int(input("Enter a number:"))

num>1
for i in range(2,int(num**0.5) +1):
    if num % i == 1:
        print(f"{num} isn't a prime number")
        break
    else: 
        print(f"{num} is a prime number")

else: 
    print(f"{num} isn't a prime number")