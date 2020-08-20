list = input("Enter a list to be sorted in ascending order: (eg. 5 2 7 5 8) \n").split()

try:
    for i in range(len(list)):
        #define what key and the compare_target is
        #key is initially the 2nd number in the list
        #compare_target is always the number before the key
        key = list[i+1]
        compare_target = list[int(list.index(key))-1]
        # compare key with the compare target (number before the key)
        #if key is smaller or equal than compare_target,
        #switch positions of key and compare_target
        #the compare_target changes to the number before the key (because key changed number)
        #keep switching places with the number before if key is smaller
        #until key is no longer smaller than the number before, key becomes the next unsorted number in the list
        #process loops until all numbers are in their position and indexerror occur which prints out the final sorted list
        while float(key) <= float(compare_target):
            a, b = list.index(key), list.index(compare_target)
            list[b], list[a] = list[a], list[b]
            if list.index(key) == 0:
               break
            else:
               compare_target = list[int(list.index(key))-1]
except IndexError:
    print("Sorted List: " + str(list))
