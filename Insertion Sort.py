#Insertion Sort (card shuffle - this is how you would sort your cards)
#There's two parts, sorted and unsorted, the front is sorted, the back of the list is unsorted

list = input("Enter a list to be sorted in ascending order: (eg. 5 2 7 5 8) \n").split()


for i in range(len(list)-1):
    # define what key and the compare_target is
    # key is initially the 2nd number in the list
    # compare_target is always the number before the key
    key = i + 1
    compare_target = key - 1
    while float(list[key]) < float(list[compare_target]):
        list[compare_target], list[key] = list[key], list[compare_target]
        #keep comparing until key is greater than compare_target
        key -= 1
        compare_target -= 1
        #if compare_target becomes -1 (which means key is at 0: the beginning) stop
        if compare_target == -1:
            break

print("Sorted List: " + str(list))

