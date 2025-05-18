def llm(prompt):
    return {
        "content": "Hello how can i help you",
        "role": "assistant"
    }


respone = llm(prompt="hi")
# print only the content of the response
print(respone["content"])


# decorater function
def my_decorator(func):
    def wrapper():
        print("Something is happening before the function is called.")
        func()
        print("Something is happening after the function is called.")
        return wrapper
    return my_decorator
