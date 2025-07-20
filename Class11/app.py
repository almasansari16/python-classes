# class Human:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     def eat():
#         print("eating with right hand")


# class Student(Human):
#     def __init__(self , name , age , rollNum , feeStatus: bool):
#         # inheritance
#         super().__init__(name ,  age)
#         self.rollNum:int = rollNum
#         self.feeStatus: bool = feeStatus

#     def display(self):
#         print(f"{self.name}")
#         print(f"{self.age}")
#         print(f"{self.rollNum}")
#         if self.feeStatus:
#             print("fee is paid") 
#         else:
#             print("fee is pending")

#     def __str__(self):
#          return f"Student(name={self.name}, age={self.age} rollNum={self.rollNum}, feeStatus={'Paid' if self.feeStatus else 'Pending'})"        


# std1 = Student("ali", 22, 123, True)
# std1.display()

# # std2 = Student("bilal" , 456 , False)
# # std2.display()


# class Course:
#     def __init__(self, course_name):
#         self.course_name = course_name
#         self.students = []

#     def add_student(self, student):
#         self.students.append(student)
#         # print(student)

# ai_course = Course("AI")
# ai_course.add_student(std1)
# print(ai_course.students[0])


# class Teacher(Human):
#     def __init__(self ,  name , age , salary):
#         super().__init__(name , age)
#         self.salary = salary

#     # polymorphisum
#     def eat(self):
#         print("eating with left hand")  

# teah1 = Teacher("salma" , 50 , 50000)  
# teah1.eat()


class BankAccount():
    def __init__(self , name , account_no , balance):
        self.name = name
        self.account_no = account_no
        self.__balance = balance

    def get_Balance(self , account_no , balance):
        if account_no == account_no:
            return balance
        else:
            return "invalid account number"

user1 = BankAccount("Almas", 123456, 1000)
user1.get_Balance("123456" , 1000)
