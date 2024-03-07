while True:

    TEMP_choice = int(input("Enter a  SCALE \n0 for exit\n1 for Celsius\n2 for Fahreinheit\n3 for Kelvin :\n"))
    if TEMP_choice==0:
        break
    temp = float(input("Enter the temperature you want to input: "))
    if TEMP_choice==1:
        print(f"Fahrenheit value : {temp*(9/5)+32}F\nKelvin value : {temp + 273.15}K")
    elif TEMP_choice==2:
        print(f"Celsius value : {(temp-32)*(5/9)}C\nKelvin value : {(temp-32)*(5/9) + 273.15}K")
    elif TEMP_choice==3:
        print(f"Celsius value : {temp-273.15}C\nFahreinheit value : {(temp-273.15)*(9/5)+32}F")
    
    else:
        print("Wrong input")
