
while True:
    print(" ====== [ MENU ] =======")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiply")
    print("4. Division")
    print("5. Exit")
    Select = int(input("Select : "))
    
    if Select == 1:
         a = int(input("Enter First Number : "))
         b = int(input("Enter Second Number : "))
         print (a , " + ", b ," = " , (a+b))
    elif Select == 2:
         a = int(input("Enter First Number : "))
         b = int(input("Enter Second Number : "))
         print (a , " - ", b ," = " , (a-b))
    elif Select == 3:
        a = int(input("Enter First Number : "))
        b = int(input("Enter Second Number : "))     
        print (a , " * ", b ," = " , (a*b))
    elif Select == 4:
        a = int(input("Enter Nominator Number : "))
        b = int(input("Enter Denominator Number : "))
        result = float( a / b)
        print (a , " + ", b ," = " , result)
    elif Select == 5:
        break
    elif Select >= 6:
        print("ERROR INPUT")
    