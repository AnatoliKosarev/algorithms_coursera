def merge_sort(list_to_sort):
    sorted_result_list = []

    # base case
    if len(list_to_sort) <= 1:
        return list_to_sort

    # find medium of list to sort
    list_med = len(list_to_sort) // 2

    left = list_to_sort[:list_med]
    right = list_to_sort[list_med:]

    # recursive calls to sort both lists
    sorted_left = merge_sort(left)
    sorted_right = merge_sort(right)

    # indices to traverse through each list
    i = 0
    j = 0

    while i < len(sorted_left) and j < len(sorted_right):
        if sorted_left[i] <= sorted_right[j]:
            sorted_result_list.append(sorted_left[i])
            i += 1
        else:
            sorted_result_list.append(sorted_right[j])
            j += 1

    # after one of the lists was exhausted - add all values left from another list to result
    # as there's nothing to compare them with
    while i < len(sorted_left):
        sorted_result_list.append(sorted_left[i])
        i += 1
    while j < len(sorted_right):
        sorted_result_list.append(sorted_right[j])
        j += 1

    return sorted_result_list


list_test = [54,26,-93,17,77,31,44,55,20]
sorted_list = merge_sort(list_test)
print(sorted_list)
