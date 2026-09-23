# salary = float(input("Enter you salary :  "))
# if salary < 30000:
#     tax = salary*5/100
# elif salary >= 30000 or salary <= 70000:
#     tax = salary*15/100
# elif salary > 70000:
#     tax = salary*25/100

# print("YOur total tax is : ",tax)



#Q2
# a = int(input("Enter first integer : "))
# b = int(input("Enter second integer : "))

# for i in range(a+1,b):
#     if i%2 == 0:
#         print(i)

# Q3
# n = int(input("Enter the digit : "))
# def Couter(n):
#     count = 0
#     for i in range(n):
#         if i/10 < 1:
#             break
#     count+=1
#     return count
# print(Couter(n))

#Q6
# for i in range(1,100):
#     if i % 3 == 0 or i % 5 == 0:
#         print(i)
    

#Q7
while(True):
    x = input("Enter the input : ")
    if(x == "Quite"):
        break
    elif x == float(x):
        print = x
    else:
        print("Wrong Input")