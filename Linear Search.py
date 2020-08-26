# Linear Search
# search through each element for the key until key is found or list is exhausted

list = input("Enter a list to be searched: (eg. 5 2 7 5 8) \n").split()
key = input("Enter what element you wish to find: ")
print("")

for position in range(len(list)):
    if position >= len(list) - 1:
        print("Your element was not found in the list")
    elif list[position] != key:
        continue
    elif list[position] == key:
        print("The element " + str(key) + " was found at index " + str(position))
        break
