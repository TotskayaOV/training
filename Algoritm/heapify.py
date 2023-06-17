def sorted(sort_list):
    for i in range(int(len(sort_list)/2) -1, 0, -1):
        heapify(sort_list, len(sort_list)-1, i)

    for i in range(len(sort_list)-1, 0, -1):
        temp = sort_list[0]
        sort_list[0] = sort_list[i]
        sort_list[i] = temp
        heapify(sort_list, i, 0)
    return  sort_list

def heapify(sort_list: list, heap_size: int, root_index: int):
    largest = root_index
    left_child = 2 * root_index + 1
    right_child = 2 * root_index +2
    if left_child < heap_size and sort_list[left_child] > sort_list[largest]:
        largest = left_child
    if right_child < heap_size and sort_list[right_child] > sort_list[largest]:
        largest = right_child
    if largest != root_index:
        temp = sort_list[root_index]
        sort_list[root_index] = sort_list[largest]
        sort_list[largest] = temp
        heapify(sort_list, heap_size, largest)
    return sort_list


my_list = [2, 4, 2 , 7, 9, 1, 4, 0, 10, 4, 8, 23, 8]
print(sorted(my_list))