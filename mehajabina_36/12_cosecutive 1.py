lines_with_consecutive_ones = []

file = open("file1.1.txt", "r")
for line in file:
    if "11" in line:      # Check for two consecutive 1's
        lines_with_consecutive_ones.append(line.strip())

file.close()

print(lines_with_consecutive_ones)

print("Lines containing two consecutive '1's:")
for line in lines_with_consecutive_ones:
    print(line)
