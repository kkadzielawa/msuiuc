def reverse_lst(lst):
    if len(lst) == 1:
        return [lst[0]]
    else:
        return [lst[len(lst) - 1]] + reverse_lst(lst[0 : len(lst) - 1])


lst = [1, 3, 5, 7, 9]

print(reverse_lst(lst))
