n = int(input("Введите верхнюю границу диапазона: "))
numbers= set(range(2, n+1))
while numbers:
    prime = min(numbers)
    print(prime, end = "\t")
    numbers -= set(range(prime, n+1, prime))
