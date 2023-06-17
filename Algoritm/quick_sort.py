def quick_sorted(sort_list: list, start_point: int, end_point: int) -> list:
    left_point = start_point
    right_point = end_point
    pivot = sort_list[int((start_point + end_point) / 2)]
    while left_point <= right_point:
        while sort_list[left_point] < pivot:
            left_point += 1
        while sort_list[right_point] > pivot:
            right_point -= 1
        if left_point <= right_point:
            if left_point < right_point:
                temp = sort_list[left_point]
                sort_list[left_point] = sort_list[right_point]
                sort_list[right_point] = temp
            left_point += 1
            right_point -= 1
    if left_point < end_point:
        quick_sorted(sort_list, left_point, end_point)
    if start_point < right_point:
        quick_sorted(sort_list, start_point, right_point)
    return sort_list

my_list = [2, 4, 2 , 7, 9, 1, 4, 0, 10, 4, 8, 23, 8]
print(quick_sorted(my_list, 0, len(my_list)-1))