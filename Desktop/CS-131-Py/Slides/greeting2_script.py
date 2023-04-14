import box
#import guess
from random import randint


greetings = ["おはようございます", "Buenos días", "Bom Dia",
             "Bonjour", "Xin chào", "صبح بخیر"]
groceries = ["half & half", greetings, "kitty litter", "yoghurt",
             "frozen peas", "crackers", "hummus", "lentils", "sunbutter",
             "strawberry jam"]
chores = ["dishes", "laundry", "bathroom trash cans", "kitchen trash",
          "change sheets", "kitty litter", "vacuum", groceries]

print(greetings[0], groceries[0], chores[0])
print(greetings[1], groceries[1], chores[1])
greetings.append("Hello")
print(greetings)
greetings.insert(1,"Ciao")
print(greetings)

def greet_select() -> str:
    '''returns random geeting language selection'''
    result = ""
    i = randint(1,len(greetings))
    result = greetings[i]   
    return result
    

##if __name__=="__main__":
##    name = input("What is your name?")
##    greeting = greet_select()
##    box.box_string(greeting + " " + name)
