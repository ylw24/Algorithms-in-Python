# Binary Search (Binary Chop)
# how we would guess a person's age: "Are you bigger than 25? Yes? What about 30?"
# list must be sorted
#if multiple elements are present, it will tell you where one of the element position is

import math #math module is used for math.floor to round gap to its lower integer, int(gap) would work the same

list = input("Enter a list to be searched: (eg. 5 2 7 5 8) \n").split()
key = input("Enter what element you wish to find: ")

#___________________________________________________________________________________________________________

#To sort the list, use a sorting algorithm:
#I used Merge Sort but any other sorting algorithm work the same

def Merge_Sort(list):
    if len(list) > 1:
        Mid = list[len(list) // 2]
        A = list[0:list.index(Mid)]
        B = list[list.index(Mid):len(list)]
        Merge_Sort(A)
        Merge_Sort(B)

        o = l = i = 0

        while len(A) > 1 and l != len(list):
            if A[o] > B[i]:
                list[l] = B[i]
                # l is what slot is next on the list
                l += 1
                i += 1
                while i == len(B) and l != len(list):
                    list[l] = A[o]
                    l += 1
                    o += 1
            elif A[o] <= B[i]:
                list[l] = A[o]
                l += 1
                o += 1
                while o == len(A) and l != len(list):
                    list[l] = B[i]
                    l += 1
                    i += 1

        while len(A) > i or len(B) > i:
            if B[i] > A[o]:
                list[l] = A[o]
                l += 1
                list[l] = B[i]
                break
            elif A[o] >= B[i]:
                list[l] = B[i]
                l += 1
                list[l] = A[o]

            i += 1

    return list

#____________________________________________________________________________________________

Merge_Sort(list)
print("Your new ordered list is: " + str(list))

#---------below starts the binary search algorithm, code from this comment to the first line is not necessary if list is already sorted----------

mid = math.floor(len(list)/2)
loop = True

while loop:
    if list[mid] != key:
        if list[mid] > key:
            mid = math.floor(mid/2)
            #continue is here so it doesn't conflict with the "not found"-if statement
            continue
        elif list[mid] < key:
            #checking if list is odd and even prevent bug where code doesn't know which middle to go to (this can result in a loop)
            if len(list) % 2 == 0:
               mid = math.floor(mid/2+mid)
            elif len(list) % 2 != 0:
               mid = math.ceil(mid/2 + mid)
            # continue is here so it doesn't conflict with the "not found"-if statement
            continue
    elif list[mid] == key:
        #print where the number is in the ORDERED LIST
        print("The element " + str(key) + " was found at index " + str(mid) + " in the ordered list.")
        loop = False
        break
    #this wouldn't be a conflict even if element is AT index 0 since it checks if mid==key before it checks this
    if mid == 0:
        print("The element " + str(key) + " was not found in the list")
        loop = False
        break
