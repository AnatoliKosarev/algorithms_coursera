from random import randrange


def partition(start: int, end: int, list_to_part: list) -> int:
    # choose random index for pivot
    random_index = randrange(start, end)
    # swap first element of the list with pivot
    if random_index != start:
        list_to_part[start], list_to_part[random_index] = list_to_part[random_index], list_to_part[start]
    # choose boundary index for values < and > than pivot as next index after pivot
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

    pivot_index = partition(start, end, list_to_sort)
    # recursively call function for the first (el < pivot) and second (el > pivot) parts of the partitioned list
    quicksort(start=start, end=pivot_index, list_to_sort=list_to_sort)
    quicksort(start=pivot_index + 1, end=end, list_to_sort=list_to_sort)

    return list_to_sort


# test = [2, 5, 6, 1, 4, 6, 2, 4, 7, 8]
test = [2, 5, 6, 1]
print(quicksort(start=0, end=len(test), list_to_sort=test))
