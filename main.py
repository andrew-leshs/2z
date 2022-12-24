mass = list()
a = int(input())
for i in range(a):
    mass.append(int(input()))

control = int(input())
lis = list()
for i in mass:
    try:
        if min(mass) == abs(control - i):
            lis.append(i)
    except Exception:
        lis.append(i)
[print(i, end=" ") for i in lis]
