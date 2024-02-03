from stack import Stack

string = "{{"


def is_balanced(string):
    s = Stack()

    for item in string:
        if item == "{":
            s.push(item)
        else:
            s.pop()

    print(s.peek_all())

    if s.isEmpty():
        return "OK"
    else:
        return "NOT OK"


print(is_balanced(string))
