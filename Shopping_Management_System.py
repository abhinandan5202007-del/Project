
import mysql.connector as m

from prettytable import PrettyTable

# To connect mysql with python and creating a table

def connect():
    con=m.connect(host='localhost',
                  username= 'root',
                  password='1234',
                  database='shop')
    if con.is_connected():
        cur=con.cursor()
        st='Create table  if not exists cust_details ( name varchar(30),gmail varchar(30),contact char(10) PRIMARY KEY,password varchar(30));'
        cur.execute(st)
    con.commit()
    
    con.close()

connect()

# To make a login window

def loginaccount():
    con1=m.connect(host='localhost',
                  username= 'root',
                  password='1234',
                  database='shop')
    if con1.is_connected():
        cur1=con1.cursor()
        
        gmail=input("Enter the email: ")
        password= input("Enter the password:")
        login="Select count(*) from cust_details where gmail='{}' and password='{}'".format(gmail,password)
        print()
        cur1.execute(login)

        x=cur1.fetchall()
        
        return x
    
    con1.close()

# To create an account
    
def createlogin():
    
    con2=m.connect(host='localhost',
                    username= 'root',
                    password='1234',
                    database='shop')
    if con2.is_connected():
        cur2=con2.cursor()

        name=input("Enter name:")
        contact=input("Enter contact:")
        gmail=input("Enter the email: ")
        password= input("Enter the password:")
        login="Insert into cust_details values('{}','{}','{}','{}')".format(name,gmail,contact,password)
            
        cur2.execute(login)
    con2.commit()
    con2.close()


# End of logging in

# Creation of inventory table

def inventory():
    con3=m.connect(host='localhost',
                      username= 'root',
                      password='1234',
                      database='shop')
    if con3.is_connected():
        cur3=con3.cursor()
        st='Create table  if not exists inventory (product varchar(30) PRIMARY KEY,price int NOT NULL,category varchar(30) NOT NULL,stock int NOT NULL)'
        cur3.execute(st)
    con3.commit()
    
    con3.close()
inventory()

# Insertion of items in inventory

def insert_inventory():
    con7=m.connect(host='localhost',
                        username= 'root',
                        password='1234',
                        database='shop')
    if con7.is_connected():
        cur7=con7.cursor()
        product=input("Enter the product name :")
        price=int(input("Enter the price :"))
        category=input("Enter the category of product (clothing,daily,electronics)")
        stock=int(input("Enter the stock:"))   
        st="Insert into inventory values('{}',{},'{}',{})".format(product,price,category,stock)
        cur7.execute(st)
    con7.commit()
        
    con7.close()

# Updatation of items in inventory
   
def update_inventory():
    con8=m.connect(host='localhost',
                        username= 'root',
                        password='1234',
                        database='shop')
    if con8.is_connected():
        cur8=con8.cursor()
        pro=input("Enter product name : ")
        stock=int(input("Enter the stock: "))
        price=int(input("Enter the price: "))
        st="Update inventory set stock = {} where product = '{}'".format(stock,pro)
        st1="Update inventory set price = {} where product = '{}'".format(price,pro)
        cur8.execute(st)
        cur8.execute(st1)
    con8.commit()
        
    con8.close()

# Deletion of items in inventory

def delete_inventory():
    con9=m.connect(host='localhost',
                        username= 'root',
                        password='1234',
                        database='shop')
    if con9.is_connected():
        cur9=con9.cursor()
        prod=input("Enter the product name :")  
        st="Delete from inventory where product = '{}'".format(prod)
        cur9.execute(st)
    con9.commit()
        
    con9.close()

# Updatation of stock in inventory

def stock_inventory(p,number):
    con10=m.connect(host='localhost',
                        username= 'root',
                        password='1234',
                        database='shop')
    if con10.is_connected():
        cur10=con10.cursor()
         
        st="Update inventory set stock = stock - {} where product='{}'".format(number,p) 
        cur10.execute(st)
    con10.commit()
        
    con10.close()

# Display of items in inventory

def display_inventory():
    con13=m.connect(host='localhost',
                        username= 'root',
                        password='1234',
                        database='shop')
    if con13.is_connected():
        cur13=con13.cursor()
         
        st="Select * from inventory "
        cur13.execute(st)
        table = PrettyTable()

        column_names = [i[0] for i in cur13.description]
        table.field_names = column_names


        for i in cur13.fetchall():
            table.add_row(i)

        print(table)
        
    con13.close()

# Searching items based on category in inventory

def search_inventory(cat):
    con11=m.connect(host='localhost',
                        username= 'root',
                        password='1234',
                        database='shop')
    if con11.is_connected():
        cur11=con11.cursor()
         
        st="Select * from inventory where category = '{}'".format(cat)
        cur11.execute(st)
        table = PrettyTable()

        column_names = [i[0] for i in cur11.description]
        table.field_names = column_names


        for i in cur11.fetchall():
            table.add_row(i)

        print(table)
        print()
    con11.close()
    
# Start of admin 

# Creation of admin table
    
def admin():
    con4=m.connect(host='localhost',
                      username= 'root',
                      password='1234',
                      database='shop')
    if con4.is_connected():
        cur4=con4.cursor()
        st='Create table  if not exists admin_details (name varchar(30),user varchar(30) PRIMARY KEY,password varchar(30))'
        cur4.execute(st)
    con4.commit()
    
    con4.close()
admin()

# To make a login window

def adminaccount():
    con5=m.connect(host='localhost',
                  username= 'root',
                  password='1234',
                  database='shop')
    if con5.is_connected():
        cur5=con5.cursor()
        
        user=input("Enter the email: ")
        password= input("Enter the password:")
        login="Select count(*) from admin_details where user='{}' and password='{}'".format(user,password)
        
        cur5.execute(login)

        x=cur5.fetchall()
        
        return x
    
    con5.close()


# Billing of items brought
    
def billing(pro,l,n):
    con12=m.connect(host='localhost',
                    username= 'root',
                    password='1234',
                    database='shop')
    if con12.is_connected():
        j=[]
        cur12=con12.cursor()
        st="select * from inventory where product='{}'".format(pro)
        cur12.execute(st)
        x=cur12.fetchone()
        global bill
        
        
        bill=bill+n*(int(x[1]))

        k=list(x)
        k.append(n)
        j=[k]
        
        
        l.extend(j)
        
        
    con12.commit()
    con12.close()        

# Finally displaying the billing amount
def check(buy_product):
    con=m.connect(host='localhost',
                    username= 'root',
                    password='1234',
                    database='shop')
    if con.is_connected():
        cur=con.cursor()
        st="Select count(*) from inventory where product='{}'".format(buy_product)
        cur.execute(st)
        
        x=cur.fetchall()
        
        return x
    
    con.close()

def check_stock(buy_product):
    
    con=m.connect(host='localhost',
                    username= 'root',
                    password='1234',
                    database='shop')
    if con.is_connected():
        cur=con.cursor()
        st="Select stock from inventory where product='{}'".format(buy_product)
        cur.execute(st)
        x=cur.fetchone()

        return x
           

def final(li):
    while True:
        
        print("\nFollowing categories are available :")
        print("Fashion")
        print("Daily")
        print("Electronics\n")
        
        category = input("Enter the category you want to search: ")        
        
        if category.title() not in ["Fashion","Daily","Electronics"]:
            print("\nSelect a valid category !\n")
            
        else:
            print("Following products are available:")
            search_inventory(category.title())
            buy_product=input("Enter the product you want to buy : ")
            t=check_stock(buy_product)

            if t[0] <= 0:
                
                print("Sorry , the product is out of stock !")
                print("Enter another product !")
                continue
            
            else:

                qty=int(input("Enter the number of product you want to buy (till the stock lasts)  : "))
                for i in check(buy_product):
                
                    if i[0] == 0:
                        
                        print("No such products available.")
                        print("Enter again !")
                        break
                    
                    else:   
                        
                        billing(buy_product,li,qty)
                        stock_inventory(buy_product,qty)
                        
                if input("Continue to buy ? (y/n) : ").lower()=='n':
                    break
    print("Your bill is :")

    table = PrettyTable()

    
    table.field_names = ['Item','Amount','Quantity']

    for i in li:
        table.add_row([i[0],i[1],i[4]])

    print(table)
    print()

    print("Total amount to be paid: ",bill)

    print("\nThank you for visiting Shopping World !!")
    print("See you soon!  :)")

# Options to choose for admin to work on inventory

def admin_options():
    while True:
        #print()
        print("\nMENU :")
        print("1.Display inventory")
        print("2.Insert into inventory")
        print("3.Delete from inventory")
        print("4.Update inventory")
        print("5.Exit\n")
        #print()
        ch=int(input("Enter what you want to do ? (only numbers):"))
        if ch == 1:            
            display_inventory()
            
        elif ch == 2:
            insert_inventory()
            
        elif ch == 3:
            delete_inventory()
           
        elif ch == 4:
            update_inventory()
            
        elif ch == 5:
            print("Hope to see you again soon!  :)")
            break
        else:
            print("\nEnter a valid number")
        print()

# Calling of functions


print("\nWelcome to the Shopping World !!\n")
print("*"*117)
print("\nAre you a customer ?")

ch=input("Yes/No : ")

if ch.lower()=='yes':
    li=[]
    bill=0
    print("Do you have an account?")
    if input("Yes/No : ").lower() == 'yes' :
        
        for i in loginaccount():
            
            if i[0] == 0:
            
                print("Account not created ")
                if input("Create an account ? (y/n) : ").lower() == 'y':
                    createlogin()
                    final(li)
                    
                else:
                    print("\nThank you for visiting\n")
                    
            else:
                print("Account exists")
                final(li)


    else:
        if input("Create account ? (y/n) : ").lower() == 'y':
            createlogin()
            final(li)
            
        else:
            print("\nThank you for visiting\n")
        
elif ch.lower() == 'no' :
    
    print("Do you have an admin account?")
    
    if input("Yes/No : ").lower() == 'yes' :
        
        for i in adminaccount():
    
            if i[0] == 0:
                print("Account doesn't exists ")
                print("\nThank you for visiting\n")
            else:
               print("Account exists")
               admin_options()
                  
    else:
        print("\nThank you for visiting\n")

else:
    print("\nThank you for visiting\n")

print("*"*117)
print("\nA project by ABHINANDAN NANDI.")