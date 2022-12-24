mass = list()
a = int(input())
for i in range(a):
    mass.append(int(input()))

control = int(input())
max_ = float('inf')
min_ = 0
for i in mass:
    if control > i > min_:
        min_ = i
    elif control < i < max_:
        max_ = i
print(f"{min_} {max_}")