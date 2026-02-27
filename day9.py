n = int(input("Из скольки чисел должен состоять массив?"))

arr = [0] * n
sump = 0
minus = 0

for i in range(n):
    value = int(input("Value =  "))
    arr[i] = value
    if arr[i] > 0:
        sump += 1
    elif arr[i] < 0:
        minus = arr[i] + minus 

print("Количество положительных чисел ", sump)
print("Сумма отрицательных чисел ", minus)



