lst = [0, 6, 3, 8, 4, 1]


def find_max(lst):

    max_ = lst[0]
    for elem in lst:
        if elem > max_:
            max_ = elem
    return max_


print(find_max(lst))
