print("\n well come to national bank")
print("please insert your atm Card")
password=1234
balance=12000
choice=0
pin=int(input("please insert your pin number"))
if(pin==password):
    while(choice!=4):
     print(".....menu.....")
     print("1==balance")
     print("2==deposite")
     print("3==withdraw")
     print("4==cancel")
     choice=int(input("\nEnter your option"))
     if(choice==1):
        print("your balance is =Rs:",balance)
     elif(choice==2):
        deposite=int(input("enter your deposite amount"))
        balance+=deposite
        print("\ntotal balance in your account is RS:",balance)
     elif(choice==3):
        withdraw=int(input("\nEnter the amount to withdraw RS:"))
        balance-=withdraw 
        print("total amount in your balance is RS:",balance)
     elif(choice==4):
        print("session ended!!!")
else:
    print("please try again your pin") 