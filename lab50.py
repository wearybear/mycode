#!/usr/bin/env python3

# part1 Read the content of the Dracula novel as a file object.
with open("dracula.txt", "r") as foo:
    # part2 loop over every line in Dracula, print each line out!
    for line in foo:
        print(line)

    # part3 Actually, fix that for loop... only print out the line if it has the word vampire in it!
    for line in foo:
        if "vampire" in line:
            print(line)

    # part4 If you didn't already, make sure it prints the line no matter what case vampire is!
    for line in foo:
        if "vampire" in line.lower():
            print(line)

# part5 Count that up! How many lines contain the word vampire?
count = 0
with open("dracula.txt", "r") as foo:
    for line in foo:
        if "vampire" in line.lower():
            count += 1
print(count)

# part6 Take the lines from Dracula that have vampire in it and write them to a second file named vampytimes.txt.
counter = 0
with open("dracula.txt", "r") as foo:
    with open("vampytimes.txt", "w") as fang:
        for line in foo:
            if "vampire" in line.lower():
                print(line)
                counter += 1
                fang.write(line)

print(counter)

