#so this is a beta version. if something seems out of place or like a careless error, feel free to change it.
name_stdnt = input("Hello! What's your name? ")
print("Hello, " + name_stdnt)
print("Welcome to Fayetteville High School's GPA calculator, made by students at our very own school!")
print('       ') #prevents text from looking "clumpy"
print("Please enter in your grades using the numerical scale provided: A=4, B=3, C=2, D=1, F=0.")
print("                ") #see line 5
elective_one = input("Enter your ELECTIVE 1 grade: ")
elective_two = input("Enter your ELECTIVE 2 grade: ")
elective_three = input("Enter your ELECTIVE 3 grade: ")
sum = float(math) + float(english) + float(history) + float(science) + float(elective_one) + float(elective_two)
amount_class = 7
GPA = sum / amount_class
GPA = round(GPA, 2)
print("Here is your GPA: ")
print(GPA)
