import time

def print_floating_text(text):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(0.06)
    print()
    
print_floating_text("Hi I'm Rifqan Zalbina")
time.sleep(1)
print_floating_text("I am Computer Science Student ")
time.sleep(1)
print_floating_text("I Love Coding 💓")