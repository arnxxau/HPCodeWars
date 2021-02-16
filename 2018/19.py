color = int(input(""))
picture = input("")

# sitch=10mm yarn 0,01m
x = []
for i in range(0, len(picture)):
    x.append(picture[i])
y = list(set(x))

if color != len(y):
    exit()

for i in y:
    p = x.count(i)
    if (p * 0.01) > int((p * 0.01)):
        q = int((p * 0.01) + 1)
    print("-", q, "skeins of yarn", str(i))
