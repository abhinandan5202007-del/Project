# Project

# Shopping World: Your All-in-One Retail Manager

Shopping World is a bridge between a digital storefront and a backend warehouse. Built using Python and MySQL, it’s designed to handle the messy reality of retail—managing customers, tracking shifting stock levels, and generating instant bills—all from a clean, interactive command-line interface.

**What can it do?**
I designed this system to serve two different types of people: the shopper looking for a smooth experience and the admin who needs total control over the data.

# For the Customer: A Seamless Shopping Trip 
The customer side is all about getting from "browsing" to "bought" without any hiccups:

**Personalized Accounts:** New users can sign up in seconds, while returning customers can log straight back into their accounts.

**Easy Discovery:** Products are organized into clear categories like Fashion, Daily Essentials, and Electronics, making it easy to find exactly what you need.

**Smart Shopping:** The system acts like a real store clerk—it won’t let you buy more than what’s on the shelf. It validates stock levels in real-time.

**Instant Receipts:** No manual math required. Once you're done, the system generates a clean, professional-looking table showing your items and the total amount due.

# For the Admin: Total Inventory Mastery
The admin side is the "engine room" where the store is managed and maintained:

**Birds-Eye View:** Admins can pull up the entire inventory at once to see what’s selling and what’s running low.

**Full Creative Control:** Easily add new product lines, adjust prices for sales, or restock items with a few keystrokes.

**Data Cleanup:** Old or discontinued products can be wiped from the system instantly to keep the database clutter-free.

**Gatekeeping:** A dedicated admin login ensures that sensitive inventory data and pricing are only accessible to authorized staff.

**Tech Stack**
**Language:** Python 3.x

**Database:** MySQL

**Libraries:** * mysql-connector-python: For database connectivity.

**prettytable:** For displaying data in a structured, readable format.

**Database Schema**

The system uses three primary tables within the shop database:
Table          |  Primary Key  |         Description
cust_details   |   contact     |  Stores customer name, email, phone, and password.
admin_details  |    user       |  Stores administrator credentials.
inventory      |   product     |   Stores product names, prices, categories, and current stock.












.
