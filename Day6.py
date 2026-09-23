# x = input("enter the input : ")
# f = open("sample.txt","r+")
# f.write(x)
# data = f.read()
# print(data)
# f.close()
# import os 
# os.remove("sample.txt")

# prcise question
# data = True
# line = 1
# with open("sample.txt","r") as f:
#     while data:
#         data = f.readline()
#         if("Python" in data):
#             print(f"word found at line {line}")
#             break
#         line +=1
        

# try:
#     x = int(input("ente the x : "))
#     ans = 10/x
# except ZeroDivisionError:
#     print("Division with 0 is not possible")
# except ValueError:
#     print("in valid input ")
# except NameError:
#     print("in valid input  NameRrror occur")
# else:
#     print(f"answer is {ans}")
# print("this is out of try")

# Q1
# with open("name.txt","w+") as f:
#     for x in range(5):
#         x = input("Enter the name: ")
#         f.write(x+"\n")
# with open("name.txt","r") as f:
#     print(f.read())



# Q3
# list1 = [5,10,15,20,25]
# list2 = [i for i in list1 if i > 15   ]
# print(list2)

# Q4
# import json
# cities = {
#     "lahore":12_000,
#     "okara":15_000,
#     "multan":16_000,
#     "dep":None
# }
# with open("cities.json","w") as f:
#     c = input("Enter the city : ")
#     p = input("Enter the population : ")
#     cities.update({c:p})
#     json.dump(cities,f)

# with open("cities.json","r") as f:
#     print(json.load(f))

# Q5
# try:
#     with open("v.json","r") as f:
#         print(json.load(f))
# except FileNotFoundError:
#     print("file not found")
# else:
#     print("file not found")       

