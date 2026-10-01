items = input("Enter comma-separated 4-digit binary numbers: ").split(',')
result = [num for num in items if int(num, 2) % 5 == 0]

print(",".join(result))