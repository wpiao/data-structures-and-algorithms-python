# reverse_list1 would not change input list, it creates a reversed list and return it
def reverse_list1(list):
    reversed_list = []
    for i in range(len(list) - 1, -1, -1):
        reversed_list.append(list[i])
    return reversed_list


# reverse_list2 reverse input list itself and return it
def reverse_list2(list):
    midpoint_index = len(list) // 2
    for i in range(midpoint_index):
        temp = list[i]
        list[i] = list[len(list) - 1 - i]
        list[len(list) - 1 - i] = temp
    return list
