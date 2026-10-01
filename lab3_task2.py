temp_input = input("Enter F for Fahrenheit to Celcius and C for Celcius to Fahrenheit : ")
temp1_input = int(input("Enter the temperature "))

if temp_input.upper() == 'F':
    celcius = int(((temp1_input-32)/9)*5)
    print(f"{temp1_input} F is {celcius} in celcius")
elif temp_input.upper() == 'C':
    Fahrenheit = int((9/5*temp1_input)+32)
    print(f"{temp1_input} C is {Fahrenheit} in Fahrenheit")
else:
    print("you enter a wrong input")
