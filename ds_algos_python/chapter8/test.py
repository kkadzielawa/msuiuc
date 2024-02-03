lst = [[1, "K"], [3, "N"], [5, "A"], [6, "D"], [2, "O"], [4, "R"]]

lst.sort(key=lambda x: x[0])

s = ""
for elem in lst:
    s += elem[1]

print(s)
