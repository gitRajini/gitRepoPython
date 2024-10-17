# Open the file for reading
with open('text.txt', 'r') as file:
    # Read the first line and ignore it
    file.readline()

    # Read the second line
    second_line = file.readline()

# Print the second line
print(second_line)

with open('text.txt', 'r') as reader:
    for _ in range(2):
        reader.readline()

    t99 = reader.readline()
    print(t99)


with open('text.txt', 'r') as file:
    file.seek(2)  # Move to the 10th byte
    print(file.read())  # Read from that position onward
