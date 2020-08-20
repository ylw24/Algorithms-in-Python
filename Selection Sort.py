unsorted_list = input("Enter a list to be sorted in ascending order: (eg. 5 2 7 5 8) \n").split()
sorted_list = []
smallest_num = ''
loop = True

while loop:
    #keep running this code until all numbers are sorted
    try:
        #first define the smallest number as the first number in the unsorted list
        smallest_num = float(unsorted_list[0])
        #search through the unsorted_list number by number
        for i in range(len(unsorted_list)):
            #if a number is smaller or equal to the CURRENT smallest number, the number will BECOME the current smallest number
            if float(unsorted_list[i]) <= float(smallest_num):
                smallest_num = unsorted_list[i]
            #if a number is bigger than the CURRENT smallest number, keeo searching through the unsorted list for a potential smaller number
            elif float(unsorted_list[i]) > float(smallest_num):
                pass
        #After a round of the unsorted list is searched, add the smallest number to the sorted list, and delete from the unsorted list
        sorted_list.append(smallest_num)
        unsorted_list.remove(smallest_num)
        #search of for the smallest number in the unsorted list continues until all the numbers have been sorted and added to the sorted list

        #when all numbers have been added to the sorted list, there are no more numbers in the unsorted list
        #therefore an indexerror will occur when it tries to seach the unsorted list again for smallest number

        #when the indexerror occurs, stop looping and print out the sorted list
    except IndexError:
        loop = False

print("Sorted List: " + str(sorted_list))
