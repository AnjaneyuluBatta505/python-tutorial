number = int(input("number: ")) # 123
count = 0
start = 1
while start <= number:
    if number % start == 0:
        count = count + 1
    start = start + 1

if count == 2:
    print("it's a prime number")
else:
    print("Not a prime number")
