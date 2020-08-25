# Shell Sort
import math

list = input("Enter a list to be sorted in ascending order: (eg. 5 2 7 5 8) \n").split()

N = len(list)
gap = math.floor(N / 2)

key = 0
compare_target = key + gap
end = compare_target
rounds = 1

while compare_target < N and gap != 0:

    while float(list[key]) > float(list[compare_target]):
        list[compare_target], list[key] = list[key], list[compare_target]
        if key - gap <= -1:
            break
        key -= gap
        compare_target = key + gap
        if list[key] <= list[compare_target]:
            compare_target = end + 1
            key = compare_target - gap
            end = compare_target

            if end >= N:
                gap = math.floor(gap / 2)
                key = 0
                compare_target = key + gap
                end = compare_target
                rounds += 1

    if end >= N - 1:
        gap = math.floor(gap / 2)
        key = 0
        compare_target = key + gap
        end = compare_target
        rounds += 1

    if float(list[key]) <= float(list[compare_target]):
        key += 1
        compare_target = key + gap
        end = compare_target

print("Sorted list: " + str(list))
