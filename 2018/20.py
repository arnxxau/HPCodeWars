x = input("")
names = x.split(" ")
namesIndex = bytearray
overtakes = []
y = "str"


while 1 != 0:
    if y != "":
        y = input("")
        overtakes.append(y)
    else:
        break

for p in overtakes:
    if "overtakes" in p:
        t = p.split(" overtakes ")

        pos1 = names.index(t[0])
        pos2 = names.index(t[1])
        names[pos1] = t[1]
        names[pos2] = t[0]

for n in names:
    print(n)
