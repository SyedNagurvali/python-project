name="Nagur"
password="123"
user_name=input("Enter the User Name:")
passwords=input("Enter the Password:")
s='''
     1.Credit
     2.Debit
     3.mini statement
     4.exit
 '''
Amount=1000
if name==user_name and passwords==password:
     while True:
         print(s)
         option=int(input("Enter the Option:"))
         if option==1:
             credit_amount=float(input("Enter the Amount:"))
             print("Amount after credit:",Amount+credit_amount)
         elif option==2:
             debit_amount=float(input("Enter the Amount:"))
             print("Amount after debit:",Amount-debit_amount)
         elif option==3:
             print("###Mini Statement Amount###:",Amount)
         elif option==4:
             break
else:
     print("incorrect")