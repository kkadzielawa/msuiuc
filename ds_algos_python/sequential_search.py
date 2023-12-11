def sequential_search(lst, item):
    found = False
    pos = 0
    while pos < len(lst) and found is False:
        if lst[pos] == item:
            found = True
        else:
            pos += 1

    return found


def main():
    lst = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    item = 13
    found = sequential_search(lst, item)

    print(found)


if __name__ == "__main__":
    main()
