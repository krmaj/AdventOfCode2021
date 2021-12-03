file = open('input', 'r')
lines = file.readlines()

increasedCount = 0
previous = int(lines[0].strip())

for line in lines:
    i = int(line.strip())
    if i > previous:
        increasedCount += 1
    previous = i

print(increasedCount)
