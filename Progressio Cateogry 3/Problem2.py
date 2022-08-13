T=int(input("Enter the number of test cases(between 1 to 1000): "))

if (not 1<=T<=1000):
    print("ERROR: Make sure the number of test cases is between 1 and 1000")
    T=int(input("Renter the number of test cases(between 1 to 1000): ")) 
else:
    i=1
    while(i<=T):
        X= int(input("Enter Alice's height (between 100 to 200 cm): "))
        if not 100<=X<=200:
            print("ERROR: The height must be between 100 to 200 cms")
            X= int(input("Renter Alice's height (between 100 to 200 cm): "))

        Y= int(input("Enter Bob's height (between 100 to 200 cm): "))
        if not 100<=Y<=200:
            print("ERROR: The height must be between 100 to 200 cms")
            Y= int(input("Renter Bob's height (between 100 to 200 cm): "))

        if X==Y:
            print("ERROR: The height's cannot be the same") 
            X= int(input("Renter Alice's height (between 100 to 200 cm): "))
            Y= int(input("Renter Bob's height (between 100 to 200 cm): "))

        if (X>Y):
            print("Alice is taller")
        elif(Y>X):
            print("Bob is taller")
        i+=1
    

    