# first_name = "Almas"
# last_name = "Ansari"
# age = 28
# print(f"hello my name is  {first_name} {last_name} and my age is {age}")
# print(f"""
# Hi {first_name} {last_name}
# you won a lottrey
# in jeeto pakistan
# """)

# num1 = -10
# num1 -= 40
# print(num1)

# user_input = input = int()
# age = 20
# if age > 18:
#     print("You are eligible")
# else:
#     print("you are not eligible")


# percentage = input("Enter your percentage: ")
# print(percentage)
# # explisit type conversion
# result = int(percentage)
# if result > 100:
#     print("dont add wrong percentage")
# elif result >= 90:
#     print("your grade is A++😍")
# elif result >= 80:
#     print("your grade is A+🤩")
# elif result >= 70:
#     print("your grade is A😊")
# elif result >= 60:
#     print("your grade is B🙂")
# elif result >= 50:
#     print("your grade is C🤔")
# elif result >= 40:
#     print("your grade is D😮")
# else:
#     ("Call your parents 😥")


# submision form using logical opretor
age = int(input("enter your age: "))
gender = input("enter your gender: ")

if age >= 18 and gender == "women":
    print("you are allowed to this female hackathon!")
elif age <= 18 and gender == "women":
    print("youre age is small then our requirments")
elif age >= 18 and gender == "men":
    print("sorry mens are not allowed!")
else:
    print("404 error try again ")
