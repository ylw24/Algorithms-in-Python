#Bubble Sort - similiar to insertion sort, but without 2 parts
#unlike insertion sort, bubble sort finds the bigger number and pushes it backwards
#insertion sort compares with all the sorted number in the sorted part, to put the key in its correct slot

list = input("Enter a list to be sorted in ascending order: (eg. 5 2 7 5 8) \n").split()

#loop 
for i in range(len(list)):
    #loop: do the below until the current unsorted biggest number have been sorted to end
    #(i+1) is there to increase efficiency so code doesn't compare what has already been compared + 
    #^^it also avoids index errors so no need to try and except
    for j in range(len(list) - (i + 1)):
        key = j
        compare_target = j + 1
        #compares two number, if it's bigger, switch
        #then loops to the next two number, if bigger switch, repeat
        if float(list[key]) > float(list[compare_target]):
            list[compare_target], list[key] = list[key], list[compare_target]

print("Sorted list: " + str(list))
