x = []
for i in range(1, 11):
    x.append(int(input()))


y = []
for i in x:
    y.append(i % 42)

z = set(y)

print(len(z))
