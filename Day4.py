# word = "I study from  apnacollege"
# print(word[:-4])

a = 5
b = 10
# sum = a + b 
# print("Sum is {}".format(sum)) #fromating
# print("Sum of {} & {} is {}".format(a,b,sum)) #fromating
# print(f"Sum is {sum}") # f-string 

# # indexing formation
# print("Sum of {0} & {1} is {2}".format(b,a,sum)) #fromating

# #valu based formating
# print("Sum of {a} & {b} is {sum}".format(a=5,b=10,sum=15)) #fromating

# info = [
#     ("Alice", "Math"),
#     ("Bob", "Science"),
#     ("Alice", "Science"),
#     ("Charlie", "Science"),
#     ("Alice", "English"),
#     ("Charlie", "English"),
# ]

# # unique_courses = set()
# # unique_stu = set()
# # english_stu = set()
# dict = {}
# for  name,course  in info:
#     if(dict.get(name) == None):
#         dict.update({name: set()})
#         dict[name].add(course)
#     else:
#         dict[name].add(course)

# #     if i[1 ] == "English":
# #         english_stu.add(i[0])
# #     unique_courses.add(i[1])
# #     unique_courses.add(i[0])
# # print(unique_courses)
# # print(english_stu)
# # print(dict)



# # Q1
# strings = input("Enther the string  :  ")
# new_string1 = []
# new_string2 = []
# for i in strings:
#     new_string1.insert(0,i)
#     new_string2.append(i)
# if new_string1 == new_string2:
#     print("Yes its is palindrome")
# else:
#     print("No! its is not palindrome")



# Q2
# list1 = []
# sum = 0
# i = 0
# while(True):
#     x  = input("Enter the input q  to exit : ")
#     if x == 'q':
#         break
#     list1.append(x)
#     sum += int(list1[i])
#     i += 1
# avg = sum/len(list1)
# print(avg)



# Q3


# list1 = list(map(int, input("Enter first list: ").split()))
# list2 = list(map(int, input("Enter second list: ").split()))

# result = list1 + list2

# result.sort()

# print("Merged and Sorted List:")
# print(result)



# Q4
# tup1 = tuple(map(int, input("Enter first list: ").split()))
# even = ()
# odd = ()

# for i in tup1:
#     if i%2 == 0:
#         even = even + (i,)
#     else:
#         odd = odd + (i,)

# print(odd)
# print(even)


# Q5
# student = {}
# while True:

#     print("\nA. Add Student")
#     print("B. Update Marks")
#     print("C. Search Student")
#     print("D. Display All")
#     print("E. Exit")
#     option = input("Enter the option").upper()
#     info = {}
#     if option == 'A':
#         name = input("Enter the name :  ")
#         marks = input("Enter the marks :  ")
#         student[name] = marks
#     elif option == 'B':
#         name = input("Enter the name :  ")
#         if name in student:
#             marks = input("Enter the marks :  ")
#             student[name] = marks
#         else:
#             print("student not found")
#     elif option == 'C':
#         name = input("Enter the name :  ")
#         if name in student:
#             print(name," = ",student[name])
#         else:
#             print("student not found")
#     elif option == 'D':
#         for key, value in student.items():
#             print(key, ":", value)
#     elif option == 'E':
#         print("You are exit")
#     else:
#         print("you entered  wrong option")    



# Q6
words = ["apple", "banana", "kiwi", "cherry", "mango"]
dict1 = {}
for word in words:
    dict1.update({
        word : len(word)
    })
print(dict1)


# Q7
list1 = [1, 2, 3, 4] 
list2 = [5, 6, 7, 8]
sets = set()
for  i in 