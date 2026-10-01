numbers = (1,2,3,4,5,6,7,8,9)
even = 0
odd = 0
for number in numbers:
    if number % 2 == 0:
        even += 1
    else:
        odd +=1
print("Number of odd = ",odd)        
print("Number of even = ",even)        
        