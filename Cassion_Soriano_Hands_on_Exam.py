number = eval(input("What type of conversion: \n"
                    "[1] binary\n"
                    "[2] Octal\n"
                    "[3] Hexadecimal\n"))
if number == 1:
    dec1 = int(input("Enter a decimal value to convert:\n"))
    binary = format(dec1, "b")
    print(f"Binary value of {dec1} is {binary}")

elif number == 2:
    dec2 = int(input("Enter a value decimal value to convert:\n"))
    oct = format(dec2, "o")
    print(f"The binary value of {dec2} is {oct},")

elif number == 3:
    dec3 = int(input("Enter a decimal value to convert:\n"))
    hex = format(dec3, "x")
    print(f"Print binary value of {dec3} is {hex}, ")

else:
    print("Input error. Please try again")





