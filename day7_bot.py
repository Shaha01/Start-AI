# import json

# try:
#     with open("bot.json", "r") as file:
#         bot = json.load(file)
# except:
#     bot = {}

#     name = input("What is your name...")
    
# if name in bot:
#     print("Hello", name)
# else:
#     bot[name] = {"messages": 0}

#     with open("bot.json", "w") as file:
#         json.dump(bot, file)

#     print("New user added!")
    

# while True:
#     word = input("exit or Write...")
#     bot[name] = {"sum": + 1}

#     if word == "exit":
#         print("Messages =", sum)
#         break

#     if word == "Hello":
#         print("Hello, Hello")
#     else:
#         answer = input("Is it your age, goal, surname?")
        
#         if answer == "age":
#             bot[name]["age"] = word 
#             print("Ok")
#         if answer == "goal":
#             bot[name]["goal"]= word
#             print("Ok")
#         if answer == "surname":
#             bot[name]["surname"]= word
#             print("Ok")
#         else:
#             bot[name]["money"] = word
#             print("it's your money")
        
#     word = input("How are u? ...")

#     if word == "ok":
#         print("It's good")
#     elif word == "bad":
#         answer = print("What happened? ...")
#         bot[name] = {"incident"}
#     else:
#         print("I don't know this word")
    
#     with open("bot.json", "w") as file:
#         json.dump(bot, file)
        

# print("Name = ", bot[name])
# print("Age = ", bot[name]["age"])
# print("Goal = ", bot[name]["goal"])
# print("Money = ", bot[name]["money"])
# print("Incident = ", bot[name]["incident"])



# ==============================================================================================================================
# ==============================================================================================================================
# ==============================================================================================================================
# ==============================================================================================================================
# ==============================================================================================================================



import json

# ---------- Загрузка данных ----------
try:
    with open("bot.json", "r") as file:
        bot = json.load(file)
except:
    bot = {}

# ---------- Вход пользователя ----------
name = input("What is your name: ").strip().lower()

if name not in bot:
    bot[name] = {
        "messages": 0,
        "age": None,
        "goal": None,
        "surname": None,
        "money": None,
        "incident": None
    }
    print("New user added!")
else:
    print("Welcome back,", name)

# ---------- Чат ----------
while True:
    word = input("Write something (exit to quit): ").strip().lower()

    if word == "exit":
        print("Total messages:", bot[name]["messages"])
        break

    # увеличиваем счётчик сообщений
    bot[name]["messages"] += 1

    # простая логика
    if word == "hello":
        print("Hello, hello 😄")

    elif word in ["age", "goal", "surname", "money"]:
        value = input(f"Enter your {word}: ")
        bot[name][word] = value
        print("Saved!")

    elif word == "bad":
        incident = input("What happened? ")
        bot[name]["incident"] = incident
        print("I hope everything gets better.")

    elif word == "ok":
        print("Good to hear 👍")

    else:
        print("I don't understand this word.")

    # сохраняем после каждого шага
    with open("bot.json", "w") as file:
        json.dump(bot, file, indent=4)

# ---------- Вывод данных ----------
print("\nYour data:")
for key, value in bot[name].items():
    print(f"{key}: {value}")
