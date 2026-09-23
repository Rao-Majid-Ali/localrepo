# user_name = input("Enter your name :  ")
# user_age = input("Enter your age :  ")
# print("Hellomajid "+user_name ,"you are "+ user_age , "years old!")

# a = float(int(input("enter the first number : ")))
# b = float(int(input("enter the second number : ")))
# c = int(input("enter the 3 number : "))
# d = (a+b+c)/3
# print(d)

# x = 10+3*2**2
# print(x)

# a = int(input("enter the first number : "))
# b = int(input("enter the second number : "))
# temp = a
# a = b
# b = temp
# print(a)
# print(b)

# c_temp = input("enter the temperatur in celsius : ")
# f_temp = (float(c_temp)*(9/5))+32
# print(f_temp)

a = float(input("Enter the number : "))
integer_part = int(a)
fractional_part = a - integer_part
print("integer part - ",integer_part)
print("float part - {:.2f}".format(fractional_part))