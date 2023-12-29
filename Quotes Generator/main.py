import random
import quote

def generate_quotes():
    print("1. Inspirational")
    print("2. Motivational")
    print("3. Funny")
    print("4. Love")
    print("5. Life")
    
    choice = int(input("Entery Your Choice : "))
    if choice == 1:
        search_term = "Inspirational"
    elif choice == 2:
        search_term = "Motivational"
    elif choice == 3:
        search_term = "Funny"
    elif choice == 4:
        search_term = "Love"
    elif choice == 5:
        search_term = "Life"
    else:
        print("Invalid Choice : ")
        return
    
    quotes = quote.quote(search_term)
    num = int(input("Enter the No. of quotes to generate : "))
    
    for i in range(num):
        print(i+1, ".", random.choice(quotes)['quote'])
    
generate_quotes()