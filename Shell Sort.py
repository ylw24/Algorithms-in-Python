# Shell Sort
#much like insertion sort, except skips every line
#unstable
#efficiency depends on the list that is being sorted

import math #math module is used for math.floor to round gap to its lower integer, int(gap) would work the same

list = input("Enter a list to be sorted in ascending order: (eg. 5 2 7 5 8) \n").split()

N = len(list)
gap = math.floor(N / 2)

#initialize some variables
key = 0
compare_target = key + gap
end = compare_target
rounds = 1

#keep looping if key is comparing to a number that is not greater than the list size AND if gap isn't smaller than
while compare_target < N and gap >= 0:
    
    #shile key is bigger than compare_target, swap its positions
    while float(list[key]) > float(list[compare_target]):
        list[compare_target], list[key] = list[key], list[compare_target]
        #if you can check its position before, previous key becomes the comparison target, and checks if the number is smaller/bigger
        if key - gap <= -1:
            break
        key -= gap
        compare_target = key + gap
        #if the number is smaller (or equal to) the compare_target, compare from what was last left off (which is marked by the variable 'end')
        if list[key] <= list[compare_target]:
            compare_target = end + 1
            key = compare_target - gap
            end = compare_target

            #this is here as a backup which prevents index error for numbers like this: 14 18 19 37 23 40 29 30 11
            #notice how it's "N" not "N-1"
            if end >= N:
                gap = math.floor(gap / 2)
                key = 0
                compare_target = key + gap
                end = compare_target
                rounds += 1
    
    #if it has sorted all the numbers in the list till end, divide gap is halved the size and comparison continues
    if end >= N - 1:
        gap = math.floor(gap / 2)
        key = 0
        compare_target = key + gap
        end = compare_target
        rounds += 1

    #if key is smaller or equal to the compare_target, no swaping is necessary and checks the next two set of numbers
    if float(list[key]) <= float(list[compare_target]):
        key += 1
        compare_target = key + gap
        end = compare_target

print("Sorted list: " + str(list))
