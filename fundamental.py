# # 1. Assign function to Variable
# def plus_one(num):
#     return num+1

# add_one = plus_one

# # call
# print(add_one(2))

# # 2. Define function in other function
# def add_one(num):
#     def plus_one(num):
#         return num + 1

#     result = plus_one(num)
#     return result

# # call
# print(add_one(2))

# # 3. Pass function as Agruments to other Functions

# def plus_one(num):
#     return num + 1

# def function_call(func):
#     return func(2)
    

# print (function_call(plus_one))

# # 4. Function returning other function

# def hello_function():
#     def say_hi():
#         return "Hi"
#     return say_hi

# hello = hello_function()
# print(hello())

# # 5. Nested function have access to the enclosing function's variable scope
# def print_message(msg):
#     "Enclosing Function"
#     def message_sender():
#         "Nested Function"
#         print(msg)

# print_message("abc")


