# 🧠 Что такое словарь?

# Словарь = данные в формате:

# ключ : значение


# Пример:

# user = {
#     "name": "Shahriyor",
#     "age": 18,
#     "is_learning_ai": True
# }

# 🔹 Как получить данные
# print(user["name"])

# 🔹 Как изменить
# user["age"] = 19

# 🔹 Как добавить
# user["city"] = "Tashkent"

# 🔥 Почему это важно для бота?

# Бот будет хранить:

# user_id → данные пользователя


# Например:

# users = {
#     12345: {"name": "Ali", "messages": 10},
#     67890: {"name": "Vali", "messages": 3}
# }


# Без словарей ты не сможешь хранить состояние.


# ---------------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------


# user = {
#     # "name": "Shahriyor",
#     # "age": 18,
#     # "goal": "Become an elite"
# }

# name = input("What is your name..... ")

# if name == user["name"]:
#     print("Welcome ", user["name"], ", Your age is ", user["age"], ", Your goal is ", user["goal"], sep='')
# else:
#     user["name"] 



# ---------------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------


# users = {
#     "Shahriyor": {"age": 18, "goal": "Become an elite"}
# }


# while True:

#     name = input("What is your name... ")

#     if name in users:
#         print("Welcome", name)
#         print("Your age is", users[name]["age"])
#         print("Your goal is", users[name]["goal"])
#     else:
#         age = int(input("Enter your age: "))
#         goal = input("Enter your goal: ")
        
#         users[name] = {"age": age, "goal": goal}
#         print("New user added!")


# ---------------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------



# import json

# try:
#     with open("users.json", "r") as file:
#         users = json.load(file)
# except:
#     users = {}

# while True:

#     name = input("What is your name (0 = exit): ")

#     if name == "0":
#         break

#     if name in users:
#         print("Welcome", name)
#         print("Your age is", users[name]["age"])
#         print("Your goal is", users[name]["goal"])
#     else:
#         age = int(input("Enter your age: "))
#         goal = input("Enter your goal: ")

# users[name] = {"age": age, "goal": goal}

#         with open("users.json", "w") as file:
#             json.dump(users, file)

#         print("New user added!")
