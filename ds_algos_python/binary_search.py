import pdb


def binary_search_iter(lst, item):
    found = False
    first = 0
    last = len(lst) - 1

    while not found and first <= last:
        mid = (first + last) // 2
        if lst[mid] == item:
            found = True
        elif lst[mid] < item:
            first = mid + 1
        else:
            last = mid - 1

    return found


def binary_search_rec(lst, item):
    if len(lst) == 0:
        return False
    else:
        mid = len(lst) // 2
        if lst[mid] == item:
            return True
        else:
            if lst[mid] < item:
                return binary_search_rec(lst[(mid + 1) :], item)
            else:
                return binary_search_rec(lst[:mid], item)


def main():
    lst = [1, 2, 3, 4, 5, 6]
    item = 7
    found_iter = binary_search_iter(lst, item)
    found_rec = binary_search_rec(lst, item)
    print(found_iter)
    print(found_rec)


if __name__ == "__main__":
    main()
