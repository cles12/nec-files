def bhadess():
    name="bhadman"
    age=70
    print("My name is " + name +" and I am " + str(age) +"years old.")
bhadess()

#adding parameters
def add_one_hundred(num):
    print (num+100)
add_one_hundred(200)

def drink (money):
    if money>=2:
        return "You got a drink!"
    else:
        return "Fool! Go get yourself some money."
print(drink(3))
print(drink(1))

def alcohol(age,money):
    if (age>=18) and (money>=10):
        return "Enjoy"
    elif (age>=18) and (money<=10):
        return "Idiot you no get money you wan chill"
    else:
        return "If I sound you err"
print(alcohol(19,11))
print(alcohol(20,3))
print(alcohol(16,5))     
        