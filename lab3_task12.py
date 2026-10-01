lines = []
print("Enter lines (press Enter on a blank line to finish):")

while True:
    line = input()
    if line == "":
        break
    lines.append(line)

for l in lines:
    print(l)