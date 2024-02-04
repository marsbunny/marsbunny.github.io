#wip hahaaaaaaa
name_stdnt = input("Hello! What's your name? ")
print("Hello, " + name_stdnt)
print("Welcome to Kennedy's super duper awesome GPA calculator, made specially for super cool students like you!")
print('       ') #same reason as line 11 lol
print("Please enter in your grades using the numerical scale provided: A=4, B=3, C=2, D=1, F=0.")
print("                ") #I want a space, it can be hard to read when all the output is clumped together
print("***NOTE*** if you want an unweighted GPA calculation, enter ALL classes as STANDARD.")
print(' ')
hAP_math = input("If you take honors math, press [1], if you take AP math, press [5], if you take standard math, press [0] ")
math = input("Enter your math grade. ")
if hAP_math == 1:
    math = float(math) + 0.5
if hAP_math == 5:
    math = float(math) + 1
if hAP_math == 0:
    math = float(math)
hAP_english = input("If you take honors english, press [1], if you take AP english, press [5], if you take standard english, press [0] ")
english = input("Enter your english grade: ")
if hAP_english == 1:
    english = float(english) + 0.5
if hAP_english == 5:
    english = float(english) + 1
if hAP_english == 0:
    english = float(english)
hAP_history = input("If you take honors history, press [1], if you take AP history, press [5], if you take standard history, press [0] ")
history = input("Enter your history grade: ")
if hAP_history == 1:
    history = float(history) + 0.5
if hAP_history == 5:
    history = float(history) + 1
if hAP_history == 0:
    history = float(history)
hAP_science = input("If you take honors science, press [1], if you take AP science, press [5], if you take standard science, press [0] ")
science = input("Enter your science grade: ")
if hAP_science == 1:
    science = float(science) + 0.5
if hAP_science == 5:
    science = float(science) + 1
if hAP_math == 0:
    science = float(science)
elective_one = input("Enter your ELECTIVE 1 grade: ")
elective_two = input("Enter your ELECTIVE 2 grade: ")
elective_three = input("Enter your ELECTIVE 3 grade: ")
sum = float(math) + float(english) + float(history) + float(science) + float(elective_one) + float(elective_two) + 4
amount_class = 7
GPA = sum / amount_class
GPA = round(GPA, 2)
print("Here is your GPA: ")
print(GPA)
