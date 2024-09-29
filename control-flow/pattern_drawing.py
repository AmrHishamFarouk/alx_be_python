size = int(input("Enter the size of the pattern:"))

num = 0
while num < size :
    for number in range(size):
        print("*", end="")
    print("")
    num += 1