import asyncio


# recursive

# def add_two_numbers(num1: int, num2: int) -> int:
#     return num1 + num2


# result = add_two_numbers(2, 2)


# def my_function(**keyargs) -> tuple:
#     return keyargs  # type: ignore


# result = my_function(a=1, b=2, c=3)
# print(result)


# # lambda function
# def abc(p1, p2): return p1 + p2


# print(abc(2, 3))

# # recursive function

# def factorial(n):
#     if n == 1:
#         return 1
#     else:
#         return n * factorial(n - 1)


# print(factorial(5))  # Output: 120


# def my_recursive(n):
#     if n == 0:
#         print(f"Base case reached, n is {n}")
#         return 1
#     else:
#         print(f"Recursive case reached, n is {n}")
#         return n * my_recursive(n-1)


# my_recursive(5)


# genrator function
# def my_range(start: int, end: int , step : int):

# with open('data.py', 'w') as file:
#     file.write("hello world")


# async def say_hello():
#     print("Hello...")
#     await asyncio.sleep(2)  # Simulate a delay
#     print("...world!")

# # Run the async function
# asyncio.run(say_hello())


# def my_decorator(func):
#     def wrapper():
#         print("Function is about to run.")
#         func()
#         print("Function has finished running.")
#     return wrapper


# @my_decorator
# def say_hello():
#     print("Hello!")


# say_hello()


# error handling types
# developemnet time
# q/a time
# logical error
# production time


# try , except , else , finally

# try:
#     result = 10 / 0
#     print("Result is:", result)
# except ZeroDivisionError:
#     print("Error: You can't divide by zero!")


# try:
#     num = int(input("Enter a number: "))
#     result = 10 / num
#     print("Result:", result)
# except ValueError:
#     print("Error: Please enter a valid number.")
# except ZeroDivisionError:
#     print("Error: Division by zero is not allowed.")


# try:
#     file = open("data.txt", "r")
#     content = file.read()
#     print(content)
# except FileNotFoundError:
#     print("Error: File not found.")
# finally:
#     print("Finished trying to read the file.")


# try:
#     x = 10 / 0
# except ValueError:
#     print("Value error occurred")
# except ZeroDivisionError:
#     print("Cannot divide by zero")
# finally:
#     print("Cleanup done")
# print("python".capitalize())
# print(10 // 3)
# print('python'[::-1])


# x = [1, 2, 3]
# print(x * 2)


# x = 10


# def foo():
#     print(x)


# foo()


# def f(x, y=[]):
#     y.append(x)
#     return y


# print(f(1))
# print(f(2))

# x = 5


# def foo():
#     # global x
#     x = x + 1
#     print(x)  # prints 5


# foo()
# def g():
#     return


# print(g() is None)


# funcs = []
# for i in range(3):
#     funcs.append(lambda: i)

# results = [f() for f in funcs]
# print(results)

# print(10/0)
numbers = [1, 2, 3, 4]

even_squares = {x: x*x for x in numbers if x % 2 == 0}
print(even_squares)
