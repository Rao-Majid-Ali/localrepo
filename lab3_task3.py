input_number = int(input("Enter the gusses"))
while True:    
    if input_number > 0 and input_number < 9:
        if input_number == 8:
            print("well guess")
            break
        else:
            print("Wrong guess!,Try Again")
            input_number = int(input("Enter the gusses"))
    else:
        input_number = int(input("Enter the gusses"))
            
            
    