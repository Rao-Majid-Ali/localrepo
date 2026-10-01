m = int(input("Rows: "))
n = int(input("Columns: "))

array = [[i * j for j in range(n)] for i in range(m)]
print(array)