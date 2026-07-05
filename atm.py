import pyodbc
conn=pyodbc.connect(
    'Driver={SQL Server};''Server=DESKTOP-C4FH399;'
    'Database=ATMDB;''Trusted_Connection=yes;')
print("Connected Successfully")
cursor=conn.cursor()
# ------------------------
# -------GETTING THE INPUT DATAS----------

acc_no=int (input("Enter the Account Number    :"))
pin=int(input("Enter the pin value    :"))

query=""" select * from ATMAccount where acc_no=? and pin =?"""
cursor.execute(query,acc_no,pin)
user=cursor.fetchone()
if user:
    print("Login Successfully ")
else:
    print("Invalid Account and Pin Number")
print("List of the opearion given below :")
print("1.Check the Balance Amount")
print("2.Deposit the Amount")
print("3.Withdraw the Amount")
print("4.Exit")

choice=int(input("Enter your option :"))
if choice ==1:
    cursor.execute("select balance from ATMAccount where acc_no=?",acc_no)
    balan=cursor.fetchone()
    print("Current Balance =",balan[0])
elif choice==2:
    amount=float(input("Enter Deposite Amount :"))
    cursor.execute("""update ATMAccount set balance=balance + ? where acc_no=?""",amount,acc_no)
    print("Amount Deposit Successfully")
elif choice==3:
    withdraw_amount=float(input("Enter the withdraw Amount  :"))
    cursor.execute("select balance from ATMAccount where acc_no=?",acc_no)
    current_balance=cursor.fetchone()[0]
    if withdraw_amount<=current_balance:
        cursor.execute("""update ATMAccount set balance=balance - ? where acc_no=?""",withdraw_amount,acc_no)
        conn.commit()
        print("Amount Withdraw Successfully")
    else:
        print("Insufficent Balance in Your Account")
elif choice==4:
    print("Thank you for using ATM")
conn.close()


----------SQL Database Code----------------
-----ATM OPERATION-----------
--------DB Creation----------
create database ATMDB
--------Table Creation-------
create table ATMAccount(acc_no int primary key,customer_name varchar(100),pin int,balance decimal(10,2))
insert into ATMAccount values(102021,'Ravi',1111,15000.00),(102022,'Geetha',2222,18000.00),
(102023,'Priya',3333,12000.00),(102024,'Pavithra',4444,17000.00),(102025,'Archana',5555,13500.00),
(102026,'Giri',6666,21000.00),(102027,'Rajinikanth',7777,28000.00),(102028,'Anbarasan',8888,23000.00),
(102029,'Kavin',9999,24500.00),(102030,'Hari',1010,22500.00)
----------Read/View the Table----
select * from ATMAccount
