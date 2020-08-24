def Merge_Sort(list):
    if len(list) > 1:
        Mid = list[len(list) // 2]
        A = list[0:list.index(Mid)]
        B = list[list.index(Mid):len(list)]
        Merge_Sort(A)
        Merge_Sort(B)

        # o - always 0 - used in A because after division A always have 1 number in the list
        # l = used to indicate where to switch the numbers, 1 is added to it after first switch is done so it can switch the second num
        # i - used to signify how many rounds of checking have been done, so it checks the second B or potential more B nums as well
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


list = input("Enter a list to be sorted in ascending order: (eg. 5 2 7 5 8) \n").split()
Merge_Sort(list)
print("Sorted list: " + str(list))
