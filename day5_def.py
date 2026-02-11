# def say(a, b):
#     print(a + b)
#     print(a - b)
#     print(a * b)   

#     if(b == 0):
#         b += 1
#     elif(a == 0):
#         a += 1

#     print(a / b)

# a = int(input("A = "))
# b = int(input("B = "))

# say(a, b)

# ------------------------------------------------------------------------------------------------

# def num(n):
#     if(n % 2 == 0):
#         print("N = четный")
#     else:
#         print("Не четный ")

# n = int(input("N = "))

# num(n)


# ---------------------------------------------------------------------------------------------------

# months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

# n = int(input("Day = ? "))

# for i in range(len(months)):
#     if(n > months[i]):
#         n = n - months[i]
#     else:
#         print(n, months[i])
    

months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
month_names = [
    "Января", "Февраля", "Марта", "Апреля",
    "Мая", "Июня", "Июля", "Августа",
    "Сентября", "Октября", "Ноября", "Декабря"
]

n = int(input("Day = "))

while True:   # бесконечный цикл

    n = int(input("Day (0 = выход): "))

    if n == 0:
        break

    for i in range(len(months)): # len это количество месяцев 
        if n > 365:
            print("В году 365 дней")  
            break
        elif n > months[i]:
            n -= months[i]
        else:
            print(n, month_names[i])
            break
