user_input = int(input("Enter the number between or equal to 1500 and 2700"))

if user_input >= 1500 and  user_input <= 2700:
    if user_input % 7 == 0 and user_input % 5 == 0:
        print(f"{user_input} is disvisble by 7 and multiple of 5")
    else:
        print(f"{user_input} is disvisble by 7 and multiple of 5") 
else:
    print("Enter the number between or equal to 1500 and 2700")