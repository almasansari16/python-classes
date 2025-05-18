# data types

# first_name: str = "Almas"
# age: int = 25
# salary: float = 10000.00
# is_married: bool = False
# friends: list[str] = ['a', 'b', 'c', 'd', 4]


# def greet(name: str, age: int) -> str:
#     return f"Hello , {name} {age}"


# greet("almas", 25)

# dictonries
std1: dict[str, str | int] = {
    "name": "almas",
    "age": 25,
    "rollnum": 990,
    "class": "PIAIC batch 71"
}

# print(f"""name: {std1['name']}
#  age: {std1['age']}
#  rollnum :{std1['rollnum']} """)

for key, value in std1.items():
    print(f"{key}: {value}")
