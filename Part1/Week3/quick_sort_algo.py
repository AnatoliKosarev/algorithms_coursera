from random import randrange

COUNT_COMPARE = 0


def partition(start: int, end: int, list_to_part: list) -> int:
    # 1. choose pivot as first element
    # pivot_index = start

    # 2. choose pivot as last element
    # pivot_index = end - 1

    # 3. choose median out of 3 as pivot
    list_length = end - start

    if list_length >= 3:
        if list_length % 2 == 0:
            median_ind = int(list_length / 2) - 1 + start
        else:
            median_ind = list_length // 2 + start

        if (list_to_part[start] < list_to_part[median_ind] < list_to_part[end - 1] or
                list_to_part[start] > list_to_part[median_ind] > list_to_part[end - 1]):
            pivot_index = median_ind
        elif (list_to_part[median_ind] < list_to_part[start] < list_to_part[end - 1] or
                list_to_part[median_ind] > list_to_part[start] > list_to_part[end - 1]):
            pivot_index = start
        elif (list_to_part[median_ind] < list_to_part[end - 1] < list_to_part[start] or
                list_to_part[median_ind] > list_to_part[end - 1] > list_to_part[start]):
            pivot_index = end - 1
        else:
            raise Exception
    else:
        pivot_index = start

    # 4. choose random index for pivot
    # pivot_index = randrange(start, end)
    # # swap first element of the list with pivot
    if pivot_index != start:
        list_to_part[start], list_to_part[pivot_index] = list_to_part[pivot_index], list_to_part[start]
    # # choose boundary index for values < and > than pivot as next index after pivot
    i = start + 1

    for j in range(i, end):
        if list_to_part[j] <= list_to_part[start]:
            if i != j:
                # if element < than pivot swap it with previous boundary element
                list_to_part[i], list_to_part[j] = list_to_part[j], list_to_part[i]
            # increment boundary index so that it points to the first value bigger than pivot
            i += 1

    if start != i - 1:
        # after list is partitioned swap pivot with the last element smaller than pivot
        list_to_part[start], list_to_part[i - 1] = list_to_part[i - 1], list_to_part[start]

    # return pivot index
    return i - 1


def quicksort(start: int, end: int, list_to_sort: list) -> list:
    # base case
    if end - start <= 1:
        return list_to_sort

    global COUNT_COMPARE
    COUNT_COMPARE += end - start - 1
    pivot_index = partition(start, end, list_to_sort)
    # recursively call function for the first (el < pivot) and second (el > pivot) parts of the partitioned list
    quicksort(start=start, end=pivot_index, list_to_sort=list_to_sort)
    quicksort(start=pivot_index + 1, end=end, list_to_sort=list_to_sort)

    return list_to_sort


# test = [2, 5, 6, 1, 4, 6, 2, 4, 7, 8]
# test = [2, 5, 6, 1]
test = []
with open('/home/kosarau/Desktop/test_algo_data.txt') as file:
    for line in file:
        line = line.strip()
        if line.isdigit():
            test.append(int(line))

print(quicksort(start=0, end=len(test), list_to_sort=test))
print(COUNT_COMPARE)
