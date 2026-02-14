def chet(a):
    sum = 0
    for i in range(a):
        if i % 2 == 0:
            sum += 1
    print(sum)
    
def nechet(a):
    sum = 0
    for i in range(a):
        if i % 2 == 1:
            sum += 1
    print(sum)

def delit(a):
    for i in range(11):
        i += 1
        if a % i == 0:
            print(i)

def bukv(a):
    for i in range(len(a)):
        print(a[i] * (i + 1))




answer = input(
    "Узнать сколько четных = 1\nУзнать сколько нечетных = 2 \nУзнать на какие цифры делится число = 3 \nНаписать первую букву один раз, вторую два раза и тд = 4 \nВыход = 5 \n"
    )


if answer == "1":
    a = int(input("A = "))
    chet(a)
if answer == "2":
    a = int(input("A = "))
    nechet(a)
if answer == "3":
    a = int(input("A = "))
    delit(a)
if answer == "4":
    a = input("A = ")
    bukv(a)
if answer == "5":
    print("Goodbye")