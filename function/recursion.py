
# def greater(a,b,c):
#     if a>b and a>c:
#         return a
#     elif b>a and b>c:
#         return b
#     else:
#         return c
# a = int(input("enter the no. = "))
# b = int(input("enter the no. = "))
# c = int(input("enter the no. = "))

# print(f"the greatest no. is {greater(a,b,c)}")        




#now make the program for the celcius to fahrenheit conversion and fahrenheit to celcius conversion using function and return the value from the function and print it in the main program.


def conversion(temp,unit):       #iske liye humne 2 argument liye hai temp and unit. temp is the temperature value and unit is the unit of temperature which can be either 'C' for celcius or 'F' for fahrenheit.
    if unit == "c":
        temp= int(input("enter the tempreature in celcius = "))
        print(f"{temp}degree celcius is equal to the {(temp*9/5)+32} degree fahrenheit")
        return (temp*9/5)+32
    elif unit == "f":
        temp = int(input("enter the tempreature in fahrenheit = "))
        print(f"{temp}degree fahrenheit is equal to the {(temp-32)*5/9} degree celcius")
        return (temp-32)*5/9

temp = int(input("enter the tempreature = "))
unit = input("enter the unit (c/f) = ")
conversion(temp,unit)
#overview of the program is that it takes the temperature value and unit as input from the user and then converts the temperature to the other unit and returns the value. and then it prints the converted value in the main program. also it uses the f-string to print the converted value in a formatted way.
