for i in range(20):
    print(i)

arreglo = [1,2,3,4,5,6,7,8,9,10]
for a in arreglo:
    if a % 2 == 0:
        print(a)

for i in range(10):
    print(i)
    if i == 5:
        break

for i in range(10):
    if i == 5:
        continue
    print(i)

for i in range(10):
    if i == 5:
        pass
    print(i)

for i in range(10,0,-1):
    print(i)

for i in range(0,100,5):
    print(i)
