import re

def calculate_expression(expression):
    try:
        result = eval(expression)
        return result
    except Exception as e:
        print(f"Error : {e}")
        return None
    
print("Hello, I am a Smart Calculator, How may I Help You?")
while True:
    user = input("You : ")
    
    if user.lower() == "quit":
        print("Exiting")
        break
    
    result = calculate_expression(user)
    
    if result is not None:
        print("Calculator : ", result)
    else:
        print("Calculator : Please enter a Valid mathematical Expression.")