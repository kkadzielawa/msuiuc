from stack import Stack


def divide_by_two(n):
    s = Stack()

    while n > 0:
        rem = n % 2
        s.push(rem)
        n = n // 2

    string = ""
    while not s.isEmpty():
        string = string + str(s.pop())

    return string


print(divide_by_two(129))
