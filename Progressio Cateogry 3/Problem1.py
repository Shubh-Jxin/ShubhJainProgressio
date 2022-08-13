T=int(input("Enter the number of test cases(between 1 to 1000): "))

def amount_function():
    X=int(input("Enter the amount to  be paid(between 1 to 1000): "))
    if(1<=X<=1000):
        print("Minimum number of coins needed=",X%10)    
    else:
        print("ERROR: Make sure the amount to be paid is between 1 and 1000")
        X=int(input("Renter the amount to  be paid(between 1 to 1000): "))
        print("Minimum number of coins needed=",X%10) 


def test_function():
    i=1
    while (i<=T):
        amount_function()
        i+=1

     
if (not 1<=T<=1000):
    print("ERROR: Make sure the number of test cases is between 1 and 1000")
    T=int(input("Renter the number of test cases(between 1 to 1000): ")) 
    test_function()
else:
    test_function()
   
  
    
    

