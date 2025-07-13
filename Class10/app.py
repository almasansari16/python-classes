# def is_valid_age(age: int) -> bool:
#     if age > 18:
#         return True
#     else:
#         return False


# print(is_valid_age(22))

# name = "John"
# print(id(name))
# name += "jane"
# print(name)
# print(id(name))  # Output: Jane

# sring is immutable


# dict
# std = {
#     "name": "John",
#     "age": 30,
#     "gender": "male"
# }
# print(std["age"])

# # list
# fruits = ["apple", "banana", "cherry"]
# print(fruits[0])

# # set
# # set is unordered collection of unique elements

# traffi_light: frozenset = frozenset({"red", "green", "yellow"})
# print(traffi_light)  # Output: {'red', 'green', 'yellow'}


# short hand if else
# age = 25
# result = "you are allowed" if age >= 18 else "you are not allowed"
# print(result)  # Output: you are allowed


# s = {1, 2, 3}
# s.discard(10)
# print(s)


# s = {1, 2, 3}
# s.add(2)
# print(s)


# set1 = {1, 2, 3, 4}
# set2 = {3, 4, 5}
# print(set1.difference(set2))  # ➜ {1, 2}

# OOP
# class is a blue print:


# class Car:
#     def start(self):
#         print("Car is starting")


# my_car = Car()
# my_car.start()  # ➜ Car is starting


# class Animal:  # Base class (Parent)
#     def speak(self):  # Polymorphism
#         print("Animal speaks")


# class Dog(Animal):  # Inheritance
#     def speak(self):
#         print("Dog barks")


# class Cat(Animal):
#     def speak(self):
#         print("Cat meows")


# # Object Creation
# a = Animal()
# d = Dog()
# c = Cat()

# a.speak()  # ➜ Animal speaks
# d.speak()  # ➜ Dog barks
# c.speak()  # ➜ Cat meows


class House:
    def __init__(self, address, price, yards):
        self.address = address
        self.price = price
        self.yards = yards

    def display(self):
        print(f"Address: {self.address}")
        print(f"Price: {self.price}")
        print(f"Yards: {self.yards}")
        print("House is beautiful")

    def extra_properties(self, road_facing, parking, corner_appartment):
        self.road_facing = road_facing
        self.parking = parking
        self.corner_appartment = corner_appartment

    def show_extra(self):
        print("Road Facing:", self.road_facing)
        print("Parking:", self.parking)
        print("Corner Apartment:", self.corner_appartment)


# h1 = House("123 Main St", 500000, 240)
# h1.display()
# h1.extra_properties(True, True, False)
# h1.show_extra()


class Apartment(House):
    def __init__(self, address, price, yards, num_bedrooms):
        super().__init__(address, price, yards)
        self.num_bedrooms = num_bedrooms

        def display(self):
            super().display()
            print(f"Number of Bedrooms: {self.num_bedrooms}")
            print("Apartment is cozy")


a1 = Apartment("456 Elm St", 300000, 100, 3)
a1.display()  # ➜ Address: 456 Elm St, Price: 300000
