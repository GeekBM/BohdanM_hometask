n = int(input("Enter a positive integer "))
max = 0
while n > 0:
    if n % 10 > max:
        max = n % 10
        if max == 9:
            break
    n = n // 10
print(f'Max digit in number {max}')
