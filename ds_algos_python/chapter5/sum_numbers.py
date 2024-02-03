def sum_iterative(lst):
    sum = 0
    for item in lst:
        sum += item

    return sum


def sum_recursive(lst):
    if len(lst) == 1:
        return lst[0]
    else:
        return lst[0] + sum_recursive(lst[1:])


lst = [1, 3, 5, 7, 9]
print(sum_iterative(lst))
print(sum_recursive(lst))
