numbers = [1, 2, 3, 4, 5]
names = ["Ali", "Vali", "Shahriyor"]

index = int(input("Введи индекс: "))
print(numbers[index])
print(numbers[-1])

scores = [70, 85, 90, 60]

for score in scores:
    print(score)

scores = [70, 85, 90, 60]
total = 0

for  score in scores:
    total += score

average = total / len(scores)

average = total / len(scores)
print("Средний балл: ", average)


hours = [2, 3, 1, 4, 2]

total_hours = 0

for hour in hours:
    total_hours += hour

average_hours = total_hours / len(hours)

print("Всего часов:", total_hours)
print("Среднее в неделю:", average_hours)
