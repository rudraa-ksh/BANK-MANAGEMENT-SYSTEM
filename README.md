# BANK-MANAGEMENT-SYSTEM 

### A Simple Terminal Based Bank Management System which performs Standard Operations of a Bank.

## Tools and Technology Used:
- [Python](https://docs.python.org/3/)
- [MySQL](https://dev.mysql.com/doc/)
- [Visual Studio Code](https://code.visualstudio.com/docs)

## Operations You Can Perform:
- Create Account
- Login
- Check your Account details like:
    - Account Holder Name
    - Gender
    - DOB
    - Account Number
    - Mobile Number
    - Account Open Date
    - Address
    - LoginID
    - Password
- Perform Virtual Transactions
- Check Your Transaction Details
- Check Your Account Balance
- Delete Your Account
- Give Feedback
- Logout

## Getting Started:
1. Download and install [Python](https://www.python.org/downloads/windows/) and [MySQL](https://dev.mysql.com/downloads/installer/) in your system.
2. Connect MySQL Database with Python Interpreter by installing two libraray:
   
   ```
   pip install mysql-connector-python
   pip install pymysql
   ```
   
3. In MySql create a Database named "bank".
4. Run the following SQL Commands to create tables in "bank" database:
    ```
    create table customer_details(Account_holder varchar(30) not null, Gender varchar(6) not null check(Gender in("Male","Female")),DOB date not null, Account_no varchar(15) primary key, Mno varchar(10) not null unique, Aopend date not null, Addr varchar(50) not null);

    create table login_details(Account_no varchar(14), LoginID varchar(10) not  null unique, Password varchar(10) not null unique, foreign key(Account_no) references customer_details(Account_no));

    create table feedback_details(Feedback varchar(100) not null, LoginID varchar(10) not null);

    create table transaction_details(Account_no varchar(14), Amount bigint not null, Ttype varchar(8),Dateot datetime, Balance bigint, foreign key(Account_no) references customer_details(Account_no));

    ```
5. Change the database password and you are ready to run the program.
