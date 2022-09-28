print("Welcome To Vertual ATM")
print("Press 1 to Cash Withdrawal: " )
print("Press 2 for Cash Deposite")
print("Press 3 to Balance Chaeck: ")
print("Press 4 to other inquiry: ")

a=int(input("Enter a no: "))
if a==1:
    c=int(input("Enter a PIN: "))
    while c==123:
        b = str(input("Enter amount  :  "))
        b = "\n-"+ b 
        f = open("balance.txt","a")
        file = f.write(b)
        print(file)
        print("Collect Your Cash")
        break
    
    else:
        print("You Entered a wrong PIN")
        
if a==2 :
    myfile='balance.txt'
    sum=0
    with open (myfile) as fh:
        for n in fh:
            n=n.strip()
            balance=n.split(',')
            for ns in balance:
                sum = sum +  int(ns)
    print("Your balance is",sum)
    
    
    cr = (input("Enter amount for Credit :   "))
    cr = "\n" + cr
    f = open("balance.txt","a")
    file = f.write(cr)
    print(file)
    
    print("Your Cash is Deposit ")
    print("Now try once again and check your balance")    
 
if a==3:
    myfile='balance.txt'
    sum=0
    with open (myfile) as fh:
        for n in fh:
            n=n.strip()
            balance=n.split(',')
            for ns in balance:
                sum = sum + int(ns)
    print("Your balance is",sum)
    
if a==4:
    print("For other inquiry please visite your home branch")
    
if  a>=5 or a<=0  :
    print("Please enter a valid Input")

# try:
#     a>=5 or a<=0  
#     print("Please enter a valid Input",a==int())
#     # print(a)
# except Exception as m:
#     print(m)
#     print("Enter a valid Input")
    
    
