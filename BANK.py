import random
import mysql.connector as c 

def menu():
    print('''
    
    1) Account Details
    
    2) Transaction
    
    3) Transaction Details
    
    4) Balance
    
    5) Delete Account
    
    6) Feedback
    
    7) Logout
    
    8) Back
    
    ''')
    N=int(input("Enter your Choice: "))
    if N==1:
        cur.execute("select * from login_details where LoginID='{}'".format(u))
        g=cur.fetchall()
        for ig in g:
            cur.execute("select * from customer_details where Account_no='{}'".format(ig[0]))
            k=cur.fetchall()
            for ik in k:
                print('''Your Account Details are:- 
                ''')
                print("Account Holder Name: ",ik[0])
                print("Gender: ",ik[1])
                print("DOB: ",ik[2])
                print("Account Number: ",ik[3])
                print("Mobile Number: ",ik[4])
                print("Account open date: ",ik[5])
                print("Address: ",ik[6])
                print("LoginID: ",ig[1])
                print("Password: ",ig[2])
                menu()
    elif N==2:
        print('''
        1) Deposit
        2) Withdraw
        3) Back
        ''')
        n3=int(input("Enter your choice: "))
        if n3==1:
            a=int(input("Enter deposit amount: Rs."))
            cur.execute("select * from login_details where LoginID='{}'".format(u))
            g1=cur.fetchall()
            for ig1 in g1:
                cur.execute("select max(Dateot) from transaction_details where Account_no='{}'".format(ig1[0]))
                x=cur.fetchall()
                for ix in x:
                    cur.execute("Select * from transaction_details where account_no='{}' and Dateot='{}'".format(ig1[0],ix[0]))
                    c=cur.fetchall()
                    for ic in c:
                        cur.execute("insert into transaction_details values('{}',{},'Deposit',Now(),{})".format(ig1[0],a,ic[4]+a))
                        con.commit()
                        print('Account Updated Succesfully!')
                        menu()
        elif n3==2:
            w=int(input("Enter withdraw amount: Rs."))
            cur.execute("select * from login_details where LoginID='{}'".format(u))
            g2=cur.fetchall()
            for ig2 in g2:
                cur.execute("select max(Dateot) from transaction_details where Account_no='{}'".format(ig2[0]))
                x1=cur.fetchall()
                for ix1 in x1:
                    cur.execute("Select * from transaction_details where account_no='{}' and Dateot='{}'".format(ig2[0],ix1[0]))
                    c1=cur.fetchall()
                    for c1i in c1:
                        if c1i[4]<w:
                            print("Insufficient Balance")
                        elif w<c1i[4]:
                            cur.execute("insert into transaction_details values('{}',{},'Withdraw',Now(),{})".format(ig2[0],w,c1i[4]-w))
                            con.commit()
                            print('Account Updated Succesfully!')
                            menu()
        elif n3==3:
            menu()
        else:
            print("Incorrect input, Try again")
            menu()           
    elif N==3:
        cur.execute("select * from login_details where LoginID='{}'".format(u))
        j=cur.fetchall()
        for ji in j:
            cur.execute("Select Amount,Ttype,Balance,Dateot from transaction_details where Account_no = '{}'".format(ji[0]))
            s=cur.fetchall()
            for si in s:
                print(si)
            menu()
    elif N==4:
        cur.execute("select Account_no from login_details where LoginID='{}'".format(u))
        u5=cur.fetchall()
        for u5i in u5:
            cur.execute("select max(Dateot) from transaction_details where Account_no='{}'".format(u5i[0]))
            u6=cur.fetchall()
            for u6i in u6:
                cur.execute("Select balance from transaction_details where Account_no='{}' and Dateot='{}'".format(u5i[0],u6i[0]))
                u7=cur.fetchall()
                for u7i in u7:
                    print("Your Current Balance is: Rs.",u7i[0])
                menu()
    elif N==5:
        cur.execute("select Account_no from login_details where LoginID='{}'".format(u))
        u9=cur.fetchall()
        for u9i in u9:
            cur.execute("Delete from transaction_details where Account_no='{}'".format(u9i[0]))
            con.commit()
            cur.execute("Delete from login_details where Account_no='{}'".format(u9i[0]))
            con.commit
            cur.execute("Delete from customer_details where Account_no='{}'".format(u9i[0]))
            con.commit()
            cur.execute("Select * from customer_details where Account_no='{}'".format(u9i[0]))
            if cur.fetchone() is None:
                print("Account Deleted")
                Login()
            else:
                print("Try Again, Something went wrong")
    elif N==6:
        f=input("Give Your feedback hear: ")
        cur.execute("insert into feedback_details values('{}','{}')".format(f,u))
        con.commit()
        cur.execute("select * from feedback_details where LoginID='{}'".format(u))
        if cur.fetchall() is None:
            print("Please Try Again Something went wrong")
            menu()
        else:
            print("Feedback Submitted")
            menu()
    elif N==7:
        print("----------------------------------------------------Thankyou Visit Again-----------------------------------------------------")
    elif N==8:
        Login()
    else:
        print("Incorrect input, Try again")
        menu()
            
def login():
    global u
    u=input("LoginID: ")
    fp=input("Forgot Password?(Yes/No): ")
    if fp=='Yes':
        d=input("Please Confirm Your Birthdate(yyyy-mm-dd): ")
        cur.execute("Select * from login_details where LoginID='{}'".format(u))
        fp1=cur.fetchall()
        for fp1i in fp1:
            cur.execute("Select * from customer_details where Account_No='{}'".format(fp1i[0]))
            fp2=cur.fetchall()
            for fp2i in fp2:
                if str(d)==str(fp2i[2]):
                    cur.execute("select * from login_details where LoginID='{}'".format(u))
                    fp3=cur.fetchall()
                    for fp3i in fp3:
                        print("Your Password is: ",fp3i[2])
                        login()
                else:
                    print("Incorrect Birthdate")
                    login()
    elif fp=='No':
        p=input("Password: ")
        cur.execute("select * from login_details where LoginID='{}' and Password='{}'".format(u,p))
        if cur.fetchone() is None:
            print("Invalid username or password,Try Again")
            login()
        else:
            menu()
    else:
        print("Invalid Input, try again")
        login()
        
def account():
    print("To create account enter details below: -")
    n1=input("Name: ")
    G1=input("Gender(Male,Female): ")
    B1=input("date of Birth(yyyy-mm-dd): ")
    r1=random.randint(10000000000000,99999999999999)
    P1=input("10 digit Phone Number: ")
    a1=input("Address: ")
    o=int(input("Enter the opening ammount: "))
    u1=input("Enter loginId(for example 'xyz@125'): ")
    p1=input("Enter password maximum of 10 character: ")
    cur.execute("insert into customer_details values('{}','{}','{}','{}','{}',curdate(),'{}')".format(n1,G1,B1,r1,P1,a1))
    con.commit()
    cur.execute("insert into login_details values('{}','{}','{}')".format(r1,u1,p1))
    con.commit()
    cur.execute("insert into transaction_details values('{}',{},'Deposit',Now(),{})".format(r1,o,o))
    con.commit()
    cur.execute("select * from login_details where LoginID='{}' and Password='{}'".format(u1,p1))
    if cur.fetchall() is None:
        print("Please Try Again Something went wrong")
        account()
    else:
        print("Account created succesfully")
        cur.execute("select Account_no from login_details where LoginID='{}' and Password='{}'".format(u1,p1))
        v=cur.fetchall()
        for iv in v:
            print("Your Account Number is:- ",iv[0])
            login()
    
def Login():
    print(''' 
    1) Login
    
    2) Create Account
    
    3) Contact us
    
    4) Exit
        ''')
    n=int(input("Enter your choice: "))
    if n==1:
        login()
    elif n==2 :
        account()
    elif n==3:
        print('''
        Call:- 7415678322
        ''')
        Login()
    elif n==4:
        print("----------------------------------------------------Thankyou visit Again-------------------------------------------------------")
    else:
        print("Incorrect Input,Try Again")
        Login()
        
con=c.connect(host="localhost",user="root",passwd="rudraxcode",database="bank")
if con.is_connected():
    cur=con.cursor()
    print("------------------------------------------------------------BANK------------------------------------------------------------")
    Login()
con.close()
