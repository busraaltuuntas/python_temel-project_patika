from re import X


x= [[1, 2], [3, 4], [5, 6, 7]]
x= x[::-1]

for i in range(len(x)):
    (x[i])=(x[i])[::-1]
print(x)

