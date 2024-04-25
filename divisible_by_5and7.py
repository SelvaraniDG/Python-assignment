def divisible(n):
    for num in range(n+1):
        if num % 5 == 0  and num % 7 == 0:
            yield num

while True:
    n = int(input("Enter a number: "))
    if n <= 0:
        print("Please enter a positive number.")
    else:
        res = divisible(n)
        print("Numbers divisible by 5 and 7 between 0 and", n, ":")
        print(*res, sep=", ")
        break