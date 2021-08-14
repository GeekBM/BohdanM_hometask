n = abs(int(input("Enter a positive integer ")))
m = n % 10
while n >= 1:
    n = n // 10
    if n % 10 > m:
        m = n % 10
    if n > 9:
        continue
    else:
        print("Maximum digit in the number ", m)
        break
