def count_inversion_algo(list_to_sort):
    inv_count = 0
    sorted_list = []

    if len(list_to_sort) <= 1:
        return {'sorted_list': list_to_sort}

    med = len(list_to_sort) // 2

    left = list_to_sort[:med]
    right = list_to_sort[med:]

    result_for_left = count_inversion_algo(left)
    result_for_right = count_inversion_algo(right)
    sorted_left = result_for_left.get('sorted_list', False)
    sorted_right = result_for_right.get('sorted_list', False)
    inv_count += (result_for_left.get('inv_count', False) + result_for_right.get('inv_count', False))

    i = 0
    j = 0

    while i < len(sorted_left) and j < len(sorted_right):
        if sorted_left[i] <= sorted_right[j]:
            sorted_list.append(sorted_left[i])
            i += 1
        else:
            inv_count += med - i
            sorted_list.append(sorted_right[j])
            j += 1

    while i < len(sorted_left):
        sorted_list.append(sorted_left[i])
        i += 1

    while j < len(sorted_right):
        sorted_list.append(sorted_right[j])
        j += 1

    return {'sorted_list': sorted_list, 'inv_count': inv_count}


# test = [3, 5, 1, 4, 6, 2]
# result = count_inversion_algo(test)


result = 0
list_to_sort = []

with open('/home/kosarau/Desktop/test_inv_algo.txt') as file:
    for line in file:
        line = line.strip()
        if line.isdigit():
            list_to_sort.append(int(line))

result = count_inversion_algo(list_to_sort)

print(f'Number of inversions: {result.get("inv_count", False)}\nSorted list: {result.get("sorted_list", False)}')
