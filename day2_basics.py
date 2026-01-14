print("Я начал путь в AI и ML(Машинное обучение). День 2.")


name = "Shahriyor  ="
age = int(input("Сколько тебе лет?  =  "))
hours_per_week = int(input("Сколько времени уделяешь изучению ИИ  =  "))

learning_ai = True



print("\n ---- ИНФО ----")
print(f"Возраст: {age}")
print(f"Часов в неделю: {age}")
print(f"Учу AI: {learning_ai}")


print("\n ---- AНАЛИЗ ----")
if hours_per_week >= 2:
    print("Режим норм, идём к цели 💪")
else:
    print("Нужно больше фокуса")

if age >= 18:
    print("Можно идти в большой мир")
else:
    print("Ещё готовимся")


for i in range(5):
    print("Учусь AI", i)


count = 0

while count < 3:
    print(f"Дальше ")
    count += 1

for i in range(10):
    print(f"", i)

num = 0

while num != 5:
    print(f"Не то, Нужен 5 ")
    num = int(input("Введи 5 -> "))