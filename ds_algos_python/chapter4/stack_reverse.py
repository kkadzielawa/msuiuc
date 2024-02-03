from stack import Stack

test_string = "KONRAD"

s = Stack()

for elem in test_string:
    s.push(elem)


print(s.peek_all())

d = Stack()
while s.isEmpty:
    print("HI")
    s.pop()
