#!/usr/bin/python3
for number in range(10):
    for i in range(number + 1, 10):
        print("{}".format(str(number) + str(i)), end="")
        if int(str(number) + str(i)) < 89:
            print(", ", end="")
print("")
