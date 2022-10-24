from random import randrange

# Overwrite existing file
file = open("numbers.txt", "w")

# Make a list of random 4 digit numbers
arr = [randrange(1000,9999) for x in range(15)]

# Write in file all numbers from list
for i in arr:
    file.write(str(i)+"\n")

file.close()
print("Done!")
